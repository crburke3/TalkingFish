# system modules
from gpiozero import LED
import time
import time

# user defined modules
from billy_bass_controller import MotorController


class RPIMotorController(MotorController):
    INA_1 = LED(14)
    INA_2 = LED(15)
    INA_3 = LED(17)

    upper_body_on = False
    lower_body_on = False
    mouth_on = False

    def __init__(self):
        for pin in [self.INA_1, self.INA_2, self.INA_3]:
            print("Turning off pin: ", pin.pin)
            pin.off()

    def turn_on_upper_body(self):
        start_time = time.time()
        assert not self.lower_body_on
        self.INA_1.on()
        self.upper_body_on = True
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn ON upper body")

    def turn_off_upper_body(self):
        start_time = time.time()
        self.INA_1.off()
        self.upper_body_on = False
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn OFF upper body")

    def turn_on_lower_body(self):
        start_time = time.time()
        assert not self.upper_body_on
        self.INA_2.on()
        self.lower_body_on = True
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn ON lower body")

    def turn_off_lower_body(self):
        start_time = time.time()
        self.INA_2.off()
        self.lower_body_on = False
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn OFF lower body")

    def turn_on_mouth(self):
        start_time = time.time()
        self.INA_3.on()
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn ON mouth")

    def turn_off_mouth(self):
        start_time = time.time()
        self.INA_3.off()
        execution_time = time.time() - start_time
        print(f"it took {execution_time}ms to turn off mouth")


