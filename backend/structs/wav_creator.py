from gtts import gTTS, lang
from google.cloud import storage
from datetime import datetime
from structs import server_globals
from pydub import AudioSegment
import os

class WavCreator:

    # Generate an audio file for the given senetence, upload it to google cloud, and return a url to the file
    # language can be the key "en" or the language "english"
    def textToSpeach(self, sentence: str, language: str):
        timeSec = int(datetime.utcnow().timestamp())
        filename = "audio_" + str(timeSec)
        lang_key, lang_name = WavCreator.find_language_key_from_language_parameter(language)
        if not lang_key:
            lang_key = server_globals.default_language_key
        soundObj = gTTS(text=sentence, lang=lang_key, slow=False)
        soundObj.save("/tmp/" + filename + ".mp3")

        print("Converting " + filename + ".mp3 to " + filename + ".wav")
        sound = AudioSegment.from_mp3("/tmp/" + filename + ".mp3")
        sound.export("/tmp/" + filename + ".wav", format="wav")
        if server_globals.is_running_in_cloud():
            print("is running in google cloud")
        else:
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = server_globals.gcs_cred_path
        storage_client = storage.Client()
        bucket_name = "fish-audio-files"
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename + ".wav")
        blob.upload_from_filename("/tmp/" + filename + ".wav")
        print("File {} uploaded to {}.".format(filename + ".wav", bucket_name))
        return "https://storage.googleapis.com/" + bucket_name + "/" + filename + ".wav"

    @staticmethod
    def find_language_key_from_language_parameter(language_parameter: str):
        lang_param_clean = language_parameter.lower()
        for language_key, language_name in lang.tts_langs().items():
            if (lang_param_clean == language_key) or (lang_param_clean == language_name.lower()):
                return language_key, language_name
        return None, None
