import json, requests
from structs import server_globals


def post_fish_information(request):
    request_json = server_globals.parse_basic_arguments(request)
    print("fish post data: ", request_json)

    server_globals.fish_firestore.set_fish_information(request_json)
    return json.dumps({"message": "success!"}), 201
