# firmware defined modules
import time

# user defined modules
from device import Device

# globals
device = Device()

ACTIVATION_TIME = 1

while True:
    device.mc.turn_on_upper_body()
    time.sleep(ACTIVATION_TIME)
    device.mc.turn_off_upper_body()
    time.sleep(ACTIVATION_TIME)
    device.mc.turn_on_lower_body()
    time.sleep(ACTIVATION_TIME)
    device.mc.turn_off_lower_body()
    time.sleep(ACTIVATION_TIME)
    device.mc.turn_on_mouth()
    time.sleep(ACTIVATION_TIME)
    device.mc.turn_off_mouth()
    time.sleep(ACTIVATION_TIME)
