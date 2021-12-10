from backend import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_get_success_200():
    fake_get = TestClass({})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    main.hello_world(fake_get)