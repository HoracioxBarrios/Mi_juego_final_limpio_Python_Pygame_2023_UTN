import pygame
from utilidades import *

class PoderFinalVid(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, screen):
        super().__init__()
        self.lista_animacion = []
        self.frame = 0
        self.screen = screen
        for i in range(43):
            path_index = "asset/pelea_final_img/{0}.jpg".format(i)
            image = get_surface_form_sprite_sheet(path_index, 1, 1, 0, 0, 0, False)
            image = pygame.transform.scale(image[0], (1000, 650))
            self.lista_animacion.append(image)

        self.rect = self.lista_animacion[0].get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
    def update(self):
        self.verificar_frames()
        self.draw()

    def draw(self):
       image = self.lista_animacion[self.frame]
       self.screen.blit(image, self.rect)
    def verificar_frames(self):
        '''
        El personaje se moverá y se animará correctamente con respecto 
        al tiempo transcurrido, lo que resultará en un movimiento más suave 
        y consistente sin depender de la tasa de cuadros (FPS) del juego
        
        '''
        if(self.frame < len(self.lista_animacion) -1):
            self.frame += 1
        else:
            self.frame = 0


        
    