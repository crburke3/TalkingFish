# firmware defined modules
import time, threading

# user defined modules
from billy_bass_controller import Device, FishCommand
from billy_bass_controller.globals import get_device_id
from billy_bass_controller.fish_information import FishInformation
import billy_bass_controller.default_commands as default_cmds
from datetime import datetime

if __name__ == '__main__':
    device = Device()
    starting_fish_info = FishInformation(device_id=get_device_id())
    while True:
        button_pressed = device.button_1_pressed()
        print(f"PRESSED: {button_pressed}")
        time.sleep(0.1)

    device.fc.perform(default_cmds.mac_boot())
    internet_attempts = 2
    internet_connected = False
    internet_connection_performance = default_cmds.peter_griffin_giggle()
    while not internet_connected and internet_attempts > 0:
        device.fc.perform(internet_connection_performance)
        # internet_connected = device.internet_on()
        internet_connected = False
        internet_attempts -= 1
        time.sleep(1)

    if not internet_connected:
        print("NOT CONNECTED TO INTERNET")
        device.fc.perform(default_cmds.minecraft_oof())
        offline_performances = [
            default_cmds.jingle_bells_chill(),
            default_cmds.down_with_the_sickness(),
            default_cmds.look_at_me_now(),
            default_cmds.merry_christmas(),
        ]
        button_counter = len(offline_performances) - 1
        last_press = None
        button_ever_pressed = False
        while True:
            button_pressed = device.button_1_pressed()
            if button_pressed:
                print("button pressed!")
                button_ever_pressed = True
            if button_pressed or last_press == None:
                last_press = datetime.now()
                if button_counter < 0:
                    button_counter = len(offline_performances) - 1
                performance_for_press = offline_performances[button_counter]
                device.fc.perform(performance_for_press)
                button_counter -= 1
            time.sleep(1)
            secs_since_last_press = (datetime.now() - last_press).total_seconds()
            print(f"It has been {round(secs_since_last_press)}s since you last pressed the button")
            if not button_ever_pressed:
                if secs_since_last_press >= 20:
                    last_press = None
    else:
        device.fc.perform(default_cmds.wazzup_scary_movie())
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