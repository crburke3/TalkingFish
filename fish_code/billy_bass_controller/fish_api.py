import requests, os

from .fish_command import FishCommand


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
        return requests.get("http://us-central1-talkingfish-332301.cloudfunctions.net/addToQueue/get_from_queue")

    def download_song_for_object(self, cmd: FishCommand):
        local_url = _download_file(cmd.song_url)
        cmd.local_song_url = local_url
