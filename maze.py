import pygame as pg 
import csv, os
from pygame.sprite import Sprite
from spritesheet import Spritesheet

wall_spritesheet = Spritesheet('images/PacmanWalls.png')
a_wall = wall_spritesheet.get_sprite(0, 0, 32, 32)

class MazeTile(Sprite):
    def __init__(self, image, x, y, spritesheet):
        self.image = spritesheet.parse_sprite(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        
    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
        
class Maze():
    def __init__(self, filename, spritesheet):
        self.tile_size = 32
        self.start_x, self.start_y = 0, 0
        self.spritesheet = spritesheet
        self.tiles = self.load_tiles(filename)
        self.map_surface = pg.Surface((self.map_w, self.map_h))
        self.map_surface.set_colorkey((0, 0, 0))
        self.load_map()
      
    def draw(self, screen):
        screen.blit(self.map_surface, (0,0))
        
    def load_map(self):
        for tile in self.tiles:
            tile.draw(self.map_surface)
            
    def read_csv(self, filename):
        map = []
        with open(os.path.join(filename)) as data:
            data = csv.reader(data, delimiter=',')
            for row in data:
                map.append(list(row))
        return map
    
    def load_tiles(self, filename):
        tiles = []
        map = self.read_csv(filename)
        x, y = 1, 0
        for row in map:
            x = 1
            for tile in row:
                if tile == '0':
                    tiles.append(MazeTile('MC-bottomLeft.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '1':
                    tiles.append(MazeTile('MC-bottomRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '2':
                    tiles.append(MazeTile('MCS-bottomLeft.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '3':
                    tiles.append(MazeTile('MCS-bottomRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '4':
                    tiles.append(MazeTile('MCS-topLeft.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '5':
                    tiles.append(MazeTile('MCS-topRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '6':
                    tiles.append(MazeTile('MC-topLeft.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '7':
                    tiles.append(MazeTile('MC-topRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '8':
                    tiles.append(MazeTile('MHT-left-down.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '9':
                    tiles.append(MazeTile('MHT-left-right.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '10':
                    tiles.append(MazeTile('MHT-left-up.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '11':
                    tiles.append(MazeTile('MHT-right-down.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '12':
                    tiles.append(MazeTile('MHT-right-up.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '13':
                    tiles.append(MazeTile('MHT-up-down.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '14':
                    tiles.append(MazeTile('MTE-Down.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '15':
                    tiles.append(MazeTile('MTE-Left.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '16':
                    tiles.append(MazeTile('MTE-Right.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '17':
                    tiles.append(MazeTile('MTE-UP.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '18':
                    tiles.append(MazeTile('MW-DownRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '19':
                    tiles.append(MazeTile('MW-LeftUp.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '20':
                    tiles.append(MazeTile('MW-RightUp.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                elif tile == '21':
                    tiles.append(MazeTile('MW-UpRight.png', x * self.tile_size, y * self.tile_size, self.spritesheet))
                    
                x += 1
            y  += 1
        self.map_w, self.map_h = x * self.tile_size, y * self.tile_size
        return tiles