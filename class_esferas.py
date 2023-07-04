import pygame
import random
from utilidades import *




class Esferas(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, path_img, ancho, alto) -> None:
        self.image = pygame.image.load(path_img)
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.x = x
        self.rect.y = y
        self.gravity_vel_y = 0
        self.dy = 0
        self.dx = 0

    def add_gravity(self):
        #char representa a cualquier tipo de personaje
        #velocidad de caida final = 10
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)


        
        


       