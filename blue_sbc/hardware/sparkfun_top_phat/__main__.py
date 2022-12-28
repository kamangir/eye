import argparse
import time
from . import *
from .classes import Sparkfun_Top_phat
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="validate_leds",
)
args = parser.parse_args()

hardware = Sparkfun_Top_phat()

success = False
if args.task == "validate_leds":
    logger.info("loop started (Ctrl+C to stop)")
    # https://stackoverflow.com/a/18994932/10917551
    try:
        while True:
            for index in range(hardware.pixel_count):
                hardware.pixels[index] = (10, 0, 0)

            hardware.pixels.show()
            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")
    finally:
        hardware.release()
    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
