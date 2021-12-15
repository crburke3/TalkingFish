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

DEFAULT_DEVICE_ID = "DEFAULT_DEVICE_ID"

name_to_device_id = {
    "lib": "b8:27:eb:e4:59:f4",
    "DEFAULT_DEVICE_ID": "fish_1",
    "memae": ""
}


def parse_fish_id_from_text(message_text: str) -> str:
    print(f"parsing device id from: {message_text}")
    for key, value in name_to_device_id.items():
        search_text = message_text.lower()
        print(f"checking for key: {key} in {message_text}")
        if key in search_text:
            return value
    return DEFAULT_DEVICE_ID


def parse_basic_arguments(request):
    try:
        fields = {}
        data = {}
        try:
            data.update(request.args)
            print(f"got request.args: {data}")
        except: x = 5

        try:
            data.update(request.form.to_dict())
            print(f"got request.form: {data}")
        except:x = 5

        try:
            data.update(request.get_json())
            print(f"got request.get_json(): {data}")
        except: x = 5

        try:
            fields["files"] = request.files.to_dict()
            print(f"got request files: {fields['files']}")
        except: x = 5

        for field in data:
            fields[field] = data[field]
        print(f"received arguments: {fields.items()}")
        fields["requestMethod"] = request.method
        return fields
    except Exception as e:
        print(f"parse_basic_arguments error: {str(e)}")
        return None

