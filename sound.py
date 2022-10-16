import pygame as pg
import time

class Sounds:
    def __init__(self):
        pg.mixer.init()
        bgm = pg.mixer.Sound('sounds/siren_1.wav')
        self.munch_sound_1 = pg.mixer.Sound('sounds/munch_1.wav')
        self.munch_sound_2 = pg.mixer.Sound('sounds/munch_2.wav') 
        self.death_sound = pg.mixer.Sound('sounds/death.wav')

        pg.mixer.music.load(bgm)
        pg.mixer.music.set_volume(0.1)

        self.alternate_munch = 0

    def play_bgm(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_music(self):
        pg.mixer.music.stop()

    def munch_sound(self):
        if self.alternate_munch == 0:
            pg.mixer.Sound.play(self.munch_sound_1)
            self.alternate_munch += 1
        else:
            pg.mixer.Sound.play(self.munch_sound_2)
            self.alternate_munch -= 1

    def dead_sound(self):
        self.stop_music()
        pg.mixer.Sound.play(self.death_sound)
        