from abcli.modules.cookie import cookie
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Hardware(object):
    def __init__(self):
        self.kind = cookie.get("hardware.kind", "led_switch")

        logger.info(f"{self.__class__.__name__}.init({self.kind}).")

        self.key_buffer = []
