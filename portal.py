import pygame as pg 
from pygame.sprite import Sprite, Group
from timer import Timer

class Portals:
    def __init__(self):
        self.portals = Group()
        self.portals_up = False
        
    def reset(self):
        self.portals.empty()
        self.portals_up = False
        
    def shoot(self, spawn_point, direction): pass
        
    
class Portal(Sprite):
    def __init__(self):
        super().__init__()
        self.portals
        