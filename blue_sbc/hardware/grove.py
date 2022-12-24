import cv2
from .screen import Screen
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24


class Grove(Screen):
    def __init__(self):
        super(Grove, self).__init__()

        from grove.grove_button import GroveButton

        # https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/
        self.size = (64, 128)

        self.button = GroveButton(BUTTON)
        self.button.on_press = lambda t: grove_button_on_press(self, t)
        self.button.on_release = lambda t: grove_button_on_release(self, t)


def grove_button_on_press(screen, t):
    logger.info("grove.button: pressed.")


def grove_button_on_release(screen, t):
    logger.info(f"grove.button: released after {string.pretty_duration(t)}.")

    if t > 60:
        logger.info("long press, ignored.")
        return

    if t > 5:
        key = "s"
    elif t > 3:
        key = "u"
    else:
        key = " "

    screen.key_buffer.append(key)
    logger.info(f"{screen.__class__.__name__}: '{key}'")
