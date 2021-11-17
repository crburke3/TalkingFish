# firmware defined modules
import time, os, sys
sys.path.insert(1, '../')

# user defined modules
from billy_bass_controller import Device

device = Device()

# make sure shit is working
device.mc.turn_on_mouth()
time.sleep(1)
device.mc.turn_off_mouth()
time.sleep(1)
device.mc.turn_on_upper_body()
time.sleep(1)
device.mc.turn_off_upper_body()
time.sleep(1)
device.mc.turn_on_lower_body()
time.sleep(1)
device.mc.turn_off_lower_body()
time.sleep(1)


# try and run a series of commands
