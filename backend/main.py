import json

from routes.post_to_queue import post_to_queue
from routes.get_from_queue import get_from_queue
from structs import server_globals, fish_firestore, text_to_commands, wav_creator
from _local_resources_.TestClass import TestClass


# Globals Creation
server_globals.fish_firestore = fish_firestore.FishFirestore()
server_globals.text_to_commands = text_to_commands.TextToCommands()
server_globals.wav_creator = wav_creator.WavCreator()


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

fake_post = TestClass([
        {'time': '2021-11-16T16:35:57.159Z', 
         'type': 'message-received', 
         'to': '+19843586100', 
         'description': 'Incoming message received', 
         'message': {
             'id': '891b9238-c8b7-43e3-b681-56e74c482d57', 
             'owner': '+19843586100', 
             'applicationId': 'f50bebeb-57a7-4dda-bbb4-3567292acbff', 
             'time': '2021-11-16T16:35:57.062Z', 
             'segmentCount': 1, 
             'direction': 'in', 
             'to': ['+19843586100'], 
             'from': '+17036095909', 
             'text': 'Will this be a wave?'
             }
        }
    ])
fake_post.path = "post_to_queue"
fake_post.method = "POST"
hello_world(fake_post)