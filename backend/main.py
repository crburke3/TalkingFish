import json

from routes.post_to_queue import post_to_queue
from structs import server_globals, fish_firestore
from _local_resources_.TestClass import TestClass

# Globals Creation
server_globals.fish_firestore = fish_firestore.FishFirestore()  # initalize when main runs.


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
    else:
        return json.dumps({"ERROR": "unknown route"}), 401


if __name__ == '__main__':
    fake_post = TestClass({
        "message": {
            "text": "Hello world"
        }
    })
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    hello_world(fake_post)
