import machine

INA_1 = machine.Pin(13, machine.Pin.OUT)  # Pin D0 on board, green wire
INA_2 = machine.Pin(12, machine.Pin.OUT)  # Pin D1 on board, blue wire
INA_3 = machine.Pin(27, machine.Pin.OUT)  # Pin D2 on board, brown wire
INA_4 = machine.Pin(33, machine.Pin.OUT)  # Pin D2 on board, NOT USED

for pin in [INA_1, INA_2, INA_3, INA_4]:
    pin.off()  # turn off all pins on import

class MotorController:

    _upper_body_on = False
    _lower_body_on = False
    _mouth_on = False

    def turn_on_upper_body(self):
        assert not self._lower_body_on
        INA_1.on()
        self._upper_body_on = True

    def turn_off_upper_body(self):
        INA_1.off()
        self._upper_body_on = False

    def turn_on_lower_body(self):
        assert not self._upper_body_on
        INA_2.on()
        self._lower_body_on = True

    def turn_off_lower_body(self):
        INA_2.off()
        self._lower_body_on = False

    def turn_on_mouth(self):
        INA_3.on()
        INA_4.off()

    def turn_off_mouth(self):
        INA_3.off()
        INA_4.off()



