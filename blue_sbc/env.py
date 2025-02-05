import os
from blue_options.env import load_config, load_env

load_env(__name__)
load_config(__name__)


BLUE_SBC_HARDWARE_KIND = os.getenv(
    "BLUE_SBC_HARDWARE_KIND",
    "",
)

BLUE_SBC_SESSION_IMAGER_CAMERA = os.getenv(
    "BLUE_SBC_SESSION_IMAGER_CAMERA",
    "",
)
