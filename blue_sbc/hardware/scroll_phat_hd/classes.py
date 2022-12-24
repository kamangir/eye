import cv2
import time
from blue_sbc.hardware.screen.classes import Screen


class Scroll_Phat_HD(Screen):
    def __init__(self):
        super(Scroll_Phat_HD, self).__init__()
        self.size = (7, 17)
        self.animated = True

    def show(self, image, session=None, header=[], sidebar=[]):
        import scrollphathd

        image_ = cv2.resize(
            image,
            self.size,
        )

        super(Scroll_Phat_HD, self).show(image_, session, header, sidebar)

        image_ = cv2.cvtColor(
            image_,
            cv2.COLOR_BGR2GRAY,
        )

        for y in range(0, 17):
            for x in range(0, 7):
                scrollphathd.set_pixel(y, x, image_[y, x] / 255.0)

        time.sleep(0.01)
        scrollphathd.show()

        return self
