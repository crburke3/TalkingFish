from gtts import gTTS
from google.cloud import storage
from datetime import datetime
from structs import server_globals
import os

class Mp3Creator:

    # Generate an audio file for the given senetence, upload it to google cloud, and return a url to the file
    def textToSpeach(self, sentence: str):
        timeSec = int(datetime.utcnow().timestamp())
        filename = "audio_" + str(timeSec) + ".mp3"
        print(filename)
        soundObj = gTTS(text=sentence, lang='en', slow=False)
        soundObj.save("/tmp/" + filename)

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = server_globals.gcs_cred_path
        storage_client = storage.Client()
        bucket_name = "fish-1-audio-files"
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(filename)
        blob.upload_from_filename("/tmp/" + filename)
        print("File {} uploaded to {}.".format(filename, bucket_name))
        return "https://storage.googleapis.com/" + bucket_name + "/" + filename