import sys
sys.path.append("..")
from audio_driver import AudioDriver  # ignore warning


def test_wav_play():
    file_path = "../../_resources/joke.wav"
    driver = AudioDriver()
    driver.play_file(file_path)


if __name__ == '__main__':
    test_wav_play()
