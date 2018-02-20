#!/usr/bin/python

# import system modules
import pygame,sys
from pygame.locals import *
import random
import time
import serial

# import custom modules
import launcher
import target
import rock
from colors import *

# tunable constants
HEIGHT=400
WIDTH=500
FPS = 30
TARGET_WIDTH = 50

def main():
    # start up pygame and build a game window
    pygame.init()
    fpsClock=pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH,HEIGHT),0,32)
    pygame.display.set_caption('Launchr')
    s = serial.Serial("/dev/ttyACM1",timeout=0.5)
    # create custom objects
    my_launcher = launcher.Launcher(0,HEIGHT-20)
    my_rock = rock.Rock(0,HEIGHT-20)
    my_target = target.Target((random.random()*280)+50, HEIGHT-20,
                              TARGET_WIDTH)
    objs = [my_launcher, my_rock, my_target]

    # Main game loop
    while(True):
        # 1 Process Events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                """arduino controls launcher mag/angle
                if event.key == pygame.K_UP:
                    my_launcher.changeAngle(3)
                if event.key == pygame.K_DOWN:
                    my_launcher.changeAngle(-3)
                if event.key == pygame.K_RIGHT:
                    my_launcher.changeMag(5)
                if event.key == pygame.K_LEFT:
                    my_launcher.changeMag(-5)
                """
                if ((event.key == pygame.K_SPACE) and
                    not my_rock.isMoving()):
                    my_launcher.fire(my_rock)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # 2 Update Game State
        # read from arduino
        s.write('p')
        str_data = s.readline()
        if(len(str_data)>0):
            data = [int(x) for x in str_data.split(',')]
            my_launcher.setAngle((data[0]/1024.0)*90)
            my_launcher.setMag((data[1]/1024.0)*100)

        my_rock.move(1.0/FPS) # force floating point division
        if(my_rock.y>HEIGHT):
            # rock is below the screen
            my_rock.moveTo(0,HEIGHT-20)
            s.write('r')
            displayMessage(window,"Miss!")
        if(my_target.hitBy(my_rock.getRect())):
           # rock hit the target!
           my_rock.moveTo(0,HEIGHT-20)
           s.write('g')
           displayMessage(window,"Hit!")

        # 3 Update Display
        drawWorld(window)
        for obj in objs:
            obj.draw(window)
        pygame.display.update()
        fpsClock.tick(FPS)
        
    
def drawWorld(surf):
    # erase surface with a fill
    surf.fill(SKY_BLUE)
    # add in some grass
    grass_rect=(0,HEIGHT-20,WIDTH,20)
    pygame.draw.rect(surf,GRASS_GREEN,grass_rect)
    # write the game title
    fontObj = pygame.font.Font('freesansbold.ttf',32)
    textSurfaceObj = fontObj.render('Launchr 1.0',
                                    True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,20)
    surf.blit(textSurfaceObj,textRectObj)

def displayMessage(surf, msg):
    # display [msg] for 1 second (freezes the game)
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
