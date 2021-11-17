# firmware defined modules
import time, os, sys
sys.path.insert(1, '../')

# user defined modules
from billy_bass_controller import Device
from billy_bass_controller import FishCommand

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
fake_command = FishCommand()
fake_command.commands = ['C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'C2', 'O4', 'C2', 'O4', 'C2', 'O1',
                                 'C2', 'O1', 'C2', 'O4', 'C2', 'O1', 'C2', 'O4', 'C2', 'C2']
device.fc.current_task = fake_command
device.fc._move_to_commands()
