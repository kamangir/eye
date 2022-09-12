import cv2


class Screen(object):
    def __init__(self):
        self.key_buffer = []
        self.interpolation = cv2.INTER_LINEAR
        self.sign_images = True

    def show(
        self,
        image,
        session=None,
        header=[],
        sidebar=[],
    ):
        return self
