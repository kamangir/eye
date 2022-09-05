import argparse
import cv2
import numpy as np
import os
from time import sleep
from abcli.modules import objects
from abcli import file
from abcli.modules import host
from abcli.modules.cookie import cookie
from abcli.plugins import graphics
from abcli import string
from . import NAME
from blue_sbc.algo.diff import Diff
from blue_sbc.display import instance as display
from blue_sbc.hardware import instance as hardware
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Imager(object):
    def __init__(self):
        self.frame = -1
        self.unique_frame = -1

        self.diff = Diff(cookie.get("camera.diff", 0.1))

    def capture(self):
        self.frame += 1
        return False, "", np.ones((1, 1, 3), dtype=np.uint8) * 127

    def filename_of(
        self,
        filename="",
    ):
        """produce filename.

        Args:
            filename           : filename. Default to "".
            name_and_extension : name and extension. Default to "camera.jpg".

        Returns:
            str: filename
        """
        if "filename" == "-":
            return ""

        filename = (
            filename
            if filename
            else os.path.join(
                os.getenv("abcli_object_path", ""),
                f"{self.frame:05d}.jpg",
            )
        )

        file.prepare_for_saving(filename)

        return filename

    def signature(self, image):
        return [
            " | ".join(
                objects.signature(self.frame)
                + [
                    string.pretty_shape_of_matrix(image),
                    self.__class__.__name__.lower(),
                ]
                + self.signature_()
            ),
            " | ".join(host.signature()),
        ]

    def signature_(self):
        return []


class TemplateImager(Imager):
    def __init__(self):
        pass

    def capture(self, filename="", sign=True):
        """capture.

        Args:
            filename (str, optional): filename. Defaults to "": use timestamp.
            sign (bool, optional): sign output. Defaults to True.

        Returns:
            bool: success.
        """
        _, _, image_blank = super(TemplateImager, self).capture()

        filename = self.filename_of(filename)

        return False, filename, image_blank

    def signature_(self):
        return ["device_name"]
