import sys
sys.path.append("..")
from audio_driver import AudioDriver  # ignore warning


def test_mp3():
    file_path = "../../_resources/scream.mp3"
    driver = AudioDriver()
    driver.play_file(file_path)


def test_get_mp3_length():
    file_path = "../../_resources/scream.mp3"
    driver = AudioDriver()
    print(driver.get_audio_length_seconds(file_path))

def test_wav_play():
    file_path = "../../_resources/joke.wav"
    driver = AudioDriver()
    driver.play_file(file_path)


test_wav_play()
