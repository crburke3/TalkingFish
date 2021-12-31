import json

from routes.post_to_queue import post_to_queue
from routes.get_from_queue import get_from_queue
from routes.post_fish_information import post_fish_information
from structs import server_globals, fish_firestore, text_to_commands, wav_creator

# Globals Creation
server_globals.fish_firestore = fish_firestore.FishFirestore()
server_globals.text_to_commands = text_to_commands.TextToCommands()
server_globals.wav_creator = wav_creator.WavCreator()


def test_device_parse_id_from_name():
    id = server_globals.parse_fish_id_from_text("memae")
    assert id == "b8:27:eb:12:ea:dc"

def test_device_parse_name_from_id():
    name = server_globals.parse_fish_id_from_text("b8:27:eb:12:ea:dc")
    assert name == "memae"

def test_device_parse_name_from_id_stripped():
    # this test is necessary because backend strips the : from the device ID in text
    name = server_globals.parse_fish_id_from_text("b827eb12eadc")
    assert name == "memae"

