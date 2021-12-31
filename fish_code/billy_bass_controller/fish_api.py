import requests, os
from datetime import datetime

from .fish_command import FishCommand
from .audio_driver import AudioDriver
from .globals import get_device_id


def _download_file(url):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    local_filename = url.split('/')[-1]
    local_path = f"{dir_path}/downloads/{local_filename}"
    if os.path.exists(local_path):
        print("WAV file already exists, deleteing...")
        os.remove(local_path)
        print("existing WAV file deleted!")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print("successfully downloaded to: ", local_path)
    return local_path


class FishAPI:

    def get_next_item_in_queue(self):
        id = get_device_id()
        url = f"http://us-central1-talkingfish-332301.cloudfunctions.net/addToQueue/get_from_queue?device_id={id}"
        return requests.get(url)

    def download_song_for_object(self, cmd: FishCommand):
        local_url = _download_file(cmd.song_url)
        if "mp3" in local_url:
            print("file recognized as .mp3 converting...")
            audio_driver = AudioDriver()
            wav_path = audio_driver.convert_mp3_to_wav(local_url)
            cmd.local_song_url = wav_path
            return
        cmd.local_song_url = local_url


    def post_fish_formation(self):
        url = "http://us-central1-talkingfish-332301.cloudfunctions.net/addToQueue/add_fish_data"
        fish_data = {
            "device_id": get_device_id(),
            "state": "booting",
            "last_updated": datetime.utcnow()
        }
        requests.post(url, fish_data)
        print("successfully posted fish boot info")
