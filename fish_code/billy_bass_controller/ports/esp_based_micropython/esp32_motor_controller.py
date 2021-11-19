import machine

from billy_bass_controller import MotorController


class ESP32MotorController(MotorController):
    INA_1 = machine.Pin(13, machine.Pin.OUT)  # Pin D0 on board, green wire
    INA_2 = machine.Pin(12, machine.Pin.OUT)  # Pin D1 on board, blue wire
    INA_3 = machine.Pin(27, machine.Pin.OUT)  # Pin D2 on board, brown wire

    upper_body_on = False
    lower_body_on = False
    mouth_on = False

    def __init__(self):
        for pin in [self.INA_1, self.INA_2, self.INA_3]:
            pin.off()  # turn off all pins on import

    def turn_on_upper_body(self):
        assert not self.lower_body_on
        self.INA_1.on()
        self.upper_body_on = True

    def turn_off_upper_body(self):
        self.INA_1.off()
        self.upper_body_on = False

    def turn_on_lower_body(self):
        assert not self.upper_body_on
        self.INA_2.on()
        self.lower_body_on = True

    def turn_off_lower_body(self):
        self.INA_2.off()
        self.lower_body_on = False

    def turn_on_mouth(self):
        self.INA_3.on()

    def turn_off_mouth(self):
        self.INA_3.off()



