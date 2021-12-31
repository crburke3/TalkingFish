from backend import main
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
             'text': 'maddie Hello World I am a sweedish fish'
             }
        }
    ])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201

def test_bubbles_object_creation_success_201_many_accents():
    import gtts
    from structs import server_globals
    key_arr = list(gtts.lang.tts_langs().keys())[20:40]
    key_arr = ["sw"]
    for key in key_arr:
        print("creating call for: ", key)
        server_globals.default_language_key = key

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
                 'text': 'Hello World I am a talking fish'
                 }
            }
        ])
        fake_post.path = "post_to_queue"
        fake_post.method = "POST"
        resp = main.hello_world(fake_post)
        assert resp[1] == 201

def test_bubbles_object_creation_success_201_many_accents_for_maddie():
    import gtts
    from structs import server_globals
    key_arr = list(gtts.lang.tts_langs().keys())[20:40]
    language_arr = list(gtts.lang.tts_langs().values())[20:40]

    for i, key in enumerate(key_arr):
        language = language_arr[i]
        print("creating call for: ", key)
        server_globals.default_language_key = key

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
                 'text': f'maddie here is a {language} accent'
                 }
            }
        ])
        fake_post.path = "post_to_queue"
        fake_post.method = "POST"
        resp = main.hello_world(fake_post)
        assert resp[1] == 201

def test_multiple_bubbles_object_creation_success_201():
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
             'text': 'maddie memae Hello World I am a talking fish'
             }
        }
    ])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201

def test_multiple_bubbles_object_creation_success_201():
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
             'text': 'b8:27:eb:e4:59:f4 I AM ALIVE'
             }
        }
    ])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201

def test_set_language_to_sweedish():
    from structs import server_globals, fish_firestore, text_to_commands, wav_creator


    # # Globals Creation
    # if not server_globals.fish_firestore:
    #     server_globals.fish_firestore = fish_firestore.FishFirestore()
    # if not server_globals.text_to_commands:
    #     server_globals.text_to_commands = text_to_commands.TextToCommands()
    # if not server_globals.wav_creator:
    #     server_globals.wav_creator = wav_creator.WavCreator()

    fake_post = TestClass([{'message': {'text': 'maddie set language to swedish'}}])
    fake_post.path = "post_to_queue"
    fake_post.method = "POST"
    resp = main.hello_world(fake_post)
    assert resp[1] == 201