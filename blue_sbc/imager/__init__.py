from blueness import module

from blue_sbc import NAME
from blue_sbc import env
from blue_sbc.logger import logger

NAME = module.name(__file__, NAME)


imager_name = env.BLUE_SBC_SESSION_IMAGER
if imager_name == "lepton":
    from blue_sbc.imager.lepton import instance as imager
else:
    from blue_sbc.imager.camera import instance as imager

logger.info(f"{NAME}: {imager_name}: {imager.__class__.__name__}")
