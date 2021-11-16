import json
from structs import server_globals


def post_to_queue(request):
    print("parameters passed: ", request)
    server_globals.fish_firestore.add_request_to_queue("TEST TEXT")
    return json.dumps({"test": "test"}), 201
