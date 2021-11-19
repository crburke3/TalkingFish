# python Modules
import os

# User defined modules
from structs.fish_firestore import FishFirestore
from structs.text_to_commands import TextToCommands
from structs.mp3_creator import Mp3Creator

base_folder_path = f"{os.path.dirname(os.path.abspath(__file__))}".replace("/structs", "")
gcs_cred_path = f"{base_folder_path}/resources/credentials.json"

fish_firestore: FishFirestore = None
text_to_commands: TextToCommands = None
mp3_creator: Mp3Creator = None
