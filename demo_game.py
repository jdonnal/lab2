#!/usr/bin/python

import pygame,sys
import launcher
from pygame.locals import *
from colors import *

HEIGHT=400
WIDTH=500
FPS = 30

def main():
    pygame.init()
    fpsClock=pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    pygame.display.set_caption('Launchr')
    my_launcher = launcher.Launcher(0,HEIGHT-20)
    while(True):
        draw_world(window)    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    my_launcher.changeAngle(3)
                if event.key == pygame.K_DOWN:
                    my_launcher.changeAngle(-3)
                if event.key == pygame.K_RIGHT:
                    my_launcher.changeMag(5)
                if event.key == pygame.K_LEFT:
                    my_launcher.changeMag(-5)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        my_launcher.draw(window)
        pygame.display.update()        
        fpsClock.tick(FPS)
        
    
def draw_world(surf):
    surf.fill(SKY_BLUE)
    grass_rect=(0,HEIGHT-20,WIDTH,20)
    pygame.draw.rect(surf,GRASS_GREEN,grass_rect)
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render('Launchr 1.0',
                                    True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,20)
    surf.blit(textSurfaceObj,textRectObj)
    
if __name__=="__main__":
    main()
