from structs.wav_creator import WavCreator
import structs.server_globals as server_globals


def _find_lang_key_from_message(message_text: str):
    words = message_text.split(" ")
    for word in words:
        lang_key, lang_name = WavCreator.find_language_key_from_language_parameter(word)
        if lang_key:
            return lang_key, lang_name
    return None, None


def _handle_language_change(message_text: str, device_id: str) -> str:
    print(f"handling language change on message: {message_text}")
    lang_key, lang_name = _find_lang_key_from_message(message_text)
    if not lang_key:
        return "I could not find a language in your message. You can try english, spanish, sweedish and a whole lot more. Ask christian for the full list"
    current_fish_info = server_globals.fish_firestore.get_fish_information(device_id)
    current_fish_info.language_key = lang_key
    server_globals.fish_firestore.set_fish_information(current_fish_info.dict())
    return f"now I am {lang_name}"


def handle_command_and_return_message(message_text: str, device_id: str) -> str:
    original_message = message_text
    if "set language" in message_text:
        return _handle_language_change(message_text, device_id)
    print("no command recognized in message. returning original")
    return original_message