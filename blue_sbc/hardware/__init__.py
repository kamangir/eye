from blue_sbc.hardware.hardware import Hardware as Hardware_Class
from abcli.modules.cookie import cookie
from abcli.modules import host
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.hardware"

hardware_kind = cookie.get("hardware.kind", "prototype_hat")
if host.is_mac():
    from .display import Display as Hardware_Class
elif hardware_kind == "adafruit_rgb_matrix":
    from .adafruit_rgb_matrix import Adafruit_Rgb_Matrix as Hardware_Class
elif hardware_kind == "grove":
    from .grove import Grove as Hardware_Class
elif hardware_kind == "prototype_hat":
    if host.is_headless():
        from .hat.prototype import Prototype_Hat as Hardware_Class
    else:
        from .display import Display as Hardware_Class
elif hardware_kind == "scroll_phat_hd":
    from .scroll_phat_hd import Scroll_Phat_HD as Hardware_Class
elif hardware_kind == "sparkfun-top-phat":
    from .sparkfun_top_phat.classes import Sparkfun_Top_phat as Hardware_Class
elif hardware_kind == "unicorn_16x16":
    from .unicorn_16x16 import Unicorn_16x16 as Hardware_Class
else:
    raise NameError(f"-blue-sbc: {hardware_kind}: hardware not found.")

hardware = Hardware_Class()

logger.info(f"{NAME}: {hardware_kind}: {hardware.__class__.__name__}")
