from gtts import gTTS
from google.cloud import storage
from datetime import datetime
from structs import server_globals
from pydub import AudioSegment
import os

class WavCreator:

    # Generate an audio file for the given senetence, upload it to google cloud, and return a url to the file
    def textToSpeach(self, sentence: str):
        timeSec = int(datetime.utcnow().timestamp())
        filename = "audio_" + str(timeSec)
        soundObj = gTTS(text=sentence, lang=server_globals.language_key, slow=False)
        soundObj.save("/tmp/" + filename + ".mp3")

        print("Converting " + filename + ".mp3 to " + filename + ".wav")
        sound = AudioSegment.from_mp3("/tmp/" + filename + ".mp3")
        sound.export("/tmp/" + filename + ".wav", format="wav")

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = server_globals.gcs_cred_path
        storage_client = storage.Client()
        bucket_name = "fish-1-audio-files"
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename + ".wav")
        blob.upload_from_filename("/tmp/" + filename + ".wav")
        print("File {} uploaded to {}.".format(filename + ".wav", bucket_name))
        return "https://storage.googleapis.com/" + bucket_name + "/" + filename + ".wav"