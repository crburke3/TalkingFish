import json
from structs import server_globals
from structs.text_to_commands import TextToCommands


def post_to_queue(request):
    print("parameters passed: ", request)
    text = request.get_json()['message']['text']
    commands = TextToCommands.convertTextToCommands(text)
    server_globals.fish_firestore.add_request_to_queue(text, commands)
    return json.dumps({"text_added_to_queue": text, "commands": commands}), 201
