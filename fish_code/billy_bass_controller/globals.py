import os, getmac, platform

AUDIO_START_OFFSET = 0.0
AUDIO_SHORTENING = 0.0

base_path = os.path.dirname(os.path.realpath(__file__))


def _parse_movement_and_duration(command):
    if len(command) == 2:
        command = f"{command[0]}:{command[1]}"
    try:
        use_ms = False
        movement = command.split(":")[0]
        duration_raw = command.split(":")[1]
        if "@" in duration_raw:
            duration_raw = duration_raw.replace("@", "")
            duration = float(duration_raw)
        else:
            if "s" in duration_raw:
                use_ms = True
                duration_raw = duration_raw.replace("s", "")
                duration = float(duration_raw)
            else:
                duration = int(duration_raw)
        return movement, duration, use_ms
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