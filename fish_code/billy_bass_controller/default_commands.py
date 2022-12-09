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
    command.commands = ["O:0", "UPPER_ON:1"]
    command.local_song_url = f"{base_path}/../_resources/mac_startup_sound.wav"
    return command

def merry_christmas():
    command = FishCommand()
    command.commands = ["UPPER_ON:0", "O:1", "C:1",  "O:1", "C:1", "O:1", "C:1", "O:1", "C:1",
                        "UPPER_OFF:0",  "LOWER_ON:0", "O:3", "C:1", "O:3", "LOWER_OFF:0", "UPPER_ON:1", "C:1", "O:3", "C:1"]
    command.local_song_url = f"{base_path}/../_resources/merry_christmas.wav"
    return command

def wazzup_scary_movie():
    command = FishCommand()
    command.commands = ["UPPER_ON:0", "O:3", "C:1",  "O:0",
                        "UPPER_OFF:0",  "LOWER_ON:5",  "LOWER_OFF:2", "LOWER_ON:5",  "LOWER_OFF:2"]
    command.local_song_url = f"{base_path}/../_resources/merry_christmas.wav"
    return command