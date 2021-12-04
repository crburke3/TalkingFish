import sys
sys.path.append("..")
from audio_driver import AudioDriver  # ignore warning


def test_wav_play():
    file_path = "../../_resources/joke.wav"
    driver = AudioDriver()
    driver.play_file(file_path)

test_wav_play()

sys.path.append("../..")
from billy_bass_controller import Device, FishCommand

if __name__ == '__main__':
    device = Device()
    test_wav_play()

