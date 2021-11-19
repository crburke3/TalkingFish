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
