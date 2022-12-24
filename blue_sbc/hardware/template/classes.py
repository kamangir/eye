import cv2
from blue_sbc.hardware.screen.classes import Screen


class Template(Screen):
    def __init__(self):
        super(Template, self).__init__()
        self.size = (7, 17)
        self.animated = True

    def show(self, image, session=None, header=[], sidebar=[]):
        image_ = cv2.resize(
            self.size,
        )

        super(Template, self).show(image_, session, header, sidebar)

        # TODO: show image_

        return self
