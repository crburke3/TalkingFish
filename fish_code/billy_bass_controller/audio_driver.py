import pygame, wave
import os

class AudioDriver:

    # def __init__(self):

    def play_wav_file(self, file_path: str):
        file_wav = wave.open(file_path)
        frequency = file_wav.getframerate()
        pygame.mixer.init(frequency=frequency)
        assert os.path.exists(file_path)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
