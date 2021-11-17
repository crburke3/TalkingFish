# system modules
import time
from datetime import datetime
from multiprocessing import Pool


# user defined modules
from .motor_controller import MotorController
from .fish_command import FishCommand
from .audio_driver import AudioDriver
from .globals import AUDIO_START_OFFSET, _parse_movement_and_duration

MOUTH_OPEN_CMD = "O"
MOUTH_CLOSED_CMD = "C"
UPPER_BODY_ON_CMD = "UPPER_ON"
UPPER_BODY_OFF_CMD = "UPPER_OFF"
LOWER_BODY_ON_CMD = "LOWER_ON"
LOWER_BODY_OFF_CMD = "LOWER_OFF"


class FishController:

    def __init__(self, motor_controller: MotorController, audio_driver: AudioDriver):
        self.mc = motor_controller
        self.ad = audio_driver
        self.current_task: FishCommand

    def happy_dance(self):
        # defualts to a time of 0.25s
        movements = ["LOWER_ON:2", "LOWER_OFF:2", "UPPER_ON:2", "UPPER_OFF:2", "O:2", "LOWER_ON:2", "LOWER_OFF:2",
                    "LOWER_ON:2", "LOWER_OFF:2", "C:2"]
        command = FishCommand()
        command.commands = movements
        self.perform(command)

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
        p1.join()
        p2.join()
        print("threads finished!")




    def _move_to_commands(self):
        time.sleep(self.current_task.audio_start_offset)
        start_time = datetime.now().timestamp()
        print("moving to commands: ", self.current_task.commands)
        for cmd in self.current_task.commands:
            cmd_action = cmd.split(":")[0]
            if cmd_action in [MOUTH_OPEN_CMD, MOUTH_CLOSED_CMD]:
                self._handle_mouth_movement(cmd)
            elif cmd_action in [UPPER_BODY_ON_CMD, UPPER_BODY_OFF_CMD]:
                self._handle_upper_body_movement(cmd)
            elif cmd_action in [LOWER_BODY_ON_CMD, LOWER_BODY_OFF_CMD]:
                self._handle_upper_body_movement(cmd)
            else:
                print("Cannot move to cmd: ", cmd, flush=True)
        diff = datetime.now().timestamp() - start_time
        print(f"it took {diff}s  to move")

    def _play_song(self):
        if not self.current_task.local_song_url:
            print("No song to play!")
            return
        print("playgin song...", flush=True)
        self.ad.play_wav_file(self.current_task.local_song_url)

    def _handle_mouth_movement(self, command: str):
        print("Executing command: ", command)
        movement, duration = _parse_movement_and_duration(command)
        if movement == MOUTH_CLOSED_CMD:
            self.mc.turn_off_mouth()
        if movement == MOUTH_OPEN_CMD:
            self.mc.turn_on_mouth()
        self._sleep_for_units(duration)

    def _handle_upper_body_movement(self, command: str):
        print("Executing command: ", command)
        movement, duration = _parse_movement_and_duration(command)
        if movement == UPPER_BODY_ON_CMD:
            self.mc.turn_on_upper_body()
        if movement == UPPER_BODY_OFF_CMD:
            self.mc.turn_off_upper_body()
        self._sleep_for_units(duration)

    def _handle_lower_body_movement(self, command: str):
        print("Executing command: ", command)
        movement, duration = _parse_movement_and_duration(command)
        if movement == LOWER_BODY_ON_CMD:
            self.mc.turn_on_lower_body()
        if movement == LOWER_BODY_OFF_CMD:
            self.mc.turn_off_lower_body()
        self._sleep_for_units(duration)

    def _sleep_for_units(self, units):
        prescaler = self.current_task.get_expected_prescaler()
        sleep_time = units * prescaler
        print("sleeping for (s): ", sleep_time)
        time.sleep(sleep_time)




