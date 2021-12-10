import json, requests
from structs import server_globals


def get_from_queue(request):
    print("Request to get latest from queue received")
    commands = "No commands found"
    audio_url = "No Audio URL found"
    request_json = request.get_json()
    if not request_json:
        request_json = {}
    print("Json body: ", request_json)

    device_id = request_json.get("device_id", server_globals.DEFAULT_DEVICE_ID)
    bubbles = server_globals.fish_firestore.get_request_from_queue(device_id)
    print(bubbles)

    if bubbles == 404:
        print("There is nothing on the queue. Returning a 404...")
        return json.dumps({}), 404

    if 'commands' in bubbles:
        commands = bubbles['commands']
    if 'audio_url' in bubbles:
        audio_url = bubbles['audio_url']
        
    server_globals.fish_firestore.delete_request_from_queue(bubbles['queue_count'], device_id)
    return json.dumps({"commands": commands, "audio_url": audio_url}), 200