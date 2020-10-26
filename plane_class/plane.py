import pygame
import time
import sys
import os

class Plane(pygame.sprite.Sprite):
    '''
    基类plane类:共有数值和数据
    '''
    def __init__(self,plane_image,screen,plane_pos,health,speed):
        '''plane类_init'''
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image=plane_image[0]              #初始化plane图片

        self.rect=self.image.get_rect()     #Rect(left, top, width, height)
        self.rect.topleft=plane_pos         #初始化plane位置

        self.bullets=pygame.sprite.Group()
        self.bullet_spacing=0

        self.health = health
        self.speed = speed

    def move(self,offset):
        '''plane移动事件函数'''
        x=self.rect.left+offset[pygame.K_RIGHT]-offset[pygame.K_LEFT]
        y=self.rect.top+offset[pygame.K_DOWN]-offset[pygame.K_UP]
        if x<0:
            self.rect.left=0        #到达屏幕左端
        elif x >self.screen.get_width()-self.rect.width:
            self.rect.left=self.screen.get_width()-self.rect.width
        else:
            self.rect.left=x        #到达屏幕右端
    
        if y<0:
            self.rect.top=0         #到达屏幕上端
        elif y >self.screen.get_height()-self.rect.height:
            self.rect.top=self.screen.get_height()-self.rect.height
        else:
            self.rect.top=y         #到达屏幕下端
    
    def single_shoot(self,bullet_surface):
        bullet=Bullet(bullet_surface,self.rect.midtop)
        self.bullets.add(bullet)

    