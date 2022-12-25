import argparse
from . import *
import importlib
from blue_sbc import VERSION
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)

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
        logger.info(f"blue-sbc-{VERSION}: session.application: {args.application}")
        try:
            # https://stackoverflow.com/a/13598111/17619982
            module = importlib.import_module(args.application, package=None)
            logger.info(f"loaded {args.application}: {module}")

            application = module.Application()
            logger.info(f"created an {application}.")

            success = True
        except:
            crash_report(f"-{NAME}: importing {args.application}.Application: failed.")

    if success or not args.application:
        logger.info(f"blue-sbc.session.start({application.__class__.__name__})")

        success = Session.start(application)
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
