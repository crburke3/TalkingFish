from motor_controller import MotorController
from fish_controller import FishController
from audio_driver import AudioDriver


class Device:

    def __init__(self):
        self.mc: MotorController
        self.ad: AudioDriver
        self.fc: FishController
        self._initalize_motor_controller()
        self._initalize_audio_driver()
        self._initalize_fish_controller()

    def _initalize_motor_controller(self):
        try:
            from ports.esp_based_micropython.esp32_motor_controller import ESP32MotorController
            self.mc = ESP32MotorController()
            print("Motor Controller Device Identified: ESP32")
        except:
            pass
        try:
            from ports.raspberry_pi.raspberry_pi_motor_controller import RPIMotorController
            self.mc = RPIMotorController()
            print("Motor Controller Device Identified: Raspberry PI")
        except:
            pass
        try:
            from ports.mac.mac_motor_controller import FakeMotorController
            self.mc = FakeMotorController()
            print("Motor Controller Device Identified: Local Computer")
        except:
            raise Exception("Motor Controller Device Not Recognized!")

    def _initalize_audio_driver(self):
        self.ad = AudioDriver()

    def _initalize_fish_controller(self):
        self.fc = FishController(self.mc, self.ad)
