import time
from abcli import VERSION
from abcli.modules.display import instance as display
from abcli import file
from abcli.modules.hardware import instance as hardware
from abcli.modules import terraform
from abcli.plugins import storage
from abcli.plugins.message.messenger import instance as messenger
from abcli import string
from abcli.timer import Timer
from abcli.modules import host
from . import NAME
from .functions import return_to_bash
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)

if host.cookie.get("camera") == "lepton":
    from blue_eye.camera.lepton import instance as camera
else:
    from blue_eye.camera import instance as camera
logger.info(f"camera: {camera.__class__.__name__}")


class Session(object):
    def __init__(self, output=""):
        super(Session, self).__init__()

        self.keys = {
            "e": "exit",
            "r": "reboot",
            "s": "shutdown",
            "u": "update",
        }

        self.capture_requested = False

        self.new_frame = False
        self.frame_image = terraform.poster(None)
        self.frame_filename = ""

        self.auto_upload = host.cookie.get("session.auto_upload", True)
        self.outbound_queue = host.cookie.get("session.outbound_queue", "stream")
        self.capture_enabled = host.cookie.get("session.capture.enabled", True)

        self.output = output

        self.messages = []

        self.model = None

        self.params = {"iteration": -1}

        self.state = {}

        self.switch_on_time = None

        self.timer = {}
        for name, period in {
            "capture": 60 * 5,
            "display": 4,
            "messenger": 60,
            "reboot": 60 * 60 * 4,
            "temperature": 300,
        }.items():
            self.add_timer(name, period)

    def add_timer(self, name, period):
        if name not in self.timer:
            period = host.cookie.get(f"session.{name}.period", period)
            self.timer[name] = Timer(period, name)
            logger.info(
                "session: timer[{}]:{}".format(
                    name, string.pretty_frequency(1 / period)
                )
            )
            return True
        return False

    def check_camera(self):
        self.new_frame = False

        if not self.capture_enabled or (
            not self.capture_requested and not self.timer["capture"].tick()
        ):
            return

        success, filename, image = camera.capture(
            forced=self.capture_requested,
        )

        self.capture_command = ""

        if not filename or filename == "same" or not success:
            return

        hardware.pulse(hardware.data_pin)

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

    def check_keyboard(self):
        for key in display.key_buffer:
            if key in self.keys:
                return_to_bash(self.keys[key])
                return False

        if " " in display.key_buffer:
            self.capture_requested = True

        display.key_buffer = []

        return None

    def check_messages(self):
        self.messages = []

        if not self.timer["messenger"].tick():
            return None

        _, self.messages = messenger.request()
        if self.messages:
            hardware.pulse(hardware.incoming_pin)

        for message in self.messages:
            output = self.process_message(message)
            if output in [True, False]:
                return output

        return None

    def process_message(self, message):
        if message.event == "capture":
            logger.info(f"{NAME}: capture message received.")
            self.capture_requested = True

        if message.event in "reboot,shutdown".split(","):
            logger.info(f"{NAME}: {message.event} message received.")
            return_to_bash(message.event)
            return False

        if message.event == "update":
            try:
                if message.data["version"] > VERSION:
                    return_to_bash("update")
                    return False
            except:
                crash_report("looper.process_message() bad update message")

        return None

    def check_seed(self):
        seed_filename = host.get_seed_filename()
        if not file.exist(seed_filename):
            return None

        success, content = file.load_json(f"{seed_filename}.json")
        if not success:
            return None

        hardware.pulse("outputs")

        seed_version = content.get("version", "")
        if seed_version <= VERSION:
            return None

        logger.info(f"{NAME}: seed {seed_version} detected.")
        return_to_bash("seed", [seed_filename])
        return False

    def check_switch(self):
        if hardware.activated(hardware.switch_pin):
            if self.switch_on_time is None:
                self.switch_on_time = time.time()
                logger.info("{NAME}: switch_on_time was set.")
        else:
            self.switch_on_time = None

        if self.switch_on_time is not None:
            hardware.pulse("outputs")

            if time.time() - self.switch_on_time > 10:
                return_to_bash("shutdown")
                return False
            else:
                return True

        return None

    def check_timers(self):
        if self.timer["display"].tick():
            display.show(
                image=self.frame_image,
                header=self.signature(),
                sidebar=string.pretty_param(self.params),
                on_screen=self.output == "screen",
            )

        if self.timer["reboot"].tick("wait"):
            return_to_bash("reboot")
            return False

        if self.timer["temperature"].tick():
            self.read_temperature()

        return None

    def close(self):
        hardware.release()

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
                except:
                    crash_report(f"{NAME}.read_temperature(cpu) failed")
                    return

        self.params.update(params)
        logger.info(
            "{}: {}".format(
                NAME,
                ", ".join(string.pretty_param(params)),
            )
        )

    def signature_(self):
        return (
            sorted([timer.signature() for timer in self.timer.values()])
            + (["*"] if self.new_frame else [])
            + (["^"] if self.auto_upload else [])
            + ([f">{self.outbound_queue}"] if self.outbound_queue else [])
            + ([f"hat:{hardware.hat}"] if hardware.hat else [])
            + (
                [
                    "switch:{}".format(
                        string.pretty_duration(
                            time.time() - self.switch_on_time,
                            largest=True,
                            short=True,
                        )
                    )
                ]
                if self.switch_on_time is not None
                else []
            )
        )

    def signature(self):
        return [" | ".join(self.signature_())] + (
            [] if self.model is None else [" | ".join(self.model.signature())]
        )

    def step(
        self,
        steps="all",
    ):
        """step session.

        Args:
            steps (str, optional): steps. Defaults to "all".

        Returns:
            bool: success.
        """
        if steps == "all":
            steps = "camera,keyboard,messages,seed,switch,timers".split(",")

        self.params["iteration"] += 1

        hardware.pulse(hardware.looper_pin, 0)

        for enabled, step_ in zip(
            [
                "keyboard" in steps,
                "messages" in steps,
                "timers" in steps,
                "switch" in steps,
                "seed" in steps,
                "camera" in steps,
            ],
            [
                self.check_keyboard,
                self.check_messages,
                self.check_timers,
                self.check_switch,
                self.check_seed,
                self.check_camera,
            ],
        ):
            if not enabled:
                continue
            output = step_()
            if output in [False, True]:
                return output

        return True
