import json

from routes.post_to_queue import post_to_queue
from routes.get_from_queue import get_from_queue
from structs import server_globals, fish_firestore, text_to_commands, mp3_creator
from _local_resources_.TestClass import TestClass

# Globals Creation
server_globals.fish_firestore = fish_firestore.FishFirestore()
server_globals.text_to_commands = text_to_commands.TextToCommands()
server_globals.mp3_creator = mp3_creator.Mp3Creator()


def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    if "post_to_queue" in request.path:
        return post_to_queue(request)
    elif "get_from_queue" in request.path:
        return get_from_queue()
    else:
        return json.dumps({"ERROR": "unknown route"}), 401
