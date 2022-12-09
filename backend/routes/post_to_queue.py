import json, string

from structs import server_globals, command_handler


def post_to_queue(request):

    print("parameters passed: ", request)
    request_json = request.form.to_dict()
    print("Json body: ", request_json)
    # text = request.get_json()[0]['message']['text']
    text = request_json['Body']
    print(f"recieved text: {text}")
    device_ids = server_globals.parse_fish_id_from_text(text)
    if "local:" in text:
        file_name = text.replace("local:", "")
        post_data = {
            "local_file": file_name
        }
        for device_id in device_ids:
            server_globals.fish_firestore.post_raw(device_id, post_data)
        return json.dumps(post_data), 201

    print(f"chose devices by ID: {device_ids}")
    text = text.translate(str.maketrans('', '', string.punctuation))
    try:
        commands = server_globals.text_to_commands.convertTextToCommands(text)
    except KeyError as err:
        # When a word can't be deciphered, return these commands for the words "I'm sorry I do not understand the word _____"
        commands = "['O:4', 'C:2', 'C:2', 'O:4', 'C:2', 'O:1', 'O:4', 'C:2', 'O:4', 'C:2', 'O:4', 'C:2', 'O:3', 'C:2', 'C:2', 'O:1', 'C:2', 'C:2', 'O:4', 'C:2', 'C:2', 'C:2', 'O:1', 'C:2', 'O:4', 'C:2', 'O:1']"

        # text = "Im sorry I do not understand the word " + str(err)
    for device in device_ids:
        text = command_handler.handle_command_and_return_message(text, device)
        fish_language = server_globals.fish_firestore.get_fish_information(device).language_key
        audio_url = server_globals.wav_creator.textToSpeach(text, fish_language)
        server_globals.fish_firestore.add_request_to_queue(text, commands, audio_url, device)
    return json.dumps({"text_added_to_queue": text, "commands": commands, "audio_url": audio_url}), 201
