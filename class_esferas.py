import pygame
import random
from utilidades import *
from class_personaje import Personaje



class Esferas(pygame.sprite.Sprite):
    def __init__(self, screen, x, y, path_img, ancho, alto, id_propia) -> None:
        self.image = pygame.image.load(path_img)
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.x = x
        self.rect.y = y
        self.gravity_vel_y = 0
        self.dy = 0
        self.dx = 0
        self.score = 1000
        self.id = id_propia
        self.return_ID = None
        self.sonido = pygame.mixer.Sound("sonido\item.wav")
    def add_gravity(self):
        #char representa a cualquier tipo de personaje
        #velocidad de caida final = 10
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

    def update(self,screen, personaje: Personaje):
        self.draw(screen)
        self.colison_personaje(personaje)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def colison_personaje(self, personaje: Personaje):
            if self.rect.colliderect(personaje.rect):
                self.return_ID = self.id
                print(self.return_ID)
                self.sound()
                self.get_score(personaje)

    def sound(self):
        self.sonido.set_volume(0.5)
        self.sonido.play()

    def get_score(self, pesonaje:Personaje):
        pesonaje.score += self.score
        


       