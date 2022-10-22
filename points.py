import pygame as pg 
import csv, os
from pygame.sprite import Sprite, Group
from spritesheet import Spritesheet
from pacman import Pacman

class PointTile(Sprite):
    def __init__(self, image, x, y, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.type = type
        self.eaten = False
    
    def draw(self, surface):
        if self.type != 0:
            surface.blit(self.image, (self.rect.x, self.rect.y))
            
    def get_type(self):
        return self.type
        
    def collected(self):
        print("nom nom")
        self.eaten = True
        
    def update(self):
        if self.eaten != True:
            self.draw()
        
class Points():
    def __init__(self, filename, game):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.reg_points = self.load_reg_points(filename)
        self.all_points = Group()
        self.map_surface = pg.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.pacman = game.pacman 
        self.load_map()
              
    def draw(self, screen):
        for point in self.all_points.sprites():
            point.draw(screen)
        
    def load_map(self):
        for reg in self.reg_points:
            reg.draw(self.map_surface)
            self.all_points.add(reg)
            
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_reg_points(self, filename):
        reg_points = []
        map = self.read_csv(filename)
        x, y = 1, 0
        for row in map:
            x = 1
            for tile in row:
                if tile == '-1':
                    reg_points.append(PointTile(pg.transform.rotozoom(pg.image.load('images/food/dots.png'), 0, .1), x * self.tile_size, y * self.tile_size, 1))    
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return reg_points
    
    def check_collect(self):
        col = pg.sprite.spritecollide(self.pacman, self.all_points, False)
        if col:
            for point in col:
                point.collected()
                if point.kill():
                    print()
        
    def update(self):
        self.check_collect()