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
    default="info.h264",
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
        {
            "filename": os.path.join(args.output_path, "camera.jpg"),
            "forced": True,
        }
    )
elif args.task == "capture_video":
    success = instance.capture_video(
        args.filename,
        args.length,
        {"preview": args.preview, "resolution": (728, 600)},
    )
elif args.task == "preview":
    try:
        instance.open("log")

        while not display.pressed("qe"):
            success_, _, image = instance.capture(
                "~close,filename=-,forced,~log,~open,~sign,~save"
            )
            if not success_:
                continue

            display.show(image, [], [], "screen,~sign")

        success = True
    finally:
        instance.close("log")
else:
    logger.error('camera: unknown task "{}".'.format(args.task))

if not success:
    logger.error("camera({}): failed.".format(args.task))
