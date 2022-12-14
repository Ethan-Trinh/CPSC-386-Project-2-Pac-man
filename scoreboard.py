import pygame as pg 
from fileinput import FileInput
import os
class Scoreboard:
    def __init__(self, game): 
        self.score = 0
        self.level = 0
        self.high_score = 0
        self.game = game
        self.pacman = self.game.pacman
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.text_color = (255,255,255)
        self.font = pg.font.SysFont(None, 48)

        self.score_image = None 
        self.score_rect = None
        self.bordertop_image = pg.image.load('images/border/boardertop.png')
        self.bordertop_rect = self.bordertop_image.get_rect()
        self.borderbottom_image = pg.image.load('images/border/boardertop.png')
        self.borderbottom_rect = self.borderbottom_image.get_rect()
        self.sideleft_image = pg.image.load('images/border/boarderside.png')
        self.sideleft_rect = self.sideleft_image.get_rect()
        self.sideright_image = pg.image.load('images/border/boarderside.png')
        self.sideright_rect = self.sideright_image.get_rect()
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.get_high_score()
        self.prep_score()
        

    def increment_score(self, points_added): 
        self.score += points_added
        self.prep_score()

    def prep_score(self): 
        score_str = str(self.score)
        self.score_image = self.font.render(score_str, True, self.text_color, (0,0,0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 750
   
        
    def reset(self): 
        self.add_high_score()
        self.score = 0
        self.update()

    def update(self): 
        # TODO: other stuff
        if self.score>self.high_score:
            self.high_score = self.score
        self.add_high_score()
        self.draw()

    def draw(self): 
        self.screen.blit(self.bordertop_image, (0,0))
        self.screen.blit(self.borderbottom_image, ( 0,735))
        self.screen.blit(self.borderbottom_image, ( 0,760))
        self.screen.blit(self.sideleft_image, (0,20))
        self.screen.blit(self.sideleft_image, (30,20))
        self.screen.blit(self.sideright_image, (1160,20))
        self.screen.blit(self.sideright_image, (1120,780))
        level = self.font.render('Level' , True , self.text_color) 
        self.screen.blit(level,(580,760))
        height = 760
        start_width = 20
        for item in range(self.pacman.lives):
            self.life = self.pacman.image_scaled
            self.screen.blit(self.life,(start_width,height))
            start_width +=40
        self.screen.blit(self.score_image, self.score_rect)
       
    def get_high_score(self):
        with open('high_scores.txt','r+') as file:
            lines = file.read()
            old_high_score = lines.split('\n', 1)[0]
            print(old_high_score)
            file.seek(0)
            if int(old_high_score)> self.high_score:
                self.high_score = int(old_high_score)
    def add_high_score(self):
        with open('high_scores.txt', 'r+') as file:
            lines = file.read()
            length= len(lines)
            old_high_score = lines.split('\n', 1)[0]
            if int(old_high_score)< self.high_score:
                file.seek(0,0)
                file.write(str(self.high_score)+"\n")
                file.write(lines)
                
  
