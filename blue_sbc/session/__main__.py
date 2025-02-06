import argparse
import importlib

from blueness import module
from blue_options.logger import crash_report

from blue_sbc import fullname, NAME
from blue_sbc.session.classes import Session
from blue_sbc.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="start",
)
parser.add_argument(
    "--application",
    type=str,
    default="",
)
args = parser.parse_args()

success = False
if args.task == "start":
    application = None
    if args.application:
        logger.info(f"session.application: {args.application}")
        try:
            # https://stackoverflow.com/a/13598111/17619982
            module = importlib.import_module(args.application, package=None)
            logger.info(f"loaded {args.application}: {module}")

            application = module.Application()
            logger.info(f"created an {application}.")

            success = True
        except Exception as e:
            crash_report(e)

    if success or not args.application:
        logger.info(f"{fullname()}.session.start({application.__class__.__name__})")

        success = Session.start(application)
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
