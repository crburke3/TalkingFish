# firmware defined modules
import time

# user defined modules
from billy_bass_controller import Device, FishCommand

# globals
device = Device()

if __name__ == '__main__':
    while True:
        try:
            getRequest = device.fish_api.get_next_item_in_queue()
            if getRequest.status_code == 200:
                json_data = getRequest.json()
                command = FishCommand()
                commands_str = json_data['commands']
                commands_str = commands_str.strip('[')
                commands_str = commands_str.strip(']')
                commands_str = commands_str.replace('\'', '')
                commands_str = commands_str.replace(' ', '')
                commands = commands_str.split(',')
                command.commands = commands
                command.song_url = json_data['audio_url']
                device.fish_api.download_song_for_object(command)

                command._expected_prescaler = command.get_expected_prescaler()
                command.audio_start_offset = 0.5
                device.fc.perform(command)
                time.sleep(5)
            else:
               time.sleep(5)
        except Exception as e:
            print("FATAL EXCEPTION: ", str(e))