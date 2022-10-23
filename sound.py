import pygame as pg
import time

class Sounds:
    def __init__(self):
        pg.mixer.init()
        #bgm = pg.mixer.Sound('sounds/siren_1.wav')
        self.munch_sound_1 = pg.mixer.Sound('sounds/munch_1.wav')
        self.munch_sound_2 = pg.mixer.Sound('sounds/munch_2.wav') 
        
        self.death_sound = pg.mixer.Sound('sounds/death.wav')
        self.game_start_sound = pg.mixer.Sound('sounds/game_start.wav')
        self.intro_screen_music = pg.mixer.Sound('sounds/PacMan (Electro 2014 Remix).wav')
        self.eat_power=  pg.mixer.Sound('sounds/power_pellet.wav')
        self.eat_fruit=  pg.mixer.Sound('sounds/eat_fruit.wav')
        self.eat_ghost=  pg.mixer.Sound('sounds/eat_ghost.wav')
        self.ghost_retreat_sound = pg.mixer.Sound('sounds/retreating.wav')
        self.intermission = pg.mixer.Sound('sounds/intermission.wav')
        pg.mixer.music.load('sounds/siren_2.wav')
        pg.mixer.music.set_volume(0.1)

        self.alternate_munch = 0
        self.alternate_death = 0
    def play_bgm(self):
        pg.mixer.music.play(-1, 0.0)

    def stop_music(self):
        pg.mixer.music.stop()
    def play_intro_sound(self):
        pg.mixer.Sound.play(self.intro_screen_music)
        self.stop_music()
        

    def munch_sound(self):
        if self.alternate_munch == 0:
            pg.mixer.Sound.play(self.munch_sound_1)
            self.alternate_munch += 1
        else:
            pg.mixer.Sound.play(self.munch_sound_2)
            self.alternate_munch -= 1
            
    def eat_power_sound(self):
         pg.mixer.Sound.play(self.eat_power, loops = 5)

    def eat_fruit_sound(self):
        pg.mixer.Sound.play(self.eat_fruit)

    def eat_ghost_sound(self):
        pg.mixer.Sound.play(self.eat_ghost)

    def ghost_retreat(self):
        pg.mixer.Sound.play(self.ghost_retreat_sound, loops = 5)

    def packman_die_sound(self):
        self.stop_music()
        pg.mixer.Sound.play(self.death_sound, loops = 0)

    def start_sound(self):
        self.stop_music()
        pg.mixer.Sound.play(self.game_start_sound)
        self.stop_music()

    def dead_sound(self):
        self.stop_music()
        pg.mixer.Sound.play(self.death_sound)
        self.stop_music()
        