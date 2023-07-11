import pygame
from class_personaje import Personaje
class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('asset\jack_chun.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vida = 5000
        self.esta_muerto = False

    def update(self, screen, personaje: Personaje, fn: any, path, credits_finished):
        self.draw(screen)
        self.colison_personaje(personaje, fn, path, screen, credits_finished)
    def draw(self, screen):
        screen.blit(self.image, self.rect)  
    def cambiar_imagen(self, screen):
        self.image = pygame.image.load('asset/7_esferas.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = (screen.get_height() / 2 )+ 200 

    def colison_personaje(self, personaje: Personaje,fn, path, screen,  credits_finished: bool):
        if self.rect.colliderect(personaje.rect) and not credits_finished:
            game_over_win = fn(screen, path)
            if game_over_win:
                self.esta_muerto = True
                personaje.score += 1