from backend import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_get_success_200():
    fake_get = TestClass({"device_id": "b8:27:eb:e4:59:f4"})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    resp = main.hello_world(fake_get)
    print(resp)

def test_bubbles_object_get_success_with_specific_mac():
    mac = "b8:27:eb:d6:63:07"
    fake_get = TestClass({"device_id": mac})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    resp = main.hello_world(fake_get)
    print(resp)
