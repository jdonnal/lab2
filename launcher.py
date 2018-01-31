import pygame
import numpy as np
from colors import *

MAX_ANGLE = 90
MIN_ANGLE = 0
MAX_MAG = 100
MIN_MAG = 10

class Launcher:
  def __init__(self,x,y):
      self.x = x
      self.y = y
      self.angle = 0
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
          
  def draw(self,surf):
      #figure out dx and dy from polar coords
      dx = self.mag*np.cos(self.angle*np.pi/180)
      dy = self.mag*np.sin(self.angle*np.pi/180)
      
      pygame.draw.aaline(surf, self.color,
                       (self.x,self.y),
                       (self.x+dx, self.y-dy),
                       self.width)
