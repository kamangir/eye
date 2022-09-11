import argparse
import time
from . import *
from . import instance as hat
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="input/output",
)
parser.add_argument(
    "--outputs",
    type=str,
    default="",
)
args = parser.parse_args()

success = False
if args.task == "input":
    logger.info("loop started (Ctrl+C to stop)")
    # https://stackoverflow.com/a/18994932/10917551
    try:
        while True:
            logger.info(
                "inputs: {}".format(
                    ", ".join([str(hat.input(pin)) for pin in hat.input_pins])
                )
            )
            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")
    finally:
        hat.release()
    success = True
elif args.task == "output":
    outputs = args.outputs + len(hat.output_pins) * "1"
    for index, pin in enumerate(hat.output_pins):
        hat.output(pin, outputs[index] == "1")
    hat.release()
    success = True
elif args.task == "validate":
    logger.info("loop started (Ctrl+C to stop)")
    value = True
    try:
        while True:
            activity = False
            for pin, pin_name in zip(
                [
                    hat.green_switch_pin,
                    hat.red_switch_pin,
                    hat.switch_pin,
                    hat.trigger_pin,
                ],
                "green_switch_pin,red_switch_pin,switch_pin,trigger_pin".split(","),
            ):
                if hat.activated(pin):
                    logger.info(
                        "{}: {} activated.".format(
                            string.timestamp(ms=True),
                            pin_name,
                        )
                    )
                    activity = True

            for pin in hat.output_pins:
                hat.output(pin, activity or value)
            time.sleep(0.1)

            value = not value
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")
    finally:
        hat.release()
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
