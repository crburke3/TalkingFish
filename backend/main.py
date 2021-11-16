import json

from routes.post_to_queue import post_to_queue

def hello_world(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if "post_to_queue" in request.path:
        return post_to_queue(request)
    else:
        return json.dumps({"ERROR": "unknown route"}), 401

