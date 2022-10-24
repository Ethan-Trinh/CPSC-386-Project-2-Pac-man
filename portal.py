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
        self.portals.add(Portal(screen=game.screen, x=x+10, y=y+10, facing=facing))
        print('*portal noises*')
        
    def update(self, tiles, pacman):
        self.portals.update(tiles, pacman)
        
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
        self.hitbox = self.rect
        self.hitbox.w = self.rect.w/4
        self.hitbox.h = self.rect.h/4
        self.timer = Timer(image_list=self.portal_timer, delay=200)
        self.rect.centerx = x-10
        self.rect.bottom = y-10
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.facing = facing
        self.spawn_location = (0, 0)
        self.hold = self.facing
        
    def update(self, tiles, pacman):
        if self.facing == 0: # face right
            self.x += 1
            self.rect.x = self.x
            self.hitbox.x = self.rect.centerx
        elif self.facing == 1: # face left
            self.x -= 1
            self.rect.x = self.x
            self.hitbox.x = self.rect.centerx
        elif self.facing == 2: # face up
            self.y -= 1
            self.rect.y = self.y
            self.hitbox.y = self.rect.centery
        elif self.facing == 3: # face down
            self.y += 1
            self.rect.y = self.y
            self.hitbox.y = self.rect.centery
        elif self.facing == 4:
            if self.hold == 0:
                self.spawn_location =(self.rect.x, self.rect.y)
            elif self.hold  == 1:
                self.spawn_location =(self.rect.x, self.rect.y)
            elif self.hold  == 2:
                self.spawn_location =(self.rect.x, self.rect.y)
            elif self.hold  == 3:
                self.spawn_location =(self.rect.x, self.rect.y)
            self.check_pacman(pacman=pacman)    
        
        pg.draw.rect(surface = self.screen, color=(225,225,225), rect=self.hitbox)
        
        self.check_collision(tiles = tiles)
    
        self.draw()

    def tile_check(self, tiles):
        col = []
        for tile in tiles:
            if self.hitbox.colliderect(tile):
                col.append(tile)
        return col
    
    def check_collision(self, tiles):
        collisions = self.tile_check(tiles)
        for tile in collisions:
            self.facing = 4
    
    def check_pacman(self, pacman):
        print('pacman was here')

    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)