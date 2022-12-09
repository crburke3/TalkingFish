from .motor_controller import MotorController
from .fish_controller import FishController
from .audio_driver import AudioDriver
from .fish_api import FishAPI
from uuid import getnode
import requests
import os
from enum import Enum

RPI_BUTTON_PIN = 21


class DeviceType(Enum):
    raspberry_pi = "raspberry_pi"
    computer = "computer"


class Device:

    def __init__(self):
        self.mc: MotorController
        self.ad: AudioDriver
        self.fc: FishController
        self.fish_api: FishAPI
        self.device_type = None
        self._initalize_motor_controller()  # finds device type
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
            self.device_type = DeviceType.raspberry_pi
            self._setup_rpi_button()
            return
        except:
            pass
        try:
            from .ports.mac.mac_motor_controller import FakeMotorController
            self.mc = FakeMotorController()
            print("Motor Controller Device Identified: Local Computer")
            self.device_type = DeviceType.computer
            return
        except:
            raise Exception("Motor Controller Device Not Recognized!")

    def _initalize_audio_driver(self):
        self.ad = AudioDriver()

    def _initalize_fish_controller(self):
        self.fc = FishController(self.mc, self.ad)

    def _initalize_fish_api(self):
        self.fish_api = FishAPI()

    def _setup_rpi_button(self):
        print("setting up raspberry pi button on pin")
        import RPi.GPIO as GPIO
        GPIO.setwarnings(False)  # Ignore warning for now
        # GPIO.setmode(GPIO.BOARD)  # Use physical pin numbering
        GPIO.setup(RPI_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pin 10 to be an input pin and set

    def get_unique_id(self) -> str:
        mac_raw = getnode()
        return ':'.join(("%012X" % mac_raw)[i:i+2] for i in range(0, 12, 2))

    def internet_on(self) -> bool:
        try:
            requests.get('https://google.com', timeout=1)
            return True
        except Exception as err:
            return False

    def button_1_pressed(self) -> bool:
        if self.device_type == DeviceType.computer:
            return False
        elif self.device_type == DeviceType.raspberry_pi:
            import RPi.GPIO as GPIO
            return GPIO.input(RPI_BUTTON_PIN) == GPIO.HIGH
