import argparse

from blueness import module

from blue_sbc import NAME
from blue_sbc.session.classes import Session
from blue_sbc.logger import logger

NAME = module.name(__file__, NAME)


parser = argparse.ArgumentParser(NAME)
parser.add_argument(
    "task",
    type=str,
    help="start",
)
args = parser.parse_args()

success = False
if args.task == "start":
    success = Session.start()
else:
    logger.error(f"-{NAME}: {args.task}: command not found.")

if not success:
    logger.error(f"-{NAME}: {args.task}: failed.")
