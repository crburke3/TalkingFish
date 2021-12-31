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
    ids = server_globals.parse_fish_id_from_text("memae")
    assert "b8:27:eb:12:ea:dc" in ids


def test_device_parse_name_from_id():
    names = server_globals.parse_fish_id_from_text("b8:27:eb:12:ea:dc")
    assert "memae" in names


def test_device_parse_name_from_id_stripped():
    # this test is necessary because backend strips the : from the device ID in text
    names = server_globals.parse_fish_id_from_text("b827eb12eadc")
    assert "memae" in names


def test_find_language_key_by_name():
    name = "english"
    key = wav_creator.WavCreator.find_language_key_from_language_parameter(name)[0]
    assert key == "en"

def test_find_language_key_by_key():
    name = "en"
    key = wav_creator.WavCreator.find_language_key_from_language_parameter(name)[0]
    assert key == "en"

def test_get_fish_information():
    device_id = "b8:27:eb:e4:59:f4"
    fish_info = server_globals.fish_firestore.get_fish_information(device_id)
    assert fish_info.device_id == device_id
