from .motor_controller import MotorController
from .fish_controller import FishController
from .audio_driver import AudioDriver
from .fish_api import FishAPI
from uuid import getnode
import os
import getmac


class Device:

    def __init__(self):
        self.mc: MotorController
        self.ad: AudioDriver
        self.fc: FishController
        self.fish_api: FishAPI
        self._initalize_motor_controller()
        self._initalize_audio_driver()
        self._initalize_fish_controller()
        self._initalize_fish_api()

    def _initalize_motor_controller(self):
        try:
            from .ports.esp_based_micropython.esp32_motor_controller import ESP32MotorController
            self.mc = ESP32MotorController()
            print("Motor Controller Device Identified: ESP32")
            return
        except:
            pass
        try:
            from .ports.raspberry_pi.raspberry_pi_motor_controller import RPIMotorController
            self.mc = RPIMotorController()
            print("Motor Controller Device Identified: Raspberry PI")
            return
        except:
            pass
        try:
            from .ports.mac.mac_motor_controller import FakeMotorController
            self.mc = FakeMotorController()
            print("Motor Controller Device Identified: Local Computer")
            return
        except:
            raise Exception("Motor Controller Device Not Recognized!")

    def _initalize_audio_driver(self):
        self.ad = AudioDriver()

    def _initalize_fish_controller(self):
        self.fc = FishController(self.mc, self.ad)

    def _initalize_fish_api(self):
        self.fish_api = FishAPI()

    def get_unique_id(self) -> str:
        mac_raw = getnode()
        return ':'.join(("%012X" % mac_raw)[i:i+2] for i in range(0, 12, 2))

    @staticmethod
    def get_device_id() -> str:
        try:
            mac = getmac.get_mac_address()
            assert mac is not None
            return mac
        except Exception as e:
            print("Failed to get mac: ", e)
            return "DEFAULT_DEVICE_ID"
