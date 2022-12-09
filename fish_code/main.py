# firmware defined modules
import time, threading

# user defined modules
from billy_bass_controller import Device, FishCommand
from billy_bass_controller.globals import get_device_id
from billy_bass_controller.fish_information import FishInformation
import billy_bass_controller.default_commands as default_cmds

if __name__ == '__main__':
    device = Device()
    starting_fish_info = FishInformation(device_id=get_device_id())
    # internet_connected = device.internet_on()
    internet_connected = False
    if not internet_connected:
        print("NOT CONNECTED TO INTERNET")
        device.fc.perform(default_cmds.mac_boot())
        device.fc.perform(default_cmds.merry_christmas())
    else:
        device.fish_api.post_fish_formation(starting_fish_info)
        device.fish_api.post_fish_command(f"{get_device_id()} I am ALIVE")
        device.fc.boot_perforance()
        while True:
            print(f"listening for new messages in collection: {get_device_id()}...")
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
                    command.audio_start_offset = 0.0
                    device.fc.perform(command)
                    time.sleep(1)
                    device.fc.reset()
                else:
                   time.sleep(2)
            except Exception as e:
                print("FATAL EXCEPTION: ", str(e))