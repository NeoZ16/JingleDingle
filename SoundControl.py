import time

import pygame
from pygame.mixer import Sound


class SoundControl:
    START_JINGLE = 0
    WARNING_JINGLE = 1
    END_JINGLE = 2

    def __init__(self, start_jingle_path, warning_jingle_path, end_jingle_path, media_control):
        pygame.mixer.init()

        self.start_jingle = Sound(start_jingle_path)
        self.warning_jingle = Sound(warning_jingle_path)
        self.end_jingle = Sound(end_jingle_path)

        print(f'[*] Loaded jingles:')
        print(f'Start: {start_jingle_path}')
        print(f'Warning: {warning_jingle_path}')
        print(f'End: {end_jingle_path}')

        self.jingles = [self.start_jingle, self.warning_jingle, self.end_jingle]
        self.media_control = media_control

    def play_jingle(self, jingle):
        current_playing = False

        if self.media_control.is_playing():
            self.media_control.stop_playback()
            current_playing = True

        self.jingles[jingle].play()

        while pygame.mixer.get_busy():
            time.sleep(1)

        if current_playing:
            self.media_control.start_playback()
