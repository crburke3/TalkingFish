import json
from structs import server_globals


def post_to_queue(request):
    print("parameters passed: ", request)
    text = request.body.message.text
    server_globals.fish_firestore.add_request_to_queue(text)
    return json.dumps({"text_added_to_queue": text}), 201
