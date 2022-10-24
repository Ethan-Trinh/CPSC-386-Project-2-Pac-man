import pygame as pg 
from pygame.sprite import Sprite, Group
from timer import Timer

class Portals:
    def __init__(self):
        self.portals = Group()
        self.portals_up = False
        
    def up_port(self):
        self.portals_up = True
        
    def reset(self):
        self.portals.empty()
        self.portals_up = False
        
    def shoot(self, game, x, y, facing): 
        self.portals.add(Portal(screen=game.screen, x=x, y=y, facing=facing))
        print('*portal noises*')
        
    def update(self):
        self.portals.update()
        
    def draw(self):
        for port in self.portals.sprites():
            port.draw()
        
    
class Portal(Sprite):
    
    def __init__(self, screen, x, y, facing):
        super().__init__()
        self.screen = screen
        self.portal_timer = [pg.image.load(f'images/Portals/portal{n}.png') for n in range(4)]
        self.image = pg.image.load('images/Portals/portal0.png')
        self.rect = self.image.get_rect()
        self.timer = Timer(image_list=self.portal_timer, delay=200)
        self.rect.centerx = x
        self.rect.bottom = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.facing = facing
        
    def update(self):
        if self.facing == 0: # face right
            self.x += 1
            self.rect.x = self.x
        elif self.facing == 1: # face left
            self.x -= 1
            self.rect.x = self.x
        elif self.facing == 2: # face up
            self.y -= 1
            self.rect.y = self.y
        elif self.facing == 3: # face down
            self.y += 1
            self.rect.y = self.y
    
        self.draw()
        
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)