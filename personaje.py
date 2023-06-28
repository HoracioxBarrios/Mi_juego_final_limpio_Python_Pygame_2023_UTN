import pygame
from utilidades import *
class Personaje(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, lista_pisos):
        super().__init__()
        self.quieto_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, True)
        self.quieto_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, False)
        self.corriendo_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, False)
        self.corriendo_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, True)
        self.saltando_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, False)#para recortar una sola imagen, se ponen el desde y el hasta con el mismo valor
        self.saltando_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, True)
        self.shot_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, True)
        self.shot_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, False)
        self.gravity_vel_y = 0
        self.valocidad_caminar = 5
        self.desplazamiento_x = 0
        self.dy = 0
        self.dx = 0
        self.frame = 0
        self.animacion = self.quieto_r
        self.image = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.imagen_width = self.image.get_width()
        self.imagen_height = self.image.get_height()




        self.lista_pisos = lista_pisos


    def add_gravity(self):
        #char representa a cualquier tipo de personaje
        #velocidad de caida final = 10
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

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
        

        
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_RIGHT]):
            self.desplazamiento_x = self.valocidad_caminar
        elif(keys[pygame.K_LEFT]):
            self.desplazamiento_x = -self.valocidad_caminar
        else:
            self.desplazamiento_x = 0


        if(keys[pygame.K_SPACE]):
            self.gravity_vel_y = -5

    



    def draw(self, screen):
        screen.blit(self.image, self.rect_main)
    
    @property
    def get_dy(self):
        return self.dy
    
    @get_dy.setter
    def set_dy(self, nuevo_valor_y):
        self.dy = nuevo_valor_y
        self.rect.y += self.dy

    @property
    def get_dx(self):
        return self.dx
    
    @get_dx.setter
    def set_dx(self, nuevo_valor_x):
        self.dx = nuevo_valor_x
        self.rect.x = self.dx


    @property
    def get_rect(self):
        return self.rect
    
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

    
    


  
