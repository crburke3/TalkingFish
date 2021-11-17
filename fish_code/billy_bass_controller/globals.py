AUDIO_START_OFFSET = 0.0
AUDIO_SHORTENING = 0.0


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