from abcli.modules import host
from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.hardware"

hardware_kind = cookie.get("hardware.kind", "led_switch")
if hardware_kind == "adafruit_rgb_matrix":
    from .adafruit_rgb_matrix import instance as hardware
elif hardware_kind == "grove":
    from .grove import instance as hardware
elif hardware_kind == "led_switch":
    from .led_switch import instance as hardware
elif hardware_kind == "scroll_phat_hd":
    from .scroll_phat_hd import instance as hardware
elif hardware_kind == "sparkfun-top-phat":
    from .sparkfun_top_phat import instance as hardware
elif hardware_kind == "unicorn_16x16":
    from .unicorn_16x16 import instance as hardware
else:
    raise NameError(f"-blue-sbc: {hardware_kind}: hardware not found.")

logger.info(f"{NAME}: {hardware.__class__.__name__}")
