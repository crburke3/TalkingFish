# firmware defined modules
import time

# user defined modules
from motor_controller import MotorController

# globals
mc: MotorController
try:
    from esp_based_micropython.esp32_motor_controller import ESP32MotorController
    mc = ESP32MotorController()
except:
    from raspberry_pi.raspberry_pi_motor_controller import RPIMotorController
    mc = RPIMotorController()


ACTIVATION_TIME = 1

while True:
    mc.turn_on_upper_body()
    time.sleep(ACTIVATION_TIME)
    mc.turn_off_upper_body()
    time.sleep(ACTIVATION_TIME)
    mc.turn_on_lower_body()
    time.sleep(ACTIVATION_TIME)
    mc.turn_off_lower_body()
    time.sleep(ACTIVATION_TIME)
    mc.turn_on_mouth()
    time.sleep(ACTIVATION_TIME)
    mc.turn_off_mouth()
    time.sleep(ACTIVATION_TIME)
