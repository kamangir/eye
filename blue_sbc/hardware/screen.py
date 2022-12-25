import copy
import cv2
import random
from .hardware import Hardware
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Screen(Hardware):
    def __init__(self):
        super().__init__()
        self.size = None

        self.buffer = None

    def update_screen(self, image, session, header, sidebar):
        if self.animated:
            self.buffer = copy.deepcopy(image)

        return super().update_screen(image, session, header, sidebar)
