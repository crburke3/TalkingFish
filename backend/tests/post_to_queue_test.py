import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_creation_success_201():
    fake_post = TestClass({
        "message": {
            "text": "Hello, world!!"
        }
    })
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    main.hello_world(fake_post)
