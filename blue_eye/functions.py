from . import name
from abcli import logging
import logging

logger = logging.getLogger(__name__)


def start_session():
    logger.info("blue-eye: start_session()")
    logger.info("blue-eye: end_session()")
    return True
