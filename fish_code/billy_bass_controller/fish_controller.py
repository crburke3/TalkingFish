# system modules
import time
from datetime import datetime
from multiprocessing import Pool


# user defined modules
from .motor_controller import MotorController
from .fish_command import FishCommand
from .audio_driver import AudioDriver
from .globals import AUDIO_START_OFFSET



class FishController:

    def __init__(self, motor_controller: MotorController, audio_driver: AudioDriver):
        self.mc = motor_controller
        self.ad = audio_driver
        self.current_task: FishCommand

    def perform(self, database_object: FishCommand):
        print("Expected movement duration (units): ", database_object.command_unit_length())
        print("Unit Duration (s): ", database_object.get_expected_prescaler())
        print("Expected movement duration (s): ", database_object.command_unit_length() * database_object.get_expected_prescaler())
        print("Expected song duration (s): ", database_object.song_length_seconds())
        print("")
        print("performing!")

        database_object.validate()
        self.current_task = database_object

        print("BEGINNING PARALLELISM")
        from multiprocessing import Process
        p1 = Process(target=self._play_song)
        p1.start()
        p2 = Process(target=self._move_to_commands)
        p2.start()
        # run in sync


        print("threads finished!")

    def _move_to_commands(self):
        start_time = datetime.now().timestamp()
        time.sleep(AUDIO_START_OFFSET)
        print("moving to commands: ", self.current_task.commands)
        for cmd in self.current_task.commands:
            if ("C" in cmd) or ("O" in cmd):
                self._handle_mouth_movement(cmd)
            else:
                print("Cannot move to cmd: ", cmd, flush=True)
        diff = datetime.now().timestamp() - start_time
        print(f"it took {diff}s  to move")

    def _play_song(self):
        print("playgin song...", flush=True)
        self.ad.play_wav_file(self.current_task.local_song_url)

    def _handle_mouth_movement(self, command: str):
        print("Executing command: ", command)
        movement = command[0]
        duration = int(command[1])
        if movement == "C":
            self.mc.turn_off_mouth()
        if movement == "O":
            self.mc.turn_on_mouth()
        self.sleep_for_units(duration)

    def sleep_for_units(self, units):
        prescaler = self.current_task.get_expected_prescaler()
        sleep_time = units * prescaler
        print("sleeping for (s): ", sleep_time)
        time.sleep(sleep_time)



