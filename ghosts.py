from re import S
from ast import IsNot, Or
from email.headerregistry import HeaderRegistry
from random import randint
import pygame as pg
from pygame.sprite import Sprite, Group
from pacman import Pacman
from timer import Timer
from vector import Vector
from game_functions import clamp
import random

class Ghost(Sprite):
    ghost  = [pg.image.load(f'images/redghost/rgr{n}.png') for n in range(1,3)]
    ghost2 = [pg.transform.rotozoom(pg.image.load(f'images/redghost/rgl{n}.png'), 0, 0.7) for n in range(1,3)]
        
    def __init__(self, game, pacman = None):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pg.transform.scale(pg.image.load('images/redghost/rgl1.png'), (30,30))
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.screen_rect = self.screen.get_rect()
        #self.sb = game.scoreboard
        self.vel = Vector()
        self.vel += self.settings.pac_speed * Vector(0,-1)
        #pacman.vel += settings.pac_speed * movement[key]
        self.posn = self.center_self()
        #self.timer = Timer(image_list=self.sprite_left)
        self.target = None
        self.sprite_up = [pg.transform.rotozoom(pg.image.load(f'images/redghost/rgu{n}.png'), 0, 0.7) for n in range(1,3)]
        self.sprite_down = [pg.transform.rotozoom(pg.image.load(f'images/redghost/rgd{n}.png'), 0, 0.7) for n in range(1,3)]
        self.sprite_right = [pg.transform.rotozoom(pg.image.load(f'images/redghost/rgr{n}.png'), 0, 0.7) for n in range(1,3)]
        self.sprite_left = [pg.transform.rotozoom(pg.image.load(f'images/redghost/rgl{n}.png'), 0, 0.7) for n in range(1,3)]
        self.pacman = pacman
        self.pacman_x = None
        self.pacman_y = None
        
        self.timer = Timer(image_list=self.sprite_left)

    def center_self(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        return Vector(self.rect.left-10, self.rect.top)

    def check_edges(self): 
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            self.vel = -self.vel
            self.update_direction()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            self.vel = -self.vel
            self.update_direction()
    
    def get_current_tile(self):
        x = min(self.rect.centerx // 32, 34)
        y = self.rect.centery// 32
        #print(f'ghost is on {x}, {y}')
        return x,y

    def get_neighboring_tiles(self, x, y, tiles):
        pass

    def update_direction(self):
        #Get neighbors
        #Find Pacman
        #Pick Best Direction
        if self.vel.x < 0:
            self.timer = Timer(image_list=self.sprite_left)
        elif self.vel.x > 0:
            self.timer = Timer(image_list=self.sprite_right)
    def update_direction_x(self):
        #Get neighbors
        x,y = self.get_current_tile()
        #Find Pacman
        #Pick Best Direction
        self.vel.x = random.choice([-1,1])
        if self.vel.x < 0:
            self.timer = Timer(image_list=self.sprite_left)
        elif self.vel.x > 0:
            self.timer = Timer(image_list=self.sprite_right)
    def update_direction_y(self):
        #Get neighbors
        #Find Pacman
        #Pick Best Direction
        self.vel.y = random.choice([-1,1])
        if self.vel.y < 0:
            self.timer = Timer(image_list=self.sprite_up)
        elif self.vel.y > 0:
            self.timer = Timer(image_list=self.sprite_down)           
            
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)
    
    def update(self,tiles):
        self.check_edges()
        hitx,hity = False,False
        x,y = self.get_current_tile()
        self.check_x_collisions(tiles)
        self.check_y_collisions(tiles)

        self.check_tunnel()
        #print(f'ghost is on {x}, {y}')
        # Did this update cause us to hit a wall?
        self.posn += self.vel 
        
        
        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()

    def tile_check(self, tiles):
        col = []
        for tile in tiles:
            if self.rect.colliderect(tile):
                col.append(tile)
        return col

    def check_x_collisions(self, tiles):
        collisions = self.tile_check(tiles)
        for tile in collisions:
            if self.vel.x > 0: # moving right
                self.vel.x = 0
                self.posn.x -= 2
            elif self.vel.x < 0: # moving left
                self.vel.x = 0
                self.posn.x += 2
            self.rect.x = self.posn.x
            self.update_direction_y()
            
                
    def check_y_collisions(self, tiles):
        collisions = self.tile_check(tiles)
        for tile in collisions:
            if self.vel.y > 0: # moving up
                self.vel.y = 0
                self.posn.y -= 2
            elif self.vel.y < 0: # moving down
                self.vel.y = 0
                self.posn.y += 2
            self.rect.y = self.posn.y
            self.update_direction_x()
    def check_tunnel(self):
        if self.vel.x > 0 and self.posn.x >= 1080:
            self.posn.x = 64
        if self.vel.x < 0 and self.posn.x <= 60:
            self.posn.x = 1080
    def check_pacman_collisions(self):
        collisions = self.rect.colliderect(self.pacman)
        if collisions:
            print("I ATE PAC")
            self.pacman.hit()


class Blinky(Ghost):
    def __init__(self, game, pacman):
        Ghost.__init__(self,game, pacman)
        
        self.sprite_up = [pg.transform.scale(pg.image.load(f'images/redghost/rgu{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_down = [pg.transform.scale(pg.image.load(f'images/redghost/rgd{n}.png'),(30, 30)) for n in range(1,3)]
        self.sprite_right = [pg.transform.scale(pg.image.load(f'images/redghost/rgr{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_left = [pg.transform.scale(pg.image.load(f'images/redghost/rgl{n}.png'), (30, 30)) for n in range(1,3)]

        self.timer = Timer(image_list=self.sprite_left)

class Inky(Ghost):
    def __init__(self, game, pacman):
        Ghost.__init__(self,game, pacman)
        
        self.sprite_up = [pg.transform.scale(pg.image.load(f'images/blueghost/bgu{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_down = [pg.transform.scale(pg.image.load(f'images/blueghost/bgd{n}.png'),(30, 30)) for n in range(1,3)]
        self.sprite_right = [pg.transform.scale(pg.image.load(f'images/blueghost/bgr{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_left = [pg.transform.scale(pg.image.load(f'images/blueghost/bgl{n}.png'), (30, 30)) for n in range(1,3)]

        self.timer = Timer(image_list=self.sprite_left)

class Pinky(Ghost):
    def __init__(self, game, pacman):
        Ghost.__init__(self,game, pacman)
        
        self.sprite_up = [pg.transform.scale(pg.image.load(f'images/greenghost/ggu{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_down = [pg.transform.scale(pg.image.load(f'images/greenghost/ggd{n}.png'),(30, 30)) for n in range(1,3)]
        self.sprite_right = [pg.transform.scale(pg.image.load(f'images/greenghost/ggr{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_left = [pg.transform.scale(pg.image.load(f'images/greenghost/ggl{n}.png'), (30, 30)) for n in range(1,3)]

        self.timer = Timer(image_list=self.sprite_left)

class Clyde(Ghost):
    def __init__(self, game, pacman):
        Ghost.__init__(self,game, pacman)
        
        self.sprite_up = [pg.transform.scale(pg.image.load(f'images/purpleghost/pgu{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_down = [pg.transform.scale(pg.image.load(f'images/purpleghost/pgd{n}.png'),(30, 30)) for n in range(1,3)]
        self.sprite_right = [pg.transform.scale(pg.image.load(f'images/purpleghost/pgr{n}.png'), (30, 30)) for n in range(1,3)]
        self.sprite_left = [pg.transform.scale(pg.image.load(f'images/purpleghost/pgl{n}.png'), (30, 30)) for n in range(1,3)]

        self.timer = Timer(image_list=self.sprite_left)

class GhostController():
    def __init__(self,game, pacman):
        self.pacman = pacman
        self.blinky = Blinky(game,pacman)
        self.pinky = Pinky(game,pacman)
        self.inky = Inky(game,pacman)
        self.clyde = Clyde(game,pacman)
        self.ghost_group = [self.blinky, self.pinky, self.inky, self.clyde]

    def update(self,tiles):
        for ghost in self.ghost_group:
            ghost.check_pacman_collisions()
            ghost.update(tiles)
