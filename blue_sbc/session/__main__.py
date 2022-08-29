import argparse
from . import *
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
    "output",
    type=str,
    default="",
    help="file|screen",
)
args = parser.parse_args()

success = False
if args.task == "start":
    success = start_session(
        Session,
        output=args.output,
    )
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
