import json

from routes.post_to_queue import post_to_queue
from routes.get_from_queue import get_from_queue
from routes.post_fish_information import post_fish_information
from structs import server_globals, fish_firestore, text_to_commands, wav_creator

# Globals Creation
server_globals.fish_firestore = fish_firestore.FishFirestore()
server_globals.text_to_commands = text_to_commands.TextToCommands()
server_globals.wav_creator = wav_creator.WavCreator()

def test_get_name_to_device_id_dict():
    dict = server_globals.fish_firestore.get_name_to_device_id_dict()
    assert dict is not None