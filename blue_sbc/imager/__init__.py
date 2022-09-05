from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.imager"

from .classes import *

imager_name = cookie.get("session.imager", "camera")
if imager_name == "lepton":
    from .lepton import instance as imager
else:
    from .camera import instance as imager

logger.info(f"{NAME}: imager: {imager.__class__.__name__}")
