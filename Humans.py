
import pygame as py


red = 255,0,0
white = 255,255,255


class human(object):
    
    def __init__(self,pos):

        self.pos = pos
        self.alive = True
        
        
        
    def draw(self,screen):
        
        
        if self.alive == True:
            py.draw.circle(screen, red, self.pos,1)
        else:
            py.draw.circle(screen, white, self.pos,1)






