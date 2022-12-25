import random
from abcli.modules.cookie import cookie
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Hardware(object):
    def __init__(self):
        self.kind = cookie.get("hardware.kind", "led_switch_hat")

        logger.info(f"{self.__class__.__name__}.init({self.kind}).")

        self.key_buffer = []
        self.animated = False

    def animate(self):
        if self.buffer is None:
            return self
        if not self.animated:
            return self

        y = random.randint(0, self.buffer.shape[0] - 1)
        x = random.randint(0, self.buffer.shape[1] - 1)

        self.buffer[y, x] = 255 - self.buffer[y, x]

        self.animated = False
        self.show(self.buffer)
        self.animated = True

    def clock(self):
        return self

    def pulse(self, pin=None, frequency=None):
        """
        pulse pin.
        :param pin: "data" / "incoming" / "loop" / "outputs"
        :param frequency: frequency
        :return: self
        """
        return self

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")

    def signature(self):
        return [f"hardware:{self.kind}"]

    def update_screen(self, image, session, header, sidebar):
        return self
