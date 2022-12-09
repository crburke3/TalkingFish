from .fish_command import FishCommand
from .globals import base_path


def connecting():
    command = FishCommand()
    command.commands = ["LOWER_ON:2", "LOWER_OFF:2", "UPPER_ON:2", "UPPER_OFF:2", "O:2", "LOWER_ON:2", "LOWER_OFF:2",
                        "LOWER_ON:2", "LOWER_OFF:2", "O:2"]
    command.local_song_url = f"{base_path}/../_resources/joke.wav"
    return command


def mac_boot():
    command = FishCommand()
    command.commands = ["LOWER_ON:2", "O:2", "LOWER_OFF:2", "C:2", "UPPER_ON:2", "UPPER_OFF:2", "LOWER_ON:2", "LOWER_OFF:2",
                        "LOWER_ON:2", "LOWER_OFF:2", "O:2"]
    command.local_song_url = f"{base_path}/../_resources/mac_startup_sound.wav"
    return command
