import wave, time
from pygame import mixer
import os
from mutagen.mp3 import MP3
import audioread
from os import path
from pydub import AudioSegment

class AudioDriver:

    # def __init__(self):

    def play_file(self, file_path:str):
        if "mp3" in file_path:
            raise Exception("must be .wav file")
            # self._play_mp3_file(file_path)
        elif "wav" in file_path:
            self._play_wav_file(file_path)
        else:
            raise Exception(f"File type: {file_path} not recognized")

    def get_audio_length_seconds(self, file_path: str) -> float:
        if not file_path:
            return 5.0
        if "mp3" in file_path:
            raise Exception("Must pass a .wav file")
            # return self._get_mp3_length(file_path)
        elif "wav" in file_path:
            return self._get_wav_length(file_path)
        else:
            raise Exception(f"File type: {file_path} not recognized for time length")

    def _play_wav_file(self, file_path: str):
        file_wav = wave.open(file_path)
        frequency = file_wav.getframerate()
        mixer.init(frequency=frequency)
        assert os.path.exists(file_path), Exception("Cant find file: ", file_path)
        mixer.music.load(file_path)
        mixer.music.play()
        while mixer.music.get_busy() == True:
            continue

    def _play_mp3_file(self, file_path:str):
        mixer.init()
        mixer.music.load(file_path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(0.1)

    # def _get_mp3_length(self, file_path:str)->float:
    #     mixer.init()
    #     mixer.music.load(file_path)
    #     song = MP3(file_path)
    #     songLength = song.info.length
    #     print(songLength)
    #     return songLength

    def _get_wav_length(self, file_path:str) -> float:
        with audioread.audio_open(file_path) as f:
            totalsec = f.duration
            min, sec = divmod(totalsec, 60)
            return sec

    def convert_mp3_to_wav(self, mp3_path:str):
        out_path = mp3_path[:-3]  # sketchy
        out_path += ".wav"
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(out_path, format="wav")
        return out_path

