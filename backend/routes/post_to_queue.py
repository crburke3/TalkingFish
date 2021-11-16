import json


def post_to_queue(request):
    print("parameters passed: ", request)
    return json.dumps({"test": "test"}), 200