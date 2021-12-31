import time

from backend import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_get_success_200():
    fake_get = TestClass({"device_id": "b8:27:eb:e4:59:f4"})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    resp = main.hello_world(fake_get)
    print(resp)
    assert resp[1] == 200

def test_bubbles_object_get_success_with_specific_mac():
    # post fish data to speak
    mac = "computer"
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
             'text': f'{mac} Hello World I am a talking fish'
         }
         }
    ])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    post_resp = main.hello_world(fake_post)
    time.sleep(2)
    # get fish data we posted
    main.hello_world(fake_post)
    fake_get = TestClass({"device_id": mac})
    fake_get.path = "get_from_queue"
    fake_get.method = "GET"
    resp = main.hello_world(fake_get)
    print(resp)
    assert resp[1] == 200


