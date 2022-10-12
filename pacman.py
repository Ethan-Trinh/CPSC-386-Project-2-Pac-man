import pygame as pg
from pygame.sprite import Sprite
from game_functions import clamp
from timer import Timer
from vector import Vector

class Pacman(Sprite):
    pacman_images = [pg.image.load(f'images/pacmaneat/pacman{n}.png') for n in range(1, 5)]
    pacman_death = [pg.image.load(f'images/pacmandie/pacmandie{n}.png') for n in range(1, 15)]

    def __init__(self, settings, screen):#, sound):
        super().__init__()
        self.settings = settings
        self.screen = screen
        #self.sound = sound
        self.lives = 3
        self.dying = False
        self.dead = False

        self.timer_normal = Timer(image_list=Pacman.pacman_images)
        self.timer_death = Timer(image_list=Pacman.pacman_death, delay=100, is_loop=False)
        self.timer = self.timer_normal

    def hit(self):
        if not self.dying:
            print(f'Pac Man has been hit!')
            self.dying = True
            self.timer = self.timer_death

    def really_dead(self):
        self.lives -= 1
        print(f'Pac Man died, {self.lives} lives remaining')

    def reset(self):
        self.dying = False
        self.dead = False
        self.timer = self.timer_normal
        self.timer_death.reset()


    def update(self):
        self.draw()

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        self.screen.blit(image, rect)