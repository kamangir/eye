import numpy as np
import cv2
from . import NAME
from .legacy import get_demo, grid_print, progress
from abcli import file
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class GoLpy(object):
    def __init__(self, height, width):
        self.generation = 0
        self.buffer = np.zeros((height, width), dtype="uint8")
        self.input = None
        self.status = True

    def blank(self):
        return not bool(np.sum(self.buffer))

    def init(self, input=None):
        if input is None or input == "":
            self.buffer = get_demo("random", (self.width, self.height), "TL")
        else:
            if isinstance(input, str):
                success, input = file.load_image(input)
                if not success:
                    return self

            input = cv2.resize(input, (self.width, self.height))

            if len(input.shape) > 2 and input.shape[2] == 3:
                input = input[:, :, 0]

            _, self.buffer = cv2.threshold(
                input, 0, 1, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )

        logger.info(f"{NAME}.init({string.pretty_shape_of_matrix(self.buffer)})")

        self.input = np.copy(self.buffer)

        return self

    @property
    def height(self):
        return self.buffer.shape[0]

    def grid(self, x=None, y=None):
        if x is None or y is None:
            output = np.copy(self.buffer)
            self.status = not self.status
            output[0, 0] = self.status
            return output

        if not x and not y:
            self.status = not self.status
            return int(self.status)

        return self.buffer[x, y]

    def print(self):
        grid_print(self.buffer, self.generation)
        return self

    def progress(self):
        self.generation += 1
        progress(self.buffer)
        return self

    def re_init(self):
        if self.input is not None:
            self.buffer = np.copy(self.input)
        else:
            self.init()
        return self

    @property
    def width(self):
        return self.buffer.shape[1]
