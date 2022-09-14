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

    def release(self):
        super(Unicorn_16x16, self).release()
        logger.info(f"{self.__class__.__name__}.release()")

        import unicornhathd

        unicornhathd.off()

    def show(
        self,
        image,
        session=None,
        header=[],
        sidebar=[],
    ):
        super(Unicorn_16x16, self).show(
            image,
            session,
            header,
            sidebar,
        )
        import unicornhathd

        image_scaled = cv2.resize(image, self.size)
        for x in range(0, 16):
            for y in range(0, 16):
                unicornhathd.set_pixel(
                    x,
                    y,
                    image_scaled[x, y, 0],
                    image_scaled[x, y, 1],
                    image_scaled[x, y, 2],
                )

        unicornhathd.show()

        return self
