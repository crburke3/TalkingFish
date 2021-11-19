import json
from structs import server_globals
import string

def post_to_queue(request):
    print("parameters passed: ", request)
    request_json = request.get_json()
    print("Json body: ", request_json)
    text = request.get_json()[0]['message']['text']
    text = text.translate(str.maketrans('', '', string.punctuation))
    commands = server_globals.text_to_commands.convertTextToCommands(text)
    audio_url = server_globals.mp3_creator.textToSpeach(text)
    server_globals.fish_firestore.add_request_to_queue(text, commands, audio_url)
    return json.dumps({"text_added_to_queue": text, "commands": commands, "audio_url": audio_url}), 201
