import cv2
from blue_sbc.screen.classes import Screen
from grove.grove_button import GroveButton
from abcli import string
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24


class Grove_Screen(Screen):
    def __init__(self):
        super(Grove_Screen, self).__init__()
        # https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/
        self.size = (64, 128)

        self.button = GroveButton(BUTTON)
        self.button.on_press = lambda t: grove_button_on_press(self, t)
        self.button.on_release = lambda t: grove_button_on_release(self, t)

    def show(self, image, session=None, header=[], sidebar=[]):
        image_ = cv2.resize(
            image,
            self.size,
        )

        super(Grove_Screen, self).show(image_, session, header, sidebar)

        print(header)

        return self


def grove_button_on_press(screen, t):
    logger.info("grove.button: pressed.")


def grove_button_on_release(screen, t):
    logger.info(f"grove.button: released after {string.pretty_duration(t)}.")

    if t > 10:
        key = "s"
    elif t > 3:
        key = "u"
    else:
        key = " "

    screen.key_buffer.append(key)
    logger.info(f"{screen.__class__.__name__}: '{key}'")
