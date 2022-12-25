from blue_sbc.hardware.hat.abstract import Abstract_Hat
from abcli.modules import host
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Prototype_Hat(Abstract_Hat):
    def __init__(self):
        super(Prototype_Hat, self).__init__()

        self.is_rpi = host.is_rpi()

        if self.is_rpi:
            import RPi.GPIO as GPIO

            self.switch_pin = 12

            self.green_switch_pin = 16
            self.red_switch_pin = 13

            self.looper_pin = 22  # red led
            self.incoming_pin = 18  # yellow led
            self.data_pin = 36  # green led
            self.outgoing_pin = 40  # blue led

            self.green_led_pin = 15
            self.red_led_pin = 7

            GPIO.setmode(GPIO.BOARD)  # numbers GPIOs by physical location
        else:
            import Jetson.GPIO as GPIO

            self.switch_pin = 7

            self.trigger_pin = 12
            self.looper_pin = 29  # red led
            self.incoming_pin = 31  # yellow led
            self.data_pin = 32  # green led
            self.outgoing_pin = 33  # blue led

            GPIO.setmode(GPIO.BOARD)  # numbers GPIOs by physical location

        # http://razzpisampler.oreilly.com/ch07.html
        for pin in self.input_pins:
            self.setup(pin, "input", GPIO.PUD_UP)

        for pin in self.output_pins:
            self.setup(pin, "output")
            self.output(pin, False)

    def input(self, pin):
        if pin == -1:
            return True

        if self.is_rpi:
            import RPi.GPIO as GPIO
        else:
            import Jetson.GPIO as GPIO

        return GPIO.input(pin) == GPIO.HIGH

    def output(self, pin, output):
        if pin == -1:
            return self

        if self.is_rpi:
            import RPi.GPIO as GPIO
        else:
            import Jetson.GPIO as GPIO

        GPIO.output(pin, GPIO.HIGH if output else GPIO.LOW)
        return self

    def release(self):
        if self.is_rpi:
            import RPi.GPIO as GPIO
        else:
            import Jetson.GPIO as GPIO
        logger.info(f"{self.__class__.__name__}.release()")

        GPIO.cleanup()

        return self

    def setup(self, pin, what, pull_up_down=None):
        if pin == -1:
            return self

        if self.is_rpi:
            import RPi.GPIO as GPIO
        else:
            import Jetson.GPIO as GPIO

        if what == "output":
            what = GPIO.OUT
        elif what == "input":
            what = GPIO.IN
        else:
            raise NameError(
                f"{self.__class__.__name__}.setup({pin}): unknown what: {what}."
            )

        if pull_up_down is None:
            GPIO.setup(pin, what)
        else:
            GPIO.setup(pin, what, pull_up_down=pull_up_down)

        return self
