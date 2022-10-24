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
        
    def shoot(self, game, x, y): 
        self.portals.add(Portal(screen=game.screen, x=x, y=y))
        print('*portal noises*')
        
    def update(self, facing):
        self.portals.update(facing)
        
    def draw(self):
        for port in self.portals.sprites():
            port.draw()
        
    
class Portal(Sprite):
    
    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.portal_timer = [pg.image.load(f'images/Portals/portal{n}.png') for n in range(4)]
        self.image = pg.image.load('images/Portals/portal0.png')
        self.rect = self.image.get_rect()
        self.timer = Timer(image_list=self.portal_timer)
        self.rect.centerx = x
        self.rect.bottom = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        
    def update(self, facing):
        if facing == 0: # face right
            self.x += 1
        elif facing == 1: # face left
            self.x -= 1
        elif facing == 2: # face up
            self.y += 1
        elif facing == 3: # face down
            self.y -= 1
        
        self.rect.x = self.x
        self.draw()
        
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)