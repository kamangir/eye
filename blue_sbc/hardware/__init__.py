from blueness import module
from blue_options import host

from blue_sbc import NAME
from blue_sbc.env import BLUE_SBC_HARDWARE_KIND
from blue_sbc.hardware.hardware import Hardware as Hardware_Class
from blue_sbc.logger import logger

NAME = module.name(__file__, NAME)


if host.is_mac():
    from blue_sbc.hardware.display import Display as Hardware_Class
elif BLUE_SBC_HARDWARE_KIND == "adafruit_rgb_matrix":
    from blue_sbc.hardware.adafruit_rgb_matrix import (
        Adafruit_Rgb_Matrix as Hardware_Class,
    )
elif BLUE_SBC_HARDWARE_KIND == "grove":
    from blue_sbc.hardware.grove import Grove as Hardware_Class
elif BLUE_SBC_HARDWARE_KIND == "prototype_hat":
    if host.is_headless():
        from blue_sbc.hardware.hat.prototype import Prototype_Hat as Hardware_Class
    else:
        from blue_sbc.hardware.display import Display as Hardware_Class
elif BLUE_SBC_HARDWARE_KIND == "scroll_phat_hd":
    from blue_sbc.hardware.scroll_phat_hd import Scroll_Phat_HD as Hardware_Class
elif BLUE_SBC_HARDWARE_KIND == "sparkfun-top-phat":
    from blue_sbc.hardware.sparkfun_top_phat.classes import (
        Sparkfun_Top_phat as Hardware_Class,
    )
elif BLUE_SBC_HARDWARE_KIND == "unicorn_16x16":
    from blue_sbc.hardware.unicorn_16x16 import Unicorn_16x16 as Hardware_Class
else:
    raise NameError(f"blue-sbc: {BLUE_SBC_HARDWARE_KIND}: hardware not found.")

hardware = Hardware_Class()

logger.info(f"{NAME}: {BLUE_SBC_HARDWARE_KIND}: {hardware.__class__.__name__}")
