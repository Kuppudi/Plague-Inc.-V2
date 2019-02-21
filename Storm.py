
import pygame as py
import Variables as v

green = 0,255,0


class storm(object):
    
    
    def __init__(self,pos,stormType,size):
        
        self.pos = pos
        self.stormType = stormType
        self.size = size * 10
        
    
    def draw(self,screen):
        
        
        if self.stormType == 'hurricane':
            py.draw.circle(screen, green, self.pos, self.size)
    
    def move(self):
        
        (x,y) = self.pos
        self.pos = x+1,y-1
        self.size -= 1
#         if self.size < 0:
#             self.size = 0
        if self.size == 0:
            v.removeList.append(self)