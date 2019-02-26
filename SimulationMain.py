
import pygame as py
import Variables as v
import Humans as h
import Storm as s
import random


black = 0,0,0

clock = py.time.Clock()

worldMap = py.image.load('Map.png')
worldMap = py.transform.scale(worldMap,((v.width - 10), (v.width - 10)//2))



def main():

    global screen
    

    
    
    py.init()
    screen = py.display.set_mode(v.dimensions)
    screen.fill(v.background)
    py.display.set_caption("Wolf Sheep Simulator")
    time = 0
    
    
    while 1:
        
        for event in py.event.get():
            pass
        
        
        
        
        
        screen.blit(worldMap,(5,5))
        
        
        
        
        if  time == 0:
            for x in range(v.width):
                for y in range(v.height):
                    color = screen.get_at((x, y))
                    if color != (v.background + (255,)):
                        for i in range(4):
                            a = x + ((3//(i+2)) * (-1)**i)
                            b = y + ((i//2) * (-1)**i)
                            color = screen.get_at((a, b))
                            if color == (v.background + (255,)):
                                v.outlineList.append((x,y))
                                break
                            elif i == 3:
                                Human = h.human((x,y))
                                v.humanList.append(Human)
                        
        

        for point in v.outlineList:
            py.draw.circle(screen, black, point,1)
            
         
        for Human in v.humanList:
            h.human.draw(Human,screen)            
        
#         for i in range(1000):
#             a = random.randint(0,len(v.humanList)-1)
#             Human = v.humanList[a]
#             v.updateList.append(Human.pos)
#             Human.alive = False
#         for i in range(500):
#             a = random.randint(0,len(v.humanList)-1)
#             Human = v.humanList[a]
#             v.humanUpdateList.append(Human.pos)
#             Human.alive = True
        
        
        
        if time%10 == 0:
            x = random.randint(0,v.width)
            y = random.randint(0,v.width//2)
            color = screen.get_at((x, y))
            while color != (v.background + (255,)):
                x = random.randint(0,v.width)
                y = random.randint(0,v.width//2)
                color = screen.get_at((x, y))
            size = random.randint(1,5)
            Hurricane = s.storm((x,y),'hurricane',size)            
            
            v.stormList.append(Hurricane)
            
        for Hurricane in v.stormList:
            s.storm.move(Hurricane)
            s.storm.draw(Hurricane,screen)
        
#         for Hurricane in v.stormList:
#             if Hurricane.size == 0:
#                 v.stormList.remove(Hurricane)
        for kill in v.removeList:
            v.stormList.remove(kill)
        v.removeList = []
           
        if time == 0:
            py.display.flip()
        else:
            update()
#         py.display.flip()
        
        screen.fill(v.background)
                
                
        time += 1
         
        
        
        clock.tick(v.maxFPS)


def update():
    
    
    for i in range(len(v.updateList)):
        x,y = v.updateList[i]
        point = x-1,y-1
        rect = py.Rect(point,(2,2))

        v.updateList[i] = rect
    
    for hurricane in v.stormList:
        
        (x,y) = hurricane.pos
        rect = py.Rect((x-hurricane.size,y-hurricane.size),(hurricane.size*2,hurricane.size*2))
        v.updateList.append(rect)
     
    py.display.update(v.updateList)
    v.updateList = []

    





  
    
    
    
    
main()

# this line does not affect the code :)
# neither does this one :D
# and this one ;)
# same with this one ;D
# and this one too :o
# and also this one :O
# this one doesnt affect the code either ._.
# this is spam this is spam this is spam this is spam this is spam this is spam
