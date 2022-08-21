from blue_eye import NAME
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def start_session():
    logger.info(f"{NAME}: start_session()")
    logger.info(f"{NAME}: end_session()")
    return True
