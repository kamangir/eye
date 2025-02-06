import argparse
import os

from blueness import module

from blue_sbc import NAME
from blue_sbc.imager.camera import instance as camera
from blue_sbc.hardware import hardware
from blue_sbc.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    default="",
    help="capture|capture_video|preview",
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
    help="0|1",
)
args = parser.parse_args()

success = False
if args.task == "capture":
    success, _, _ = camera.capture(
        filename=os.path.join(args.output_path, "camera.jpg")
    )
elif args.task == "capture_video":
    success = camera.capture_video(
        args.filename,
        args.length,
        preview=args.preview,
        resolution=(728, 600),
    )
elif args.task == "preview":
    hardware.sign_images = False
    try:
        camera.open(
            log=True,
            resolution=(320, 240),
        )

        while not hardware.pressed("qe"):
            _, image = camera.capture(
                close_after=False,
                log=False,
                open_before=False,
            )
            hardware.update_screen(image, None, [], [])

        success = True

    except KeyboardInterrupt:
        logger.info("Ctrl+C, stopping.")

    finally:
        camera.close(log=True)
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
