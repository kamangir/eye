import os

from blueness import module
from blue_options import string
from blue_options import host
from blue_options.logger import crash_report
from blue_options.timer import Timer
from blue_objects import file
from blue_objects import objects
from blue_objects.storage import instance as storage
from blue_objects.graphics.signature import add_signature
from abcli import VERSION as abcli_VERSION
from abcli.modules import terraform
from blue_objects.env import abcli_object_name
from abcli.plugins.message.messenger import instance as messenger

from blue_sbc import NAME
from blue_sbc import env
from blue_sbc.host import signature
from blue_sbc.session.functions import reply_to_bash
from blue_sbc.algo.diff import Diff
from blue_sbc.hardware import hardware
from blue_sbc.imager import imager
from blue_sbc.logger import logger


NAME = module.name(__file__, NAME)


class Session:
    def __init__(self):
        self.bash_keys = {
            "e": "exit",
            "r": "reboot",
            "s": "shutdown",
            "u": "update",
        }

        self.diff = Diff(env.BLUE_SBC_SESSION_IMAGER_DIFF)

        self.capture_requested = False

        self.frame = 0
        self.new_frame = False
        self.frame_image = terraform.poster(None)
        self.frame_filename = ""

        self.auto_upload = env.BLUE_SBC_SESSION_AUTO_UPLOAD
        self.outbound_queue = env.BLUE_SBC_SESSION_OUTBOUND_QUEUE

        self.messages = []

        self.model = None

        self.params = {"iteration": -1}

        self.state = {}

        self.timer = {}
        for name, period in {
            "imager": env.BLUE_SBC_SESSION_IMAGER_PERIOD,
            "messenger": env.BLUE_SBC_SESSION_MESSENGER_PERIOD,
            "reboot": env.BLUE_SBC_SESSION_REBOOT_PERIOD,
            "screen": env.BLUE_SBC_SESSION_SCREEN_PERIOD,
            "temperature": env.BLUE_SBC_SESSION_TEMPERATURE_PERIOD,
        }.items():
            self.add_timer(name, period)

    def add_timer(
        self,
        name: str,
        period: float,
    ):
        if name not in self.timer:
            self.timer[name] = Timer(period, name)
            logger.info(
                "{}: timer[{}]:{}".format(
                    NAME,
                    name,
                    string.pretty_frequency(1 / period),
                )
            )
            return True
        return False

    def check_imager(self):
        self.new_frame = False

        if not env.BLUE_SBC_SESSION_IMAGER_ENABLED:
            return
        if not self.capture_requested and not self.timer["imager"].tick():
            return
        self.capture_requested = False

        success, image = imager.capture()
        if not success:
            return

        hardware.pulse("data")

        if self.diff.same(image):
            return

        self.frame += 1

        image = add_signature(
            image,
            [" | ".join(objects.signature(self.frame))],
            [" | ".join(signature())],
        )

        filename = objects.path_of(
            object_name=abcli_object_name,
            filename=f"{self.frame:016d}.jpg",
        )
        if not file.save_image(filename, image):
            return

        self.new_frame = True
        self.frame_image = image
        self.frame_filename = filename

        if self.outbound_queue:
            from abcli.plugins.message import Message

            Message(
                filename=self.frame_filename,
                recipient=self.outbound_queue,
                subject="frame",
            ).submit()
        elif self.auto_upload:
            storage.upload_file(self.frame_filename)

    def check_keys(self):
        for key in hardware.key_buffer:
            if key in self.bash_keys:
                reply_to_bash(self.bash_keys[key])
                return False

        if " " in hardware.key_buffer:
            self.capture_requested = True

        hardware.key_buffer = []

        return None

    def check_messages(self):
        self.messages = []

        if not self.timer["messenger"].tick():
            return None

        _, self.messages = messenger.request()
        if self.messages:
            hardware.pulse("incoming")

        for message in self.messages:

            output = self.process_message(message)
            if output in [True, False]:
                return output

        return None

    def check_seed(self):
        seed_filename = host.get_seed_filename()
        if not file.exists(seed_filename):
            return None

        success, content = file.load_json(file.set_extension(seed_filename, "json"))
        if not success:
            return None

        hardware.pulse("outputs")

        seed_version = content.get("version", "")
        if seed_version <= abcli_VERSION:
            return None

        logger.info(f"{NAME}: seed {seed_version} detected.")
        reply_to_bash("seed", [seed_filename])
        return False

    def check_timers(self):
        if self.timer["screen"].tick():
            hardware.update_screen(
                image=self.frame_image,
                session=self,
                header=self.signature(),
            )
        elif hardware.animated:
            hardware.animate()

        if self.timer["reboot"].tick("wait"):
            reply_to_bash("reboot")
            return False

        if self.timer["temperature"].tick():
            self.read_temperature()

        return None

    def close(self):
        hardware.release()

    def process_message(self, message):
        if (
            env.BLUE_SBC_SESSION_OUTBOUND_QUEUE
            and message.subject in "bolt,frame".split(",")
            and not host.is_headless()
        ):
            logger.info(f"{NAME}: frame received: {message.as_string()}")
            self.new_frame, self.frame_image = file.load_image(message.filename)

        if message.subject == "capture":
            logger.info(f"{NAME}: capture message received.")
            self.capture_requested = True

        if message.subject in "reboot,shutdown".split(","):
            logger.info(f"{NAME}: {message.subject} message received.")
            reply_to_bash(message.subject)
            return False

        if message.subject == "update":
            try:
                if message.data["version"] > abcli_VERSION:
                    reply_to_bash("update")
                    return False
            except Exception as e:
                crash_report(e)

        return None

    # https://www.cyberciti.biz/faq/linux-find-out-raspberry-pi-gpu-and-arm-cpu-temperature-command/
    def read_temperature(self):
        if not host.is_rpi():
            return

        params = {}

        success, output = file.load_text("/sys/class/thermal/thermal_zone0/temp")
        if success:
            output = [thing for thing in output if thing]
            if output:
                try:
                    params["temperature.cpu"] = float(output[0]) / 1000
                except Exception as e:
                    crash_report(e)
                    return

        self.params.update(params)
        logger.info(
            "{}: {}".format(
                NAME,
                ", ".join(string.pretty_param(params)),
            )
        )

    def signature(self):
        return [
            " | ".join(objects.signature()),
            " | ".join(sorted([timer.signature() for timer in self.timer.values()])),
            " | ".join(
                (["*"] if self.new_frame else [])
                + (["^"] if self.auto_upload else [])
                + ([f">{self.outbound_queue}"] if self.outbound_queue else [])
                + hardware.signature()
                + [
                    "diff: {:.03f} - {}".format(
                        self.diff.last_diff,
                        string.pretty_duration(
                            self.diff.last_same_period,
                            largest=True,
                            include_ms=True,
                            short=True,
                        ),
                    ),
                    string.pretty_shape_of_matrix(self.frame_image),
                ]
                + ([] if self.model is None else self.model.signature())
            ),
        ]

    @staticmethod
    def start():
        success = True
        logger.info(f"{NAME}: started ...")

        try:
            session = Session()

            while session.step():
                pass

            logger.info(f"{NAME}: stopped.")
        except KeyboardInterrupt:
            logger.info(f"{NAME}: Ctrl+C: stopped.")
            reply_to_bash("exit")
        except Exception as e:
            crash_report(e)
            success = False

        try:
            session.close()
        except Exception as e:
            crash_report(e)
            success = False

        return success

    def step(
        self,
        steps="all",
    ) -> bool:
        if steps == "all":
            steps = "imager,keys,messages,seed,switch,timers".split(",")

        self.params["iteration"] += 1

        hardware.pulse("loop", 0)

        for enabled, step_ in zip(
            [
                "keys" in steps,
                "messages" in steps,
                "timers" in steps,
                "seed" in steps,
                "imager" in steps,
            ],
            [
                self.check_keys,
                self.check_messages,
                self.check_timers,
                self.check_seed,
                self.check_imager,
            ],
        ):
            if not enabled:
                continue
            output = step_()
            if output in [False, True]:
                return output

            hardware.clock()

        return True
