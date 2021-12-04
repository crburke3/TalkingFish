
# firmware defined modules
import time, os, sys
sys.path.insert(1, '../../')

# user defined modules
from ..device import Device
from ..fish_command import FishCommand



# device.fc.perform(fake_command)


if __name__ == '__main__':
    device = Device()
    device.fc.happy_dance()
