from blue_sbc.hat.hat import Hat
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Grove_Hat(Hat):
    def __init__(self, is_rpi=True):
        super(Grove_Hat, self).__init__()

        self.looper_pin = -1  # red led
        self.incoming_pin = -2  # yellow led
        self.data_pin = -3  # green led

    def input(self, pin):
        return False

    def output(self, pin, output):
        print(f"grove_hat.output({pin},{output})")
        return self

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")
        return self

    def setup(self, pin, what, pull_up_down=None):
        return self
