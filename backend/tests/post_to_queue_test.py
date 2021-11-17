from fish_code import main
from _local_resources_.TestClass import TestClass


def test_bubbles_object_creation_success_201():
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
             'text': 'Hello World'
             }
        }
    ])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    main.hello_world(fake_post)
