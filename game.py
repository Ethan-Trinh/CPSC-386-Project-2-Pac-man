#Running Page
import sys
import pygame as pg
from settings import Settings
from pacman import Pacman
import game_functions as gf
from maze import Maze
from points import Points
from spritesheet import Spritesheet
from timer import Timer
from sound import Sounds
import time
from scoreboard import Scoreboard

class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Portal Pacman")
        self.pacman = Pacman(settings=self.settings, screen=self.screen)
        self.scoreboard = Scoreboard(self)
        
        self.test_maze = Maze('test_level.csv', Spritesheet("images/PacmanWalls.png"))
        self.reg_points = Points('test_level.csv', self)
        self.sound = Sounds()
        self.intro_sounds = intro_sounds = pg.mixer.Channel(0)


    def game_intro(self):

        self.intro_sounds.play(self.sound.intro_screen_music)
         # set colors
        intro_images = [pg.image.load(f'images/intro/intro_{n}.png') for n in range(0, 97)]
        timer = Timer(image_list=intro_images)
        color = (0,0,0)
        white= (250,250,250) 
        yellow= (255,255,0)
        blue = (0,0,255)
        # light shade of the button 
        color_light = (255,0,230)
        # dark shade of the button 
        color_dark = (0,0,255)
        # stores the width of the 
        # screen into a variable 
        width = self.screen.get_width() 
        # stores the height of the 
        # screen into a variable 
        height = self.screen.get_height() 
        # defining a font 
        smallfont = pg.font.SysFont('Corbel',35)
        smallerfont = pg.font.SysFont('Corbel', 30 )
        largefont=pg.font.Font('fonts/space_invaders.ttf', 70)
        titlefont = pg.font.Font('fonts/PAC-FONT.ttf', 90)
        subtitlefont = pg.font.Font('fonts/PAC-FONT.ttf', 50)
        smallspacefont=pg.font.Font('fonts/space_invaders.ttf', 35)
        small_titlefont = pg.font.Font('fonts/Gloomy Things.ttf', 90)
        large_titlefont = pg.font.Font('fonts/Gloomy Things.ttf', 150)
        point_values = pg.font.Font('fonts/space_invaders.ttf',30) 
        with open('high_scores.txt','r+') as file:
                high_score = file.read()  
        # rendering a text written in 
        # this font
        #Words
        quit = smallfont.render('quit' , True , color) 
        play = smallfont.render('play' , True , color)
        highscores = smallerfont.render('high scores', True, color)
        pacman_text = titlefont.render('PaCmAn', True, yellow )
        portal_text = subtitlefont.render('pOrTaL', True, blue)
      

        #for button interaction
        while True: 
            image = timer.image()
            image_rect = image.get_rect()
            
            for ev in pg.event.get(): 
                if ev.type == pg.QUIT: 
                    pg.quit() 
            #checks if a mouse is clicked 
                if ev.type == pg.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated 
                    if width/2 <= mouse[0] <= width/2+140 and height/2+(height/4) <= mouse[1] <= height/2+40+(height/4): 
                        pg.quit() 
                    elif width/2-140 <= mouse[0] <= width/2 and (height/2)+(height/4) <= mouse[1] <= (height/2)+40+(height/4):
                        # quits atm
                        self.intro_sounds.stop()
                        self.play()
                    elif width/2-100 <= mouse[0] <= width/2+40 and height/2+(height/3) <= mouse[1] <= height/2+40+(height/3):
                        self.screen.fill(self.settings.bg_color)
                        self.high_scores_menu()
        # fills the screen with a color 
            self.screen.fill((0,0,0)) 
            #self.screen.blit((0,0))
      
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
            mouse = pg.mouse.get_pos() 
        # if mouse is hovered on a button it 
         # changes to lighter shade 
            if width/2 <= mouse[0] <= width/2+140 and height/2+(height/4) <= mouse[1] <= height/2+40+(height/4): 
                pg.draw.rect(self.screen,color_light,[width/2,height/2+(height/4),140,40])
            elif width/2-180 <= mouse[0] <= width/2+40 and (height/2)+(height/4) <= mouse[1] <= height/2+40+(height/4): 
                pg.draw.rect(self.screen,color_light,[width/2-180,(height/2)+(height/4),140,40])
            elif width/2-100 <= mouse[0] <= width/2+40 and height/2+height/3 <= mouse[1] <= height/2+40+height/3:
                 pg.draw.rect(self.screen,color_light,[width/2-100,(height/2+height/3),140,40])
            else: 
                pg.draw.rect(self.screen,color_dark,[width/2,height/2+(height/4),140,40])
                pg.draw.rect(self.screen,color_dark,[width/2-180,(height/2)+(height/4),140,40])
                pg.draw.rect(self.screen,color_dark,[width/2-100,height/2+height/3, 140,40])
           
        # superimposing the text onto our button 
            self.screen.blit(quit , (width/2+40,height/2+(height/4)))
            self.screen.blit(play,(width/2+-140,height/2+(height/4)))
            self.screen.blit(highscores,(width/2-100, height/2+height/3))
            scaled_image = pg.transform.scale(image, (1200,400))
            self.screen.blit(scaled_image, (0, height/4))
        #adding title
            self.screen.blit(pacman_text,(width/2-270,100))
            self.screen.blit(portal_text,(width/2-160, 180))
        # updates the frames of the game 
            pg.display.update() 
        
    def high_scores_menu(self):
        pg.display.flip()
        self.screen.fill((0,0,0))
        scorefont = pg.font.Font('fonts/scorefont.ttf', 70)
        titlefont = pg.font.Font('fonts/PAC-FONT.ttf', 70)
        yellow= (255,255,0)
        blue = (0,0,255)
        # light shade of the button 
        color_light = (255,0,230)
        # dark shade of the button 
        color_dark = (0,0,255)
        color = (0,0,0)
        width = self.screen.get_width()
        height = self.screen.get_height()
        score_width = width/2 -100
        start_height = height/6
        old_high_scores = []
        smallfont = pg.font.SysFont('Corbel',35)
        quit = smallfont.render('quit' , True , color) 
        play = smallfont.render('play' , True , color)
        title = titlefont.render('HIGH SCORES', True,blue)
        with open('high_scores.txt') as file:
            while (line := file.readline().rstrip()):
                old_high_scores.append(line)
        for item in range(len(old_high_scores)):
            high_score_text = scorefont.render(old_high_scores[item], True, yellow)
            self.screen.blit(high_score_text,(score_width,start_height))
            start_height += 50
        mouse = pg.mouse.get_pos() 
        while True:
            for ev in pg.event.get(): 
                if ev.type == pg.QUIT: 
                    pg.quit() 
            #checks if a mouse is clicked 
                if ev.type == pg.MOUSEBUTTONDOWN: 
            #if the mouse is clicked on the 
            # button the game is terminated 
                    if width/2 <= mouse[0] <= width/2+140 and height/2+(height/4)+60 <= mouse[1] <= height/2+40+(height/4)+60: 
                        pg.quit() 
                    elif width/2-140 <= mouse[0] <= width/2 and (height/2)+(height/4)+60 <= mouse[1] <= (height/2)+40+(height/4)+60:
                        # quits atm
                        self.intro_sounds.stop()
                        self.play()
            mouse = pg.mouse.get_pos()
            if width/2 <= mouse[0] <= width/2+140 and height/2+(height/4)+60 <= mouse[1] <= height/2+40+(height/4)+60: 
                pg.draw.rect(self.screen,color_light,[width/2,height/2+(height/4)+60,140,40])
            elif width/2-180 <= mouse[0] <= width/2+40 and (height/2)+(height/4)+60 <= mouse[1] <= height/2+40+(height/4)+60: 
                pg.draw.rect(self.screen,color_light,[width/2-180,(height/2)+(height/4)+60,140,40])
            else: 
                pg.draw.rect(self.screen,color_dark,[width/2,height/2+(height/4)+60,140,40])
                pg.draw.rect(self.screen,color_dark,[width/2-180,(height/2)+(height/4)+60,140,40])
                
            self.screen.blit(quit , (width/2+40,height/2+(height/4)+60))
            self.screen.blit(play,(width/2+-140,height/2+(height/4)+60))
            self.screen.blit(title,(width/2-310,height/2-380))
            pg.display.update()
        
        
    def reset(self):
        pass


    def game_over(self):
        self.reset()
        self.high_scores_menu()


    def play(self):
        # Draw the Screen before the game begins
        self.screen.fill(self.settings.bg_color)
        self.test_maze.draw(self.screen)
        self.reg_points.draw(self.screen)
        self.pacman.draw()
        pg.display.flip()

        self.sound.start_sound()
        time.sleep(4)
        while True:
            self.sound.play_bgm()
            gf.check_events(settings=self.settings, pacman = self.pacman)
            self.screen.fill(self.settings.bg_color)
            self.test_maze.draw(self.screen)
            self.reg_points.draw(self.screen)
            self.reg_points.update()
            self.pacman.update(tiles=self.test_maze.tiles, reg_points=self.reg_points.reg_points)
            self.scoreboard.update()
            # print(self.reg_points.level)
            pg.display.flip()



def main():
    g = Game()
    g.game_intro()


if __name__ == '__main__':
    main()