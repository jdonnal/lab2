import pygame
import math
from colors import *

MAX_ANGLE = 90
MIN_ANGLE = 0
MAX_MAG = 100
MIN_MAG = 10
V_SCALE = 1

class Launcher:
  def __init__(self,x,y):
      self.x = x
      self.y = y
      self.angle = 45
      self.mag = 50
      self.width = 2
      self.color = LAUNCHER_COLOR

  def changeAngle(self,delta):
      self.angle+=delta
      if(self.angle<MIN_ANGLE):
          self.angle = MIN_ANGLE
      if(self.angle>MAX_ANGLE):
          self.angle = MAX_ANGLE

  def changeMag(self,delta):
      self.mag+=delta
      if(self.mag<MIN_MAG):
          self.mag = MIN_MAG
      if(self.mag>MAX_MAG):
          self.mag = MAX_MAG

  def fire(self, rock):
    rock.v_x = self.mag*math.cos(self.angle*math.pi/180)*V_SCALE
    rock.v_y = -1*self.mag*math.sin(self.angle*math.pi/180)*V_SCALE
      
  def draw(self,surf):
      #figure out dx and dy from polar coords
      dx = self.mag*math.cos(self.angle*math.pi/180)
      dy = self.mag*math.sin(self.angle*math.pi/180)
      
      pygame.draw.aaline(surf, self.color,
                       (self.x,self.y),
                       (self.x+dx, self.y-dy),
                       self.width)
