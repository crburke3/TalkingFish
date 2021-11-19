# firmware defined modules
import time

# user defined modules
from billy_bass_controller import Device
from billy_bass_controller import FishCommand

# globals
device = Device()

if __name__ == '__main__':
    exit(0)
    while True:
        try:
            fake_command = FishCommand()
            fake_command.commands = ['C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'C2', 'O4', 'C2', 'O4',
                                     'C2', 'O1',
                                     'C2', 'O1', 'C2', 'O4', 'C2', 'O1', 'C2', 'O4', 'C2', 'C2']
            fake_command.song_url = "https://storage.googleapis.com/fish-1-audio-files/joke.wav"
            fake_command.speech_text = "You know where I keep my money? The river bank"
            device.fish_api.download_song_for_object(fake_command)

            fake_command._expected_prescaler = 0.04789855072463768
            fake_command.audio_start_offset = 0.5
            device.fc.perform(fake_command)
            time.sleep(5)
            device.fc.happy_dance()
            time.sleep(5)
        except Exception as e:
            print("FATAL EXCEPTION: ", str(e))