import cv2
from blue_sbc.screen.classes import Screen
from grove.grove_button import GroveButton
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24


class Grove(Screen):
    def __init__(self):
        super(Grove, self).__init__()
        # https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/
        self.size = (64, 128)

        self.button = GroveButton(BUTTON)
        self.button.on_press = grove_button_on_press
        self.button.on_release = grove_button_on_release
        logger.info(f"grove.button: {self.button.pin}")

    def show(self, image, session=None, header=[], sidebar=[]):
        image_ = cv2.resize(
            image,
            self.size,
        )

        print("----show-----")

        super(Grove, self).show(image_, session, header, sidebar)

        # TODO: show image_

        return self


def grove_button_on_press(t):
    logger.info("grove.button: pressed.")


def grove_button_on_release(t):
    logger.info("grove.button: released after {0} seconds.".format(round(t, 6)))
