# firmware defined modules
import time

# user defined modules
from ..billy_bass_controller.device import Device
from ..billy_bass_controller.fish_command import FishCommand


device = Device()

fake_command = FishCommand()
fake_command.commands = ['C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'C2', 'O4', 'C2', 'O4', 'C2', 'O1',
                                 'C2', 'O1', 'C2', 'O4', 'C2', 'O1', 'C2', 'O4', 'C2', 'C2']
fake_command.song_url = "https://storage.googleapis.com/fish-1-audio-files/joke.wav"
fake_command.speech_text = "You know where I keep my money? The river bank"
device.fish_api.download_song_for_object(fake_command)

device.fc.current_task = fake_command
device.fc.perform(fake_command)
