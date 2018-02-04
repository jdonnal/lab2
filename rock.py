import pygame
from colors import *

G = 10 # accel due to gravity
ROCK_SIZE = 10

class Rock:
    def __init__(self,x,y):
        self.moveTo(x,y)
        
    def move(self, dt):
        self.x += self.v_x*dt
        if(self.v_y!=0):
            self.v_y += G*dt
        self.y += self.v_y*dt

    def moveTo(self, x, y):
        self.x = x
        self.y = y
        self.v_x = 0
        self.v_y = 0
        
    def getRect(self):
        r = pygame.Rect((0,0,ROCK_SIZE,ROCK_SIZE))
        r.center = (self.x, self.y)
        return r

    def isMoving(self):
        return not ((self.v_x==0) and (self.v_y==0))
    
    def draw(self, surf):
        r = pygame.Rect((0,0,ROCK_SIZE,ROCK_SIZE))
        r.center = (self.x, self.y)
        pygame.draw.rect(surf, ROCK_COLOR, r)
