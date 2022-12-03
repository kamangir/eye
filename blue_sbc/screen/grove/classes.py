import cv2
from blue_sbc.screen.classes import Screen
from grove.grove_button import GroveButton
from abcli import string
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from abcli import logging
import logging

logger = logging.getLogger(__name__)

BUTTON = 24

RST = None  # on the PiOLED this pin isnt used


class Grove_Screen(Screen):
    def __init__(self):
        super(Grove_Screen, self).__init__()
        # https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/
        self.size = (64, 128)

        self.button = GroveButton(BUTTON)
        self.button.on_press = lambda t: grove_button_on_press(self, t)
        self.button.on_release = lambda t: grove_button_on_release(self, t)

        # https://github.com/IcingTomato/Seeed_Python_SSD1315/blob/master/examples/stats.py
        self.display = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        self.display.begin()
        self.display.clear()
        self.display.display()

        self.width = display.width
        self.height = display.height
        self.image = Image.new("1", (self.width, self.height))

        self.draw = ImageDraw.Draw(self.image)

        # Draw a black filled box to clear the image.
        self.draw.rectangle(
            (0, 0, self.width, self.height),
            outline=0,
            fill=0,
        )

        self.padding = -2
        self.top = self.padding
        self.bottom = self.height - self.padding
        x = 0

        self.font = ImageFont.load_default()

    def show(self, image, session=None, header=[], sidebar=[]):
        image_ = cv2.resize(
            image,
            self.size,
        )

        super(Grove_Screen, self).show(image_, session, header, sidebar)

        print(header)

        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.text((x, top), header[0], font=font, fill=255)
        draw.text((x, top + 8), header[1], font=font, fill=255)
        draw.text((x, top + 16), header[2], font=font, fill=255)
        draw.text((x, top + 25), header[3], font=font, fill=255)

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
