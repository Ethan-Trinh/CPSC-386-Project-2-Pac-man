import pygame as pg 
import csv, os
from pygame.sprite import Sprite

class MazeTile(Sprite):
    def __init__(self, image, x, y, spritesheet):
        self.image = spritesheet.parse_sprite(image)
        self.rect