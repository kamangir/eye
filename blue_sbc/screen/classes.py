import cv2
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Screen(object):
    def __init__(self):
        self.key_buffer = []
        self.interpolation = cv2.INTER_LINEAR
        self.sign_images = True
        self.size = None

    def pressed(self, keys):
        return False

    def release(self):
        logger.info(f"{self.__class__.__name__}.release()")

    def show(
        self,
        image,
        session=None,
        header=[],
        sidebar=[],
    ):
        return self
