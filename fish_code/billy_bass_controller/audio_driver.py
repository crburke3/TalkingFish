import pygame
import os


class AudioDriver:

    def __init__(self):
        pygame.mixer.init()

    def play_wav_file(self, file_path: str):
        assert os.path.exists(file_path)
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
