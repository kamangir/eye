import argparse
from . import *
from abcli import logging
import logging

logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="capture/capture_video/preview",
)
parser.add_argument(
    "--filename",
    default=os.path.join(os.getenv("abcli_object_path", ""), "info.h264"),
    type=str,
)
parser.add_argument(
    "--length",
    default="10",
    type=int,
)
parser.add_argument(
    "--output_path",
    type=str,
    default="",
)
parser.add_argument(
    "--preview",
    default="1",
    type=int,
    help="0/1",
)
args = parser.parse_args()

success = False
if args.task == "capture":
    success, _, _ = instance.capture(
        filename=os.path.join(args.output_path, "camera.jpg"),
        forced=True,
    )
elif args.task == "capture_video":
    success = instance.capture_video(
        args.filename,
        args.length,
        preview=args.preview,
        resolution=(728, 600),
    )
elif args.task == "preview":
    try:
        instance.open(log=True)

        while not display.pressed("qe"):
            success_, _, image = instance.capture(
                close_after=False,
                filename="-",
                forced=True,
                log=False,
                open_before=False,
                sign=False,
                save=False,
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
        instance.close(log=True)
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
