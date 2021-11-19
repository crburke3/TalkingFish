# firmware defined modules
import time, os, sys, pytest
sys.path.insert(1, '../')

# user defined modules
from billy_bass_controller import Device
from billy_bass_controller import FishCommand


def test_failure_1():
    device = Device()
    with pytest.raises(Exception):
        movements = ["LOWER_ON:5", "UPPER_ON:5"]
        device.fc._move_to_commands(movements)


def test_failure_2():
    device = Device()
    with pytest.raises(Exception):
        movements = ["UPPER_ON:5", "LOWER_ON:5"]
        device.fc._move_to_commands(movements)

