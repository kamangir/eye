from blue_sbc.hardware.hardware import Hardware_Class
from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.hardware"

hardware_kind = cookie.get("hardware.kind", "led_switch_hat")
if hardware_kind == "adafruit_rgb_matrix":
    from .adafruit_rgb_matrix import Adafruit_Rgb_Matrix as Hardware_Class
elif hardware_kind == "grove":
    from .grove import Grove as Hardware_Class
elif hardware_kind == "prototype_switch_hat":
    from .hat.prototype import Prototype_Hat as Hardware_Class
elif hardware_kind == "scroll_phat_hd":
    from .scroll_phat_hd import Scroll_Phat_HD as Hardware_Class
elif hardware_kind == "sparkfun-top-phat":
    from .sparkfun_top_phat import Sparkfun_Top_phat as Hardware_Class
elif hardware_kind == "unicorn_16x16":
    from .unicorn_16x16 import Unicorn_16x16 as Hardware_Class
else:
    raise NameError(f"-blue-sbc: {hardware_kind}: hardware not found.")

hardware = Hardware_Class()

logger.info(f"{NAME}: {hardware.__class__.__name__}")
