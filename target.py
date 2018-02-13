import pygame
from colors import *

HEIGHT = 10

class Target:
    def __init__(self,x,y,w):
        self.rect =  pygame.Rect((0,y,w,HEIGHT))
        self.rect.centerx = x
        
    def hitBy(self,rect):
        return self.rect.colliderect(rect)
        
    def draw(self,surf):
        pygame.draw.rect(surf, TARGET_COLOR, self.rect)

