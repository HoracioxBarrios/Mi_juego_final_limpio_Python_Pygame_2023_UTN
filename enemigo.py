import pygame
from utilidades import *
class Enemigo(pygame.sprite.Sprite):  
    def __init__(self, pos_x, pos_y, lista_pisos) -> None:
        super().__init__()
        self.caminando_r = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, False)
        self.caminando_l = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, True)
        self.gravity_vel_y = 0
        self.frame = 5
        self.dy = 0
        self.dx = 0
        self.image = self.caminando_l[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.imagen_width = self.image.get_width()
        self.imagen_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.desplazamiento_x = 0

        self.lista_pisos = lista_pisos

    def add_gravity(self):
    #char representa a cualquier tipo de personaje
    #velocidad de caida final = 10
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.set_dy = self.gravity_vel_y

    def verificar_colision(self, lista_pisos):
        for piso in lista_pisos:
            if piso[1].colliderect(self.rect.x + self.dx, self.rect.y, self.imagen_width, self.imagen_height):
                self.dx = 0
                    
            if piso[1].colliderect(self.rect.x, self.rect.y + self.dy, self.imagen_width, self.imagen_height):
                if self.gravity_vel_y < 0:
                    self.dy = piso[1].bottom - self.rect.top
                    self.gravity_vel_y = 0
                elif self.gravity_vel_y >= 0:
                    self.dy = piso[1].top - self.rect.bottom
                    self.gravity_vel_y = 0
                    



    def update(self):
        self.dx = self.desplazamiento_x
        self.dy = 0

        self.add_gravity()
        self.verificar_colision(self.lista_pisos)

        self.rect.x += self.dx
        self.rect.y += self.dy



    def draw(self, screen):
        screen.blit(self.image, self.rect)
                
    @property
    def get_dy(self):
        return self.dy
    
    @property
    def get_dx(self):
        return self.dx
    @get_dy.setter
    def set_dy(self, nuevo_valor_y):
        self.dy = nuevo_valor_y
        self.rect.y += self.dy

    @get_dy.setter
    def set_dx(self, nuevo_valor_x):
        self.dx = nuevo_valor_x

    @property
    def get_rect(self):
        return self.rect
    @property
    def get_dx(self):
        return self.dx
    
    @property
    def get_width(self):
        return self.imagen_width
    @property
    def get_height(self):
        return self.imagen_height
    @property
    def get_gravity_vel_y(self):
        return self.gravity_vel_y
    @get_gravity_vel_y.setter
    def set_gravity_vel_y(self, nuevo_valor_gravedad):
        self.gravity_vel_y = nuevo_valor_gravedad
 