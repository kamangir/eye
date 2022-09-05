from abcli.modules.cookie import cookie
import abcli.logging
import logging

logger = logging.getLogger(__name__)

NAME = "blue_sbc.screen"

# screen_name = cookie.get("session.screen", "display")
# if screen_name == "display":
from .display import instance as screen

logger.info(f"{NAME}: screen: {screen.__class__.__name__}")
