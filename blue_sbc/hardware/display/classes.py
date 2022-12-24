import cv2
import numpy as np
from abcli import file
from abcli import fullname
from abcli.modules import host
from abcli.modules.cookie import cookie
from abcli.plugins import graphics
from . import NAME
from blue_sbc.hardware.screen.classes import Screen
from abcli.logging import crash_report
import abcli.logging
import logging

logger = logging.getLogger(__name__)


class Display(Screen):
    def __init__(self):
        super(Display, self).__init__()

        self.canvas = None
        self.notifications = []
        self.canvas_size = (640, 480)

        self.title = fullname()

        self.created = False

    def create(self):
        if self.created:
            return
        self.created = True

        logger.info(f"{NAME}.create()")

        if cookie.get("display.fullscreen", True) and not host.is_mac():
            # https://stackoverflow.com/a/34337534
            cv2.namedWindow(self.title, cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty(
                self.title, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
            )

            self.canvas_size = (
                graphics.screen_width,
                graphics.screen_height,
            )
        else:
            cv2.namedWindow(self.title, cv2.WINDOW_NORMAL)
            cv2.resizeWindow(
                self.title,
                self.canvas_size[0],
                self.canvas_size[1],
            )

    def pressed(self, keys):
        output = bool([key for key in keys if key in self.key_buffer])

        self.key_buffer = [key for key in self.key_buffer if key not in keys]

        return output

    def save(self, filename=""):
        """save self.

        Args:
            filename (str, optional): filename. Defaults to "".

        Returns:
            bool: success.
        """
        if self.canvas is None:
            return ""

        if not filename:
            filename = file.auxiliary("display", "jpg")

        return filename if file.save_image(filename, self.canvas) else ""

    def show(self, image, session=None, header=[], sidebar=[]):
        super(Display, self).show(image, session, header, sidebar)

        self.notifications = self.notifications[-5:]

        self.canvas = np.copy(image)

        if self.sign_images:
            self.canvas = graphics.add_signature(
                self.canvas,
                header=header,
                footer=[" | ".join(host.signature())],
            )

            self.canvas = graphics.add_sidebar(
                self.canvas,
                sidebar,
                self.notifications,
            )

        self.create()

        self.update_gui()

        key = cv2.waitKey(1)
        if key not in [-1, 255]:
            key = chr(key).lower()
            logger.info(f"{NAME}.show(): key: '{key}'")
            self.key_buffer.append(key)

        return self

    def update_gui(self):
        try:
            if len(self.canvas.shape) == 2:
                self.canvas = np.stack(3 * [self.canvas], axis=2)

            cv2.imshow(
                self.title,
                cv2.cvtColor(
                    cv2.resize(
                        self.canvas,
                        dsize=self.canvas_size,
                        interpolation=self.interpolation,
                    ),
                    cv2.COLOR_BGR2RGB,
                ),
            )
        except:
            crash_report(f"{NAME}.update_gui() failed.")
