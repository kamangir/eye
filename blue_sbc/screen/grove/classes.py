import cv2
from blue_sbc.screen.classes import Screen


class Grove(Screen):
    def __init__(self):
        super(Grove, self).__init__()
        # https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/
        self.size = (64, 128)

    def show(self, image, session=None, header=[], sidebar=[]):
        image_ = cv2.resize(
            image,
            self.size,
        )

        super(Grove, self).show(image_, session, header, sidebar)

        # TODO: show image_

        return self
