import pygame
import time
import sys
import os

class Enemy(pygame.sprite.Sprite):
    def __init__(self,screen,enemy_surface,enemy_init_pos,velocity):
        pygame.sprite.Sprite.__init__(self)
        self.image=enemy_surface
        self.down_index=0
        self.screen = screen
        
        self.rect=self.image.get_rect()
        self.rect.topleft=enemy_init_pos
        
        self.speed=velocity


    def update(self):
        self.rect.top+=self.speed
        if self.rect.top>self.screen.get_height():
            self.kill()