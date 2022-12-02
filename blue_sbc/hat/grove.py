from blue_sbc.hat.hat import Hat
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24


class Grove_Hat(Hat):
    def __init__(self, is_rpi=True):
        super(Grove_Hat, self).__init__()

    def input(self, pin):
        return False

    def output(self, pin, output):
        return self

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")
        return self

    def setup(self, pin, what, pull_up_down=None):
        return self
