import json
from structs import server_globals


def get_from_queue():
    print("Request to get latest from queue received")
    commands = "No commands found"
    audio_url = "No Audio URL found"

    bubbles = server_globals.fish_firestore.get_request_from_queue()
    print(bubbles)

    if bubbles == 404:
        print("There is nothing on the queue. Returning a 404...")
        return json.dumps({}), 404

    if 'commands' in bubbles:
        commands = bubbles['commands']
    if 'audio_url' in bubbles:
        audio_url = bubbles['audio_url']
        
    server_globals.fish_firestore.delete_request_from_queue(bubbles['queue_count'])
    return json.dumps({"commands": commands, "audio_url": audio_url}), 200