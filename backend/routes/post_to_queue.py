import json
from structs import server_globals
import string


def post_to_queue(request):
    print("parameters passed: ", request)
    request_json = request.get_json()
    print("Json body: ", request_json)
    text = request.get_json()[0]['message']['text']
    devide_id = server_globals.parse_fish_id_from_text(text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    try:
        commands = server_globals.text_to_commands.convertTextToCommands(text)
    except KeyError as err:
        # When a word can't be deciphered, return these commands for the words "I'm sorry I do not understand the word _____"
        commands = "['O:4', 'C:2', 'C:2', 'O:4', 'C:2', 'O:1', 'O:4', 'C:2', 'O:4', 'C:2', 'O:4', 'C:2', 'O:3', 'C:2', 'C:2', 'O:1', 'C:2', 'C:2', 'O:4', 'C:2', 'C:2', 'C:2', 'O:1', 'C:2', 'O:4', 'C:2', 'O:1']"
        text = "Im sorry I do not understand the word " + str(err)
    audio_url = server_globals.wav_creator.textToSpeach(text)
    server_globals.fish_firestore.add_request_to_queue(text, commands, audio_url, devide_id)
    return json.dumps({"text_added_to_queue": text, "commands": commands, "audio_url": audio_url}), 201
