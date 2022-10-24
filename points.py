import pygame as pg 
import csv, os
from pygame.sprite import Sprite, Group
from spritesheet import Spritesheet
from random import randint

class PointTile(Sprite):
    def __init__(self, image, x, y, type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.type = type
        self.eaten = False

        
    
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
            
    def get_type(self):
        return self.type
        
    def collected(self, type):
        if type == 'reg':

            print("nom nom")
        elif type == 'pow':
            print("big nom nom")    
        elif type == 'fruit':
            print("sweet nom nom") 
        elif type == 'milkshake':
            print("delicious") 
        self.eaten = True
        
    def update(self):
        if self.eaten != True:
            self.draw()
        
class Points():
    def __init__(self, filename, game):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.reg_points = self.load_reg_points(filename)
        self.pow_points = self.load_power_points(filename)
        self.r_points = Group()
        self.p_points = Group()
        self.fruit = Group()
        self.milkshake = Group()
        self.map_surface = pg.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.pacman = game.pacman
        self.ghost_controller = game.ghost_controller 
        self.sb = game.scoreboard
        self.level = 1
        print(self.level)
        self.load_map()
              
    def draw(self, screen):
        for point in self.r_points.sprites():
            point.draw(screen)
        for p in self.p_points.sprites():
            p.draw(screen)
        for f in self.fruit.sprites():
            f.draw(screen)
        for m in self.milkshake.sprites():
            m.draw(screen)
        
    def load_map(self):
        for reg in self.reg_points:
            reg.draw(self.map_surface)
            self.r_points.add(reg)
        for pow in self.pow_points:
            pow.draw(self.map_surface)
            self.p_points.add(pow)
            
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
                    reg_points.append(PointTile(pg.transform.rotozoom(pg.image.load('images/food/dots.png'), 0, .1), (x * self.tile_size) + 8, (y * self.tile_size) + 8, 'reg'))    
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return reg_points
    
    def load_power_points(self, filename):
        power_points = []
        map = self.read_csv(filename)
        x, y = 1, 0
        for row in map:
            x = 1
            for tile in row:
                if tile == '-2':
                    power_points.append(PointTile(pg.transform.rotozoom(pg.image.load('images/food/powerdot.png'), 0, .1), (x * self.tile_size) + 8, (y * self.tile_size) + 8, 'pow'))    
                x += 1
            y += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return power_points    
    
    def reset(self):
        # empty the point arrays
        self.r_points.empty()
        self.p_points.empty()
        self.fruit.empty()
        self.milkshake.empty()
        # remake the map
        self.load_map()
        
        
    
    def fruit_spawn(self):
        spawn_chance = 500
        out_of = randint(0, 5000)
        if out_of % spawn_chance == 0:
            cherry = PointTile(pg.transform.rotozoom(pg.image.load('images/food/cherries.png'), 0, .15), (18 * self.tile_size) + 3, 16 * self.tile_size, 'fruit')
            self.fruit.add(cherry)
            for fruit in self.fruit:
                fruit.draw(self.map_surface)
        
    def milkshake_spawn(self):
        spawn_chance = 500
        out_of = randint(0, 5000)
        if out_of % spawn_chance == 0:
            shake = PointTile(pg.transform.rotozoom(pg.image.load('images/food/milkshake.png'), 0, .15), (18 * self.tile_size) + 3, 9 * self.tile_size, 'milkshake')
            self.milkshake.add(shake)
            for ms in self.milkshake:
                ms.draw(self.map_surface)
    
    def check_collect(self):
        col = pg.sprite.spritecollide(self.pacman, self.r_points, False)
        if col:
            for point in col:
                point.collected(point.type)
                self.sb.increment_score(10)
                self.pacman.sound.munch_sound()
                point.kill()
        col2 = pg.sprite.spritecollide(self.pacman, self.p_points, False)
        if col2:
            for point2 in col2:
                point2.collected(type = point2.type)
                self.sb.increment_score(50)
                self.ghost_controller.frightmode()
                self.pacman.sound.eat_power_sound()
                point2.kill()
        col3 = pg.sprite.spritecollide(self.pacman, self.fruit, False)
        if col3:
            for point3 in col3:
                point3.collected(type = point3.type)
                self.sb.increment_score(100)
                self.pacman.sound.eat_fruit_sound()
                point3.kill()
        col4 = pg.sprite.spritecollide(self.pacman, self.milkshake, False)
        if col4:
            for point4 in col4:
                point4.collected(type = point4.type)
                self.sb.increment_score(500)
                self.pacman.sound.eat_fruit_sound()
                point4.kill()
        
    def update(self):
        self.check_collect()
        if not self.fruit:
            self.fruit_spawn()
        if not self.milkshake:
            self.milkshake_spawn()
        # testing the reset
        if not self.p_points:
            self.reset()
            self.level += 1