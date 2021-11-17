# system modules
import time
from threading import Thread

# user defined modules
from .motor_controller import MotorController
from .fish_command import FishCommand
from .audio_driver import AudioDriver


class FishController:

    def __init__(self, motor_controller: MotorController, audio_driver: AudioDriver):
        self.mc = motor_controller
        self.ad = audio_driver
        self.current_task: FishCommand

    def perform(self, database_object: FishCommand):
        print("performing!")
        print("Expected movement duration (units): ", database_object.command_unit_length())
        print("Expected song duration (s): ", database_object.song_length_seconds())
        database_object.validate()
        self.current_task = database_object
        movement_thread = Thread(target=self._move_to_commands)
        song_thread = Thread(target=self._play_song)
        threads = [movement_thread, song_thread]
        # begin performance
        for thread in threads:
            thread.start()
        # Wait for all of them to finish
        time.sleep(3)
        for x in threads:
            x.join()
        print("threads finished!")

    def _move_to_commands(self):
        print("moving to commands: ", self.current_task.commands)
        for cmd in self.current_task.commands:
            if ("C" in cmd) or ("O" in cmd):
                self._handle_mouth_movement(cmd)
            else:
                print("Cannot move to cmd: ", cmd, flush=True)

    def _play_song(self):
        print("playgin song...", flush=True)
        self.ad.play_wav_file(self.current_task.local_song_url)

    def _handle_mouth_movement(self, command: str):
        movement = command[0]
        duration = int(command[1])
        if movement == "C":
            self.mc.turn_off_mouth()
        if movement == "O":
            self.mc.turn_on_mouth()
        self.sleep_for_units(duration)

    def sleep_for_units(self, units):
        prescaler = self.current_task.get_expected_prescaler()
        time.sleep(units * prescaler)



