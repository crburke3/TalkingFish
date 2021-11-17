
class MotorController:
    # this class acts as an interface to be overwritten by subclasses
    INA_1 = None
    INA_2 = None
    INA_3 = None
    INA_4 = None

    _upper_body_on: bool = False
    _lower_body_on: bool = False
    _mouth_on: bool = False

    def turn_on_upper_body(self):
        print("Upper Body: ON!")
        # raise NotImplementedError()

    def turn_off_upper_body(self):
        raise NotImplementedError()

    def turn_on_lower_body(self):
        raise NotImplementedError()

    def turn_off_lower_body(self):
        raise NotImplementedError()

    def turn_on_mouth(self):
        print("Mouth: OPEN!", end="")

    def turn_off_mouth(self):
        print("   CLOSED!")
