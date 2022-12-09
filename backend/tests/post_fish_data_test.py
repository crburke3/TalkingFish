from backend import main
from _local_resources_.TestClass import TestClass



def test_bubbles_object_get_success_200():
    post_data = [
        {
            "message": {
                "text": "be careful. it might be fishy down there"
            }
        }
    ]
    fake_post = TestClass(post_data)
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201
