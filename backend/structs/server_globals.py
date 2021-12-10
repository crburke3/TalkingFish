# python Modules
import os

# User defined modules
from structs.fish_firestore import FishFirestore
from structs.text_to_commands import TextToCommands
from structs.wav_creator import WavCreator

base_folder_path = f"{os.path.dirname(os.path.abspath(__file__))}".replace("/structs", "")
gcs_cred_path = f"{base_folder_path}/resources/credentials.json"

fish_firestore: FishFirestore = None
text_to_commands: TextToCommands = None
wav_creator: WavCreator = None
language_key = "en"

name_to_device_id = {
    "lib": "b8:27:eb:e4:59:f4"
}

DEFAULT_DEVICE_ID = "DEFAULT_DEVICE_ID"


def parse_fish_id_from_text(message_text: str) -> str:
    for key, value in name_to_device_id.items():
        if key in message_text:
            return value
    return DEFAULT_DEVICE_ID
