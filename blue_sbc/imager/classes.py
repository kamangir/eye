import numpy as np
import os
from abcli.modules import objects
from abcli import file
from abcli.modules import host
from abcli.modules.cookie import cookie
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Imager(object):
    def __init__(self):
        self.frame = -1

    def capture(self, filename):
        self.frame += 1
        return False, filename, np.ones((1, 1, 3), dtype=np.uint8) * 127

    def filename_of(
        self,
        filename="",
    ):
        """produce filename.

        Args:
            filename : filename. Default to "".

        Returns:
            str: filename
        """
        if filename == "-":
            return ""

        filename = (
            filename
            if filename
            else os.path.join(
                os.getenv("abcli_object_path", ""),
                f"{self.frame:016d}.jpg",
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

    def capture(
        self,
        filename="",
        sign=True,
    ):
        """capture.

        Args:
            filename (str, optional): filename. Defaults to "": use timestamp.
            sign (bool, optional): sign output. Defaults to True.

        Returns:
            bool: success.
        """
        _, _, image_blank = super(TemplateImager, self).capture()

        filename = self.filename_of(filename)

        # TODO: capture the image here
        image = image_blank

        return True, filename, image

    def signature_(self):
        return ["device_name"]
