# firmware defined modules
import time, os, sys
sys.path.insert(1, '../../')

# user defined modules
from ..device import Device
from ..fish_command import FishCommand



# device.fc.perform(fake_command)


if __name__ == '__main__':
    device = Device()

    fake_command = FishCommand()
    fake_command.commands = ['O:4', 'C:2', 'C:2', 'O:4', 'C:2', 'O:1', 'O:4', 'C:2', 'O:4', 'C:2', 'O:4', 'C:2', 'O:3', 'C:2', 'C:2', 'O:1', 'C:2', 'C:2', 'O:4', 'C:2', 'C:2', 'C:2', 'O:1', 'C:2', 'O:4', 'C:2', 'O:1']
    fake_command.song_url = "https://storage.googleapis.com/fish-1-audio-files/audio_1637294327.mp3"
    fake_command.speech_text = "You know where I keep my money? The river bank"
    device.fish_api.download_song_for_object(fake_command)

    fake_command._expected_prescaler = 0.04789855072463768
    # fake_command.audio_start_offset = 0.5
    device.fc.perform(fake_command)
