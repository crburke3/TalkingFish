# system modules
from gpiozero import LED
import time

# user defined modules
from billy_bass_controller import MotorController


class RPIMotorController(MotorController):
    INA_1 = LED(14)
    INA_2 = LED(15)
    INA_3 = LED(18)

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



