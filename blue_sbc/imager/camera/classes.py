import argparse
import cv2
import numpy as np
import os
from time import sleep
from abcli import file
from abcli.modules import host
from abcli.modules.cookie import cookie
from abcli.plugins import graphics
from abcli import string
from . import NAME
from .constants import *
from blue_sbc.hat import hat
from blue_sbc.imager.classes import Imager
from abcli.logging import crash_report
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Camera(Imager):
    def __init__(self):
        self.device = None
        self.resolution = []

    def capture(
        self,
        close_after=True,
        log=True,
        open_before=True,
    ):
        """capture.

        Args:
            close_after (bool, optional): close camera after capture. Defaults to True.
            log (bool, optional): log. Defaults to True.
            open_before (bool, optional): open the camera before capture. Defaults to True.
            save (bool, optional): save the image. Defaults to True.

        Returns:
            bool: success.
            image: np.ndarray.
        """
        success = False
        image = np.ones((1, 1, 3), dtype=np.uint8) * 127

        if open_before:
            if not self.open():
                return success, image

        if self.device is None:
            return success, image

        if host.is_rpi():
            temp = file.auxiliary("camera", "png")
            try:
                self.device.capture(temp)
                success = True
            except:
                crash_report(f"{NAME}.capture() failed.")

            if success:
                success, image = file.load_image(temp)
        else:
            try:
                success, image = self.device.read()

                if success:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            except:
                crash_report(f"{NAME}.capture() failed.")

        if close_after:
            self.close()

        if success and log:
            logger.info(f"{NAME}.capture(): {string.pretty_shape_of_matrix(image)}")

        return success, image

    # https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/6
    def capture_video(
        self,
        filename,
        length=10,
        preview=True,
        pulse=True,
        resolution=None,
    ):
        """capture video

        Args:
            filename (str): filename.
            length (int): length in seconds. Default to 10.
            preview (bool, optional): show preview. Defaults to True.
            pulse (bool, optional): pulse hat leds. Defaults to True.
            resolution (Any, optional): resolution. Defaults to None.

        Returns:
            bool: success.
        """
        if not host.is_rpi():
            logger.error(f"{NAME}.capture_video() only works on rpi.")
            return False

        if not self.open(resolution=resolution):
            return False

        success = True
        try:
            if preview:
                self.device.start_preview()

            self.device.start_recording(filename)
            if pulse:
                for _ in range(int(10 * length)):
                    hat.pulse("outputs")
                    sleep(0.1)
            else:
                sleep(length)
            self.device.stop_recording()

            if preview:
                self.device.stop_preview()
        except:
            crash_report(f"{NAME}.capture_video()")
            success = False

        if not self.close():
            return False

        if success:
            logger.info(
                "{}.capture_video(): {} -{}-> {}".format(
                    NAME,
                    string.pretty_duration(length),
                    string.pretty_bytes(file.size(filename)),
                    filename,
                )
            )

        return success

    def close(self, log=True):
        """close camera.

        Args:
            log (bool, optional): log. Defaults to True.

        Returns:
            bool: success
        """

        if self.device is None:
            logger.warning(f"{NAME}.close(): device is {self.device}, failed.")
            return False

        success = False
        try:
            if host.is_rpi():
                self.device.close()
            else:
                self.device.release()
            success = True
        except:
            crash_report(f"{NAME}.close() failed")
            return False

        self.device = None

        if log:
            logger.info(f"{NAME}.close().")

        return success

    def get_resolution(self):
        try:
            if host.is_rpi():
                from picamera import PiCamera

                return [value for value in self.device.resolution]
            else:
                return [
                    int(self.device.get(const))
                    for const in [cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FRAME_WIDTH]
                ]
        except:
            crash_report("camera.get_resolution() failed")
            return []

    def open(
        self,
        log=True,
        resolution=None,
    ):
        """open camera.

        Args:
            log (bool, optional): log. Defaults to True.
            resolution (Tuple(int,int), optional): resolution. Defaults to None.

        Returns:
            bool: success.
        """
        try:
            if host.is_rpi():
                from picamera import PiCamera

                self.device = PiCamera()
                self.device.rotation = int(cookie.get("camera.rotation", 0))

                # https://projects.raspberrypi.org/en/projects/getting-started-with-picamera/7
                self.device.resolution = (
                    ((2592, 1944) if cookie.get("camera.hi_res", True) else (728, 600))
                    if resolution is None
                    else resolution
                )
            else:
                self.device = cv2.VideoCapture(0)

                # https://stackoverflow.com/a/31464688
                self.device.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
                self.device.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

            self.resolution = self.get_resolution()

            if log:
                logger.info(f"{NAME}.open({string.pretty_shape(self.resolution)})")

            return True
        except:
            crash_report(f"{NAME}.open: failed.")
            return False
