from abcli.modules import host
from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.hat"

hat_kind = cookie.get("hat.kind", "led_switch")
if hat_kind == "adafruit_rgb_matrix":
    from .adafruit_rgb_matrix import instance as hat
elif hat_kind == "grove":
    from .grove import instance as hat
elif hat_kind == "led_switch":
    from .led_switch import instance as hat
elif hat_kind == "scroll_phat_hd":
    from .scroll_phat_hd import instance as hat
elif hat_kind == "sparkfun-top-phat":
    from .sparkfun_top_phat import instance as hat
elif hat_kind == "unicorn_16x16":
    from .unicorn_16x16 import instance as hat
else:
    raise NameError(f"-blue-sbc: {hat_kind}: hat kind not found.")

logger.info(f"{NAME}: {hat.__class__.__name__}")
