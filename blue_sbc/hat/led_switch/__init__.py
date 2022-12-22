NAME = "blue_sbc.hat.led_switch"

from abcli.modules import host
from .classes import Led_Switch_Hat, Hat

if host.is_rpi() or host.is_jetson():
    instance = Led_Switch_Hat()
else:
    instance = Hat()
