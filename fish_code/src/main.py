# firmware defined modules
import time

# user defined modules
from motor_controller import MotorController

# globals
ACTIVATION_TIME = 1

motor_controller = MotorController()
while True:
    motor_controller.turn_on_upper_body()
    time.sleep(ACTIVATION_TIME)
    motor_controller.turn_off_upper_body()
    time.sleep(ACTIVATION_TIME)
    motor_controller.turn_on_lower_body()
    time.sleep(ACTIVATION_TIME)
    motor_controller.turn_off_lower_body()
    time.sleep(ACTIVATION_TIME)
    motor_controller.turn_on_mouth()
    time.sleep(ACTIVATION_TIME)
    motor_controller.turn_off_mouth()
    time.sleep(ACTIVATION_TIME)
