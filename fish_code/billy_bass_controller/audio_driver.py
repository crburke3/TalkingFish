import wave, time
from pygame import mixer
import os
from mutagen.mp3 import MP3

class AudioDriver:

    # def __init__(self):

    def play_wav_file(self, file_path: str):
        file_wav = wave.open(file_path)
        frequency = file_wav.getframerate()
        mixer.init(frequency=frequency)
        assert os.path.exists(file_path), Exception("Cant find file: ", file_path)
        mixer.music.load(file_path)
        mixer.music.play()
        while mixer.music.get_busy() == True:
            continue

    def play_mp3_file(self, file_path:str):
        mixer.init()
        mixer.music.load(file_path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(0.1)

    def get_mp3_length(self, file_path:str)->float:
        mixer.init()
        mixer.music.load(file_path)
        song = MP3(file_path)
        songLength = song.info.length
        print(songLength)
        return songLength