from blue_sbc.hat.hat import Hat
from grove.grove_button import GroveButton
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24


class Grove_Hat(Hat):
    def __init__(self, is_rpi=True):
        super(Grove_Hat, self).__init__()

        self.button = GroveButton(BUTTON)
        self.button.on_press = grove_button_on_press
        self.button.on_release = grove_button_on_release
        logger.info(f"grove.button: {self.button.pin}")

    def input(self, pin):
        return False

    def output(self, pin, output):
        return self

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")
        return self

    def setup(self, pin, what, pull_up_down=None):
        return self


def grove_button_on_press(t):
    logger.info("grove.button: pressed.")


def grove_button_on_release(t):
    logger.info("grove.button: released after {0} seconds.".format(round(t, 6)))
