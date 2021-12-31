import os, getmac, platform

AUDIO_START_OFFSET = 0.0
AUDIO_SHORTENING = 0.0

base_path = os.path.dirname(os.path.realpath(__file__))


def _parse_movement_and_duration(command):
    if len(command) == 2:
        command = f"{command[0]}:{command[1]}"
    try:
        movement = command.split(":")[0]
        duration = int(command.split(":")[1])
        return movement, duration
    except Exception as e:
        print("Failed to parse command: ", command)
        raise e

def get_device_id() -> str:
    if "mac" in platform.platform():
        return "computer"
    try:
        mac = getmac.get_mac_address()
        assert mac is not None
        return mac
    except Exception as e:
        print("Failed to get mac: ", e)
        return "DEFAULT_DEVICE_ID"