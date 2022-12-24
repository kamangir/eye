NAME = "blue_sbc.hardware.led_switch"

from abcli.modules import host
from .classes import Led_Switch_Hat, Hardware

if host.is_rpi() or host.is_jetson():
    instance = Led_Switch_Hat()
else:
    instance = Hardware()
