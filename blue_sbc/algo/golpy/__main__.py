import argparse
import time
from . import *
from blue_sbc.screen.display import instance as display
from abcli import logging
import logging

logger = logging.getLogger(__name__)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="simulate",
)
parser.add_argument(
    "--height",
    type=int,
    default=17,
)
parser.add_argument(
    "--input",
    type=str,
    default="",
)
parser.add_argument(
    "--display",
    type=int,
    default=0,
)
parser.add_argument(
    "--width",
    type=int,
    default=7,
)
args = parser.parse_args()

success = False
if args.task == "simulate":
    golpy = GoLpy(args.height, args.width)
    golpy.init(args.input)

    try:
        while True:
            if args.display:
                if display.pressed("qe"):
                    break
                if display.pressed(" "):
                    golpy.re_init()
                display.show(
                    image=255 * golpy.grid(),
                    on_screen=True,
                    sign=False,
                )
            else:
                golpy.print()

            if golpy.blank():
                golpy.re_init()
            else:
                golpy.progress()

            time.sleep(0.1)

    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")

    success = True
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
