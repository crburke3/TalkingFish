# import pygame as pg
import os
import audioread
from pydub import AudioSegment

freq = 16000  # wav frequency
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024  # number of samples (experiment to get right sound)
vol = 0.75

class AudioDriver:

    # def __init__(self, volume=vol):
    #     pg.mixer.init(freq, bitsize, channels, buffer)
    #     pg.mixer.music.set_volume(volume)

    def play_file(self, file_path: str):
        os.system("aplay /usr/share/sounds/alsa/Front_Center.wav &")

    # def play_file(self, file_path: str):
    #     """
    #     stream music with mixer.music module in blocking manner
    #     this will stream the sound from disk while playing
    #     """
    #     clock = pg.time.Clock()
    #     try:
    #         pg.mixer.music.load(file_path)
    #         print("Music file {} loaded!".format(file_path))
    #     except pg.error:
    #         print("File {} not found! {}".format(file_path, pg.get_error()))
    #         return
    #
    #     pg.mixer.music.play()
    #     while pg.mixer.music.get_busy():
    #         clock.tick(30)

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
        out_path += "wav"
        sound = AudioSegment.from_mp3(mp3_path)
        sound.export(out_path, format="wav")
        return out_path

