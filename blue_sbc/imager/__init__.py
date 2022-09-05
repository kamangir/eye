from abcli.modules.cookie import cookie

NAME = "blue_sbc.imager"

from .classes import *

if cookie.get("session.imager") == "lepton":
    from .lepton import instance as imager
else:
    from .camera import instance as imager

logger.info(f"{NAME}: imager: {imager.__class__.__name__}")
