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
    def capture(
        self,
        filename="",
        forced=True,
        sign=True,
    ):
        success, filename, image = super(Lepton, self).capture(filename)

        temp_dir = path.auxiliary("lepton")
        success = host.shell(
            f"python python2.py capture --output_path {temp_dir}",
            work_dir="{}/blue-sbc/blue_sbc/imager/lepton".format(
                os.getenv("abcli_path_git", "")
            ),
        )

        if success:
            success, image = file.load_image(f"{temp_dir}/image.jpg")

        if success and sign:
            image = graphics.add_signature(image, [], self.signature(image))

        if success:
            filename = self.filename_of(filename)

            if filename:
                success = file.save_image(filename, image)

                if success:
                    success = file.copy(
                        f"{temp_dir}/image_raw.jpg",
                        f"{file.path(filename)}/image_raw.jpg",
                    )

        if success:
            logger.info(
                "{}.capture(): {}{}".format(
                    NAME,
                    "{} - ".format(filename) if filename else "",
                    string.pretty_shape_of_matrix(image),
                )
            )

        return success, filename, image
