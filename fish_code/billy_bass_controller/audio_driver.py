import pygame as pg
import audioread
from pydub import AudioSegment

freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 2048  # number of samples (experiment to get right sound)


class AudioDriver:

    def __init__(self):
        pg.mixer.init(freq, bitsize, channels, buffer)

    def play_file(self, file_path: str):
        """
        stream music with mixer.music module in blocking manner
        this will stream the sound from disk while playing
        """
        clock = pg.time.Clock()
        try:
            pg.mixer.music.load(file_path)
            print("Music file {} loaded!".format(file_path))
        except pg.error:
            print("File {} not found! {}".format(file_path, pg.get_error()))
            return

        pg.mixer.music.play()
        while pg.mixer.music.get_busy():
            clock.tick(30)

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

