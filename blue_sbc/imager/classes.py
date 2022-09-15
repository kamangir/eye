import numpy as np
import os
from abcli import file
from abcli.modules import host
from abcli.modules.cookie import cookie
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Imager(object):
    pass


class TemplateImager(Imager):
    def capture(self):
        """capture.

        Returns:
            bool: success.
            image: np.ndarray.
        """
        success = True
        image = np.ones((1, 1, 3), dtype=np.uint8) * 127

        # TODO: capture the image here

        return success, image

    def signature(self):
        return ["device_name"]
