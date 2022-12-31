import cv2
import time
from blue_sbc.hardware.screen import Screen
from matplotlib import cm


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

        self.intensity = 48

        # https://matplotlib.org/stable/tutorials/colors/colormaps.html
        self.colormap = cm.get_cmap("copper", self.pixel_count)(range(self.pixel_count))

        self.pulse_cycle = 0

    def pulse(self, pin=None, frequency=None):
        super().pulse(pin, frequency)

        for index in range(self.pixel_count):
            self.pixels[index] = tuple(
                int(thing * self.intensity)
                for thing in self.colormap[
                    (index + int(self.pulse_cycle / 10)) % self.pixel_count
                ][:3]
            )

        self.pixels.show()

        self.pulse_cycle += 1

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
