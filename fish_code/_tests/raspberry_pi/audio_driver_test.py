from audio_driver import AudioDriver
from fish_api import FishAPI


def test_audio_driver_scream_16bit_audio_local_computer():
    ad = AudioDriver()
    ad.play_wav_file("../../_resources/Ouche.wav")
    # lmaoooooo


def test_audio_driver_joke_16bit_audio_local_computer():
    ad = AudioDriver()
    ad.play_wav_file("../../_resources/joke.wav")
    # lmaoooooo


def test_download_audio_from_google_cloud_local_computer():
    fish_api = FishAPI()
    ad = AudioDriver()
    url = "https://storage.googleapis.com/fish-1-audio-files/joke.wav"
    local_path = fish_api.download_file(url)
    ad.play_wav_file(local_path)

