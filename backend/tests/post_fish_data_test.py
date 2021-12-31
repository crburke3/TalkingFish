from backend import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_get_success_200():
    fake_post = TestClass({"device_id": "THIS A TEST"})
    fake_post.path = "add_fish_data"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 200
