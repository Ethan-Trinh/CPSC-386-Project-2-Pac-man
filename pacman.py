import pygame as pg
from pygame.sprite import Sprite
from game_functions import check_keydown_events, clamp
from timer import Timer
from vector import Vector
from spritesheet import Spritesheet

class Pacman(Sprite):
    pacman_images = [pg.image.load(f'images/pacmaneat/pacman{n}.png') for n in range(1, 5)]
    pacman_death = [pg.image.load(f'images/pacmandie/pacmandie{n}.png') for n in range(1, 15)]

    def __init__(self, settings, screen):#, sound):
        super().__init__()
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #self.sound = sound
        self.lives = 3
        self.dying = False
        self.dead = False

        # Image / Animation Variables
        self.image = pg.image.load('images/pacmaneat/pacman1.png')
        self.image_scaled = pg.transform.scale(self.image, (40, 40))
        self.pacman_images_scaled = [pg.transform.scale(Pacman.pacman_images[n], (40, 40)) for n in range (0, 4)]
        self.rect = self.image_scaled.get_rect() # use grabbing points
        self.hitbox = self.rect # use for the ghosts and moving through the maze
        
        self.timer_normal = Timer(image_list=self.pacman_images_scaled)
        self.timer_death = Timer(image_list=Pacman.pacman_death, delay=100, is_loop=False)
        self.timer = self.timer_normal

        # Movement / Position Handling Variables
        self.posn = self.starting_point()
        self.vel = Vector()

    def starting_point(self):
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        return Vector(self.rect.left, self.rect.top)


    def hit(self):
        if not self.dying:
            print(f'Pac Man has been hit!')
            self.dying = True
            self.timer = self.timer_death

    def really_dead(self):
        self.lives -= 1
        print(f'Pac Man died, {self.lives} lives remaining')

    def reset(self):
        self.dying = False
        self.dead = False
        self.timer = self.timer_normal
        self.timer_death.reset()


    def update(self, tiles, reg_points):
        self.check_x_collisions(tiles)
        self.check_y_collisions(tiles)
        self.posn += self.vel
        self.posn, self.rect = clamp(self.posn, self.rect, self.settings)
        self.draw()
        # The hitbox is for pacman moving in the maze so he can be closer to the wall without
        # triggering collisions + so pacman and ghosts overlap before 
        self.hitbox.w = self.rect.w/2.9
        self.hitbox.h = self.rect.h/2.9
        self.hitbox.x = self.rect.x + self.rect.w/2.8
        self.hitbox.y = self.rect.y + self.rect.h/3
        # pg.draw.rect(surface = self.screen, color=(225,225,225), rect=self.hitbox)
        self.check_tunnel()
        
    def draw(self):
        image = self.timer.image()
        rect = image.get_rect()
        rect.left, rect.top = self.rect.left, self.rect.top
        self.screen.blit(image, rect)
    
    def tile_check(self, tiles):
        col = []
        for tile in tiles:
            if self.hitbox.colliderect(tile):
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

    def check_tunnel(self):
        if self.vel.x > 0 and self.posn.x >= 1080:
            self.posn.x = 64
        if self.vel.x < 0 and self.posn.x <= 60:
            self.posn.x = 1080