from backend import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_get_success_200():
    fake_get = TestClass({"device_id": "b8:27:eb:e4:59:f4"})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    resp = main.hello_world(fake_get)
    print(resp)
