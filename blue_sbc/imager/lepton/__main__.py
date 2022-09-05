import argparse
from blue_sbc.screen.display import instance as display
from . import *
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="capture|preview",
)
parser.add_argument(
    "--filename",
    default="",
    type=str,
)
parser.add_argument(
    "--output_path",
    type=str,
    default="",
)
args = parser.parse_args()

success = False
if args.task == "capture":
    success, _, _ = instance.capture(
        filename=os.path.join(args.output_path, "camera.jpg"),
        forced=True,
    )
elif args.task == "preview":
    try:
        while not display.pressed("qe"):
            success_, _, image = instance.capture(
                filename="-",
                sign=False,
            )
            if not success_:
                continue

            display.show(
                image,
                [],
                [],
                on_screen=True,
                sign=False,
            )

        success = True
    finally:
        pass
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
