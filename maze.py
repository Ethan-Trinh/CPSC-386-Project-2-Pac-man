from wsgiref.validate import _WriterCallback
import pygame as pg 
import csv, os
from pygame.sprite import Sprite
from spritesheet import Spritesheet

wall_spritesheet = Spritesheet('images/PacmanWalls.png')
a_wall = wall_spritesheet.get_sprite(0, 0, 32, 32)

class MazeTile(Sprite):
    def __init__(self, image, x, y, spritesheet):
        self.image = spritesheet.parse_sprite(image)
        self.rect