import pygame as pg 
import json

class Spritesheet:
    def __init__(self, filename): #filename is the spritesheet
        self.filename = filename
        self.sprite_sheet = pg.image.load(filename).convert()
        
    def get_sprite(self, x, y, w, h):
        sprite = pg.Surface((w, h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x, y, w, h))
        return sprite
    
    def parse_sprite(self, name): pass