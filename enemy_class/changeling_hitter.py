import pygame
import time
import sys
import os
from . import enemy

class Changeling_Hitter(enemy.Enemy):
    surface=[]
    enemy_image=pygame.image.load(os.path.join('./image\changeling.png'))
    surface.append(enemy_image.subsurface(pygame.Rect(0,150,50,50)))
    surface.append(enemy_image.subsurface(pygame.Rect(0,100,50,50)))
    surface.append(enemy_image.subsurface(pygame.Rect(0,50,50,50)))
    surface.append(enemy_image.subsurface(pygame.Rect(0,0,50,50)))
    velocity = 8

    def __init__(self,screen,position):
        enemy.Enemy.__init__(self,screen,self.surface[0],position,self.velocity)