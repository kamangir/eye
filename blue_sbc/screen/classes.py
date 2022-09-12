import cv2


class Screen(object):
    def __init__(self):
        self.key_buffer = []
        self.interpolation = cv2.INTER_LINEAR
        self.sign_images = True
        self.size = (16, 16)

    def show(
        self,
        image,
        session=None,
        header=[],
        sidebar=[],
    ):
        return self
