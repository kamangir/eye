import cv2
from .screen import Screen


class Sparkfun_Top_phat(Screen):
    def __init__(self):
        super(Sparkfun_Top_phat, self).__init__()
        self.size = (7, 17)
        self.animated = True

    def show(self, image, session, header, sidebar):
        image = cv2.resize(self.size)

        super().show(image, session, header, sidebar)

        # TODO: show image

        return self
