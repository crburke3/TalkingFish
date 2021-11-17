# firmware defined modules
import time, os, sys
sys.path.insert(1, '../')

# user defined modules
from billy_bass_controller import Device
from billy_bass_controller import FishCommand



# device.fc.perform(fake_command)

def run_parallel(*functions):
    '''
    Run functions in parallel
    '''
    from multiprocessing import Process
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()


if __name__ == '__main__':
    device = Device()

    fake_command = FishCommand()
    fake_command.commands = ['C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'O4', 'C2', 'C2', 'O4', 'C2', 'O4',
                             'C2', 'O1',
                             'C2', 'O1', 'C2', 'O4', 'C2', 'O1', 'C2', 'O4', 'C2', 'C2']
    fake_command.song_url = "https://storage.googleapis.com/fish-1-audio-files/joke.wav"
    fake_command.speech_text = "You know where I keep my money? The river bank"
    device.fish_api.download_song_for_object(fake_command)

    device.fc.current_task = fake_command
    device.fc.current_task._expected_prescaler = 0.03

    print("BEGINNING PARALLELISM")
    run_parallel(device.fc._move_to_commands(), device.fc._play_song())