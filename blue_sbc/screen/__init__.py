from abcli.modules.cookie import cookie
from abcli.modules import host
from .classes import Screen
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.screen"

hat_kind = cookie.get("hat.kind", "other")
if hat_kind == "adafruit_rgb_matrix":
    from .adafruit_rgb_matrix import instance as screen
elif hat_kind == "scroll_phat_hd":
    from .scroll_phat_hd import instance as screen
elif hat_kind == "template":
    from .template import instance as screen
elif hat_kind == "unicorn_16x16":
    from .unicorn_16x16 import instance as screen
elif hat_kind == "grove":
    from .grove import instance as screen
elif hat_kind == "sparkfun-top-phat":
    from .sparkfun_top_phat import instance as screen
elif host.is_headless():
    screen = Screen()
else:
    from .display import instance as screen

logger.info(f"{NAME}: screen: {screen.__class__.__name__}")
