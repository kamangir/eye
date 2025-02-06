from typing import Tuple
import numpy as np
import os.path

from blueness import module
from blue_options import string
from blue_objects import file
from blue_objects import path
from blue_objects.env import abcli_path_git
from blue_objects.host import shell

from blue_sbc import NAME
from blue_sbc.imager.classes import Imager
from blue_sbc.logger import logger


NAME = module.name(__file__, NAME)


class Lepton(Imager):
    def capture(self) -> Tuple[bool, np.ndarray]:
        success, image = super().capture()

        temp_dir = path.auxiliary("lepton")
        success = shell(
            f"python python2.py capture --output_path {temp_dir}",
            work_dir=f"{abcli_path_git}/blue-sbc/blue_sbc/imager/lepton",
        )

        if success:
            success, image = file.load_image(f"{temp_dir}/image.jpg")

        if success:
            logger.info(f"{NAME}.capture(): {string.pretty_shape_of_matrix(image)}")

        return success, image
