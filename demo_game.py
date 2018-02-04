#!/usr/bin/python

import pygame,sys
import random
import launcher
import target
import rock
from pygame.locals import *
from colors import *
import time

HEIGHT=400
WIDTH=500
FPS = 3
TARGET_WIDTH = 30

def main():
    pygame.init()
    fpsClock=pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    pygame.display.set_caption('Launchr')
    my_launcher = launcher.Launcher(0,HEIGHT-20)
    my_rock = rock.Rock(0,HEIGHT-20)
    my_target = target.Target(random.random()*WIDTH, HEIGHT-20,
                              TARGET_WIDTH)
    objs = [my_launcher, my_rock, my_target]
    while(True):
        # 1 Process Events
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
                if event.key == pygame.K_a:
                    my_target.moveTo(random.random()*WIDTH)
                if (event.key == pygame.K_SPACE) and not my_rock.isMoving():
                    my_launcher.fire(my_rock)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 2 Update Game State
        my_rock.move(1.0/FPS)
        if(my_rock.y>HEIGHT):
            my_rock.moveTo(0,HEIGHT-20)
            displayMessage(window,"Miss!")
        if(my_target.hitBy(my_rock.getRect())):
           my_rock.moveTo(0,HEIGHT-20)
           displayMessage(window,"Hit!")
           my_target.moveTo(random.random()*WIDTH)

        # 3 Update Display
        drawWorld(window)
        for obj in objs:
            obj.draw(window)
        pygame.display.update()
        fpsClock.tick(FPS)
        
    
def drawWorld(surf):
    surf.fill(SKY_BLUE)
    grass_rect=(0,HEIGHT-20,WIDTH,20)
    pygame.draw.rect(surf,GRASS_GREEN,grass_rect)
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render('Launchr 1.0',
                                    True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,20)
    surf.blit(textSurfaceObj,textRectObj)

def displayMessage(surf, msg):
    fontObj = pygame.font.Font('freesansbold.ttf',40)
    textSurfaceObj = fontObj.render(msg,
                                    True, ORANGE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,HEIGHT/2)
    surf.blit(textSurfaceObj,textRectObj)
    pygame.display.update()
    time.sleep(1)
           
if __name__=="__main__":
    main()
