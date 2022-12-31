import cv2
import time
from blue_sbc.hardware.screen import Screen
import math


class Sparkfun_Top_phat(Screen):
    def __init__(self):
        super(Sparkfun_Top_phat, self).__init__()
        self.size = (7, 17)
        self.animated = False

        import board
        import neopixel

        # https://learn.sparkfun.com/tutorials/sparkfun-top-phat-hookup-guide/ws2812b-leds
        self.pixel_count = 6
        self.pixels = neopixel.NeoPixel(
            board.D12,
            self.pixel_count,
            auto_write=False,
        )

    def pulse(self, pin=None, frequency=None):
        super().pulse(pin, frequency)

        pixel_index = 0
        color = (0, 0, 1)
        if pin == "data":
            pixel_index = 1
            color = (0, 1, 0)
        if pin == "incoming":
            pixel_index = 2
            color = (1, 1, 0)
        if pin == "loop":
            pixel_index = 3
            color = (1, 0, 0)
        if pin == "outputs":
            pixel_index = 4
            color = (0, 1, 1)

        self.pixels[pixel_index] = tuple(int(thing * 64) for thing in color)
        self.pixels.show()

        return self

    def release(self):
        super().release()
        for index in range(self.pixel_count):
            self.pixels[index] = 3 * (0,)
            self.pixels.show()
            time.sleep(0.1)

    def update_screen(self, image, session, header, sidebar):
        image = cv2.resize(image, self.size)

        super().update_screen(image, session, header, sidebar)

        return self
