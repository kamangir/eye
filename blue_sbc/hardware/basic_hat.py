import math
import time
from .hardware import Hardware
from abcli import logging
import logging

logger = logging.getLogger(__name__)


class Basic_Hat(Hardware):
    def __init__(self):
        self.switch_pin = -1

        self.green_switch_pin = -1
        self.red_switch_pin = -1
        self.trigger_pin = -1

        self.looper_pin = -1  # red led
        self.incoming_pin = -1  # yellow led
        self.data_pin = -1  # green led
        self.outgoing_pin = -1  # blue led

        self.green_led_pin = -1
        self.red_led_pin = -1

        self.base_led_frequency = 10

        self.pin_history = {}

    def activated(self, pin):
        """
        is pin activated?
        :param pin: pin number
        :return: True / False
        """
        if pin in self.input_pins:
            return self.input(pin) == False

        return False

    def input(self, pin):
        """
        read pin input.
        :param pin: pin number
        :return: True / False
        """
        return True

    @property
    def input_pins(self):
        return [
            pin
            for pin in [
                self.switch_pin,
                self.green_switch_pin,
                self.red_switch_pin,
                self.trigger_pin,
            ]
            if pin != -1
        ]

    def output(self, pin, output):
        """
        set pin to ouput
        :param pin: pin number
        :param output: True / False
        :return: self
        """
        return self

    @property
    def output_pins(self):
        return [
            pin
            for pin in [
                self.looper_pin,
                self.incoming_pin,
                self.data_pin,
                self.outgoing_pin,
                self.green_led_pin,
                self.red_led_pin,
            ]
            if pin != -1
        ]

    def pulse(self, pin=None, frequency=None):
        """
        pulse pin
        :param pin: pin number / "outputs"
        :param frequency: frequency
        :return: self
        """
        if pin == "outputs":
            for index, pin in enumerate(self.output_pins):
                self.pulse(pin, index)

            return self

        if pin is None:
            for pin in self.output_pins:
                self.pulse(pin, frequency)

            return self

        self.pin_history[pin] = (
            not bool(self.pin_history.get(pin, False))
            if frequency is None
            else (lambda x: x - math.floor(x))(
                time.time() * (self.base_led_frequency + frequency)
            )
            >= 0.5
        )

        return self.output(pin, self.pin_history[pin])

    def release(self):
        """
        release self
        :return: self
        """
        return self

    def setup(self, pin, what, pull_up_down=None):
        """
        Set up pin.
        :param pin: pin number
        :param what: "input" / "output"
        :return: self
        """
        return self
