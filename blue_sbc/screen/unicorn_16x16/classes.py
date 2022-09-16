import cv2
import time
from blue_sbc.screen.classes import Screen
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Unicorn_16x16(Screen):
    def __init__(self):
        super(Unicorn_16x16, self).__init__()
        self.size = (16, 16)
        self.animated = True

    def release(self):
        super(Unicorn_16x16, self).release()
        logger.info(f"{self.__class__.__name__}.release()")

        import unicornhathd

        unicornhathd.off()

    def show(self, image, session=None, header=[], sidebar=[]):
        import unicornhathd

        image_ = cv2.rotate(
            cv2.resize(
                image,
                self.size,
            ),
            cv2.ROTATE_90_CLOCKWISE,
        )

        super(Unicorn_16x16, self).show(image_, session, header, sidebar)

        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(
                    x,
                    y,
                    image_[x, y, 0],
                    image_[x, y, 1],
                    image_[x, y, 2],
                )

        unicornhathd.show()

        return self
