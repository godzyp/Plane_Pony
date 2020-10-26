import pygame
import time
import sys
import os
from . import plane

class Twilight_Sparkle(plane.Plane):
    plane_surface=[]
    plane_image=pygame.image.load(os.path.join('./image\TS.png'))
    #plane_image = plane_image.convert_alpha()
    plane_surface.append(plane_image.subsurface(pygame.Rect(0,0,61,75)))
    plane_surface.append(plane_image.subsurface(pygame.Rect(0,75,61,75)))

    def __init__(self,screen,plane_pos):
        plane.Plane.__init__(self,self.plane_surface,screen,plane_pos,10,10)
        self.mana=6                     #MP
        self.mana_regeneration=1        #回蓝速度 /s
        self.level=1                    #level

    def skill_blink(self):
        x=self.rect.left+offset[pygame.K_RIGHT]*8-offset[pygame.K_LEFT]*8
        y=self.rect.top+offset[pygame.K_DOWN]*8-offset[pygame.K_UP]*8
        if x<0:
            self.rect.left=0#到达屏幕左端
        elif x >screen_width-self.rect.width:
            self.rect.left=screen_width-self.rect.width
        else:
            self.rect.left=x#到达屏幕右端
    
        if y<0:
            self.rect.top=0#到达屏幕上端
        elif y >screen_height-self.rect.height:
            self.rect.top=screen_height-self.rect.height
        else:
            self.rect.top=y#到达屏幕下端

    def update(self,offset):
        '''plane状态更新函数'''
        if offset[pygame.K_x]==1:
            self.skill_blink()
            offset[pygame.K_x]=0
        self.move(offset)
