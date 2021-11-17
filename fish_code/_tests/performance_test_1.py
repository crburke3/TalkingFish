# firmware defined modules
import time

# user defined modules
from device import Device
from fish_command import FishCommand


device = Device()

fake_command = FishCommand()
fake_command.commands = ['C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'C2', 'O4', 'C2', 'O4', 'C2', 'O1',
                                 'C2', 'O1', 'C2', 'O4', 'C2', 'O1', 'C2', 'O4', 'C2', 'C2']
fake_command.song_url = "https://storage.googleapis.com/fish-1-audio-files/joke.wav"
fake_command.speech_text = "You know where I keep my money? The river bank"
fake_command.local_song_url = "/Users/christianburke/PycharmProjects/TalkingFish/fish_code/src/downloads/joke.wav"

device.fc.current_task = fake_command
# device.fc._move_to_commands()
# device.fc._play_song()
device.fc.perform(fake_command)
