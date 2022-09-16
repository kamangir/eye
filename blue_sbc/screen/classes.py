import copy
import cv2
import random
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Screen(object):
    def __init__(self):
        self.key_buffer = []
        self.interpolation = cv2.INTER_LINEAR
        self.sign_images = True
        self.size = None

        self.animated = False
        self.buffer = None

    def animate(self):
        if self.buffer is None:
            return self

        y = random.randint(0, self.buffer.shape[0] - 1)
        x = random.randint(0, self.buffer.shape[1] - 1)

        self.buffer[y, x] = 255 - self.buffer[y, x]

        self.animated = False
        self.show(self.buffer)
        self.animated = True

    def pressed(self, keys):
        return False

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")

    def show(self, image, session=None, header=[], sidebar=[]):
        if self.animated:
            self.buffer = copy.deepcopy(image)
        return self
