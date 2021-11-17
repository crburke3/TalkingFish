
# firmware defined modules
import time, os, sys
sys.path.insert(1, '../')

# user defined modules
from billy_bass_controller import Device
from billy_bass_controller import FishCommand



# device.fc.perform(fake_command)


if __name__ == '__main__':
    device = Device()
    device.fc.happy_dance()
