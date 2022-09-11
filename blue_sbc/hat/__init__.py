NAME = "blue_sbc.hat"

from abcli.modules import host
from .classes import *


instance = (
    RPi_Led_Switch_Hat()
    if host.is_rpi()
    else Jetson_Led_Switch_Hat()
    if host.is_jetson()
    else Hat()
)
