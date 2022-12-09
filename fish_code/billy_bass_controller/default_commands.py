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
    command.local_song_url = f"{base_path}/../_resources/wazzup.wav"
    return command


def peter_griffin_giggle():
    command = FishCommand()
    command.commands = ["LOWER_ON:0", "O:1", "C:1", "O:1", "C:1", "O:1", "C:1", "O:1", "C:1",
                        "O:1", "C:1", "O:1", "C:1", "O:1", "C:1", "O:1", "C:1", "O:1", "C:20"]
    command.local_song_url = f"{base_path}/../_resources/peter_griffin_giggle.wav"
    return command


def minecraft_oof():
    command = FishCommand()
    command.commands = ["LOWER_ON:0", "O:1"]
    command.local_song_url = f"{base_path}/../_resources/minecraft_oof.wav"
    return command


def jingle_bells_chill():
    command = FishCommand()
    command.commands = ["O:0",
                        "LOWER_ON:1", "LOWER_OFF:1", "LOWER_ON:1", "LOWER_OFF:1",
                        "LOWER_ON:1", "LOWER_OFF:1", "LOWER_ON:1", "LOWER_OFF:1",
                        "UPPER_ON:1", "UPPER_OFF:1", "UPPER_ON:1", "UPPER_OFF:1",
                        "UPPER_ON:1", "UPPER_OFF:1", "UPPER_ON:1", "UPPER_OFF:1",

                        "LOWER_ON:1", "LOWER_OFF:0", "UPPER_ON:1", "UPPER_OFF:0",
                        "LOWER_ON:1", "LOWER_OFF:0", "UPPER_ON:1", "UPPER_OFF:0",
                        # "LOWER_ON:1", "LOWER_OFF:0", "UPPER_ON:1", "UPPER_OFF:0",
                        ]
    command.local_song_url = f"{base_path}/../_resources/jingle_bells_chill.wav"
    return command


def down_with_the_sickness():
    command = FishCommand()
    command.commands = [
                        "LOWER_ON:0.75s", "LOWER_OFF:0.75s", "LOWER_ON:0.75s", "LOWER_OFF:0.75s",
                        "LOWER_ON:0.75s", "LOWER_OFF:0.75s", "LOWER_ON:0.75s", "LOWER_OFF:0.75s",
                        "SYNC:@6.5",
                        "UPPER_ON:0.0s", "O:0.25s", "C:0.1s", "O:0.65s", "C:0.1s", "UPPER_OFF:0.5s",   # O WAH AH AH AH
                        "SYNC:@9.5",
                        "UPPER_ON:0.0s", "O:0.2s", "C:0.1s", "O:0.2s", "C:0.1s", "UPPER_OFF:0.5s",  # UH UH
                        "SYNC:@12.0",
                        "UPPER_ON:0.0s", "O:0.2s", "C:0.1s", "O:0.2s", "C:0.1s", "UPPER_OFF:0.5s",  # UH UH
                        "SYNC:@14.5",
                        "UPPER_ON:0.0s", "O:0.2s", "C:0.1s", "O:0.2s", "C:0.1s", "UPPER_OFF:0.5s",  # UH UH
    ]
    command.local_song_url = f"{base_path}/../_resources/down_with_the_sickness.wav"
    return command
