import numpy as np
import os
import os.path
from abcli import file
from abcli import path
from abcli import string
from abcli.modules import host
from abcli.plugins import graphics
from blue_sbc.imager.classes import Imager
from . import NAME
import abcli.logging
import logging

logger = logging.getLogger(__name__)


class Lepton(Imager):
    def capture(self):
        success = True
        image = np.ones((1, 1, 3), dtype=np.uint8) * 127

        temp_dir = path.auxiliary("lepton")
        success = host.shell(
            f"python python2.py capture --output_path {temp_dir}",
            work_dir="{}/blue-sbc/blue_sbc/imager/lepton".format(
                os.getenv("abcli_path_git", "")
            ),
        )

        if success:
            success, image = file.load_image(f"{temp_dir}/image.jpg")

        if success:
            logger.info(f"{NAME}.capture(): {string.pretty_shape_of_matrix(image)}")

        return success, image
