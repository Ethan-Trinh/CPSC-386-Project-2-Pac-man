#Running Page
import sys
import pygame as pg
from settings import Settings



class Game:
    def __init__(self):
        pg.init()
        self.settings = Settings()
        size = self.settings.screen_width, self.settings.screen_height   # tuple
        self.screen = pg.display.set_mode(size=size)
        pg.display.set_caption("Portal Pacman")


    def game_intro(self):
        #self.sound.play_bg()
         # set colors
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
        pacman_text = titlefont.render('PaCmAn', True, yellow )
        portal_text = subtitlefont.render('pOrTaL', True, blue)
        #point values
        #images

        #for button interaction
        while True: 
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
                        self.play()
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
            else: 
                pg.draw.rect(self.screen,color_dark,[width/2,height/2+(height/4),140,40])
                pg.draw.rect(self.screen,color_dark,[width/2-180,(height/2)+(height/4),140,40])
           
        # superimposing the text onto our button 
            self.screen.blit(quit , (width/2+40,height/2+(height/4)))
            self.screen.blit(play,(width/2+-140,height/2+(height/4)))
        #adding title
            self.screen.blit(pacman_text,(width/2-270,100))
            self.screen.blit(portal_text,(width/2-160, 180))
        # updates the frames of the game 
            pg.display.update() 
        
        
    def reset(self):
        pass
    def game_over(self):
        pass
    def play(self):
        print("Going to change screens")
        while True:
            self.screen.fill(self.settings.bg_color)
            pg.display.flip()
            print("Are we different?")






def main():

    g = Game()
    g.game_intro()


if __name__ == '__main__':
    main()