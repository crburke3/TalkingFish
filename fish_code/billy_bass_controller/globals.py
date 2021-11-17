AUDIO_START_OFFSET = 0.0
AUDIO_SHORTENING = 0.0


def _parse_movement_and_duration(command):
    movement = command.split(":")[0]
    duration = int(command.split(":")[1])
    return movement, duration