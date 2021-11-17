# system modules
import time
from unittest.mock import MagicMock

# user defined modules
from motor_controller import MotorController


class FakeMotorController(MotorController):
    INA_1 = MagicMock()
    INA_2 = MagicMock()
    INA_3 = MagicMock()

    _upper_body_on = False
    _lower_body_on = False
    _mouth_on = False

    def __init__(self):
        for pin in [self.INA_1, self.INA_2, self.INA_3]:
            pin.off()

    def turn_on_upper_body(self):
        assert not self._lower_body_on
        self.INA_1.on()
        self._upper_body_on = True

    def turn_off_upper_body(self):
        self.INA_1.off()
        self._upper_body_on = False

    def turn_on_lower_body(self):
        assert not self._upper_body_on
        self.INA_2.on()
        self._lower_body_on = True

    def turn_off_lower_body(self):
        self.INA_2.off()
        self._lower_body_on = False

    def turn_on_mouth(self):
        self.INA_3.on()

    def turn_off_mouth(self):
        self.INA_3.off()



