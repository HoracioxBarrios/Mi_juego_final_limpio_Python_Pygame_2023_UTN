from utilidades import *

class Proyectil:
    def __init__(self, orientacion_x_char, pos_char_x, pos_char_y) -> None:
        self.damage = 1
        self.vel_y = 0
        self.vel_x = 5
        self.frame = 0
        self.orientacion_x_char = orientacion_x_char
        self.imagen_r = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, False)
        self.imagen_l = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, True)
        self.explocion = get_surface_form_sprite_sheet('asset\poder_colision_enemigo\sprite_explocion.png', 5, 1, 0, 0, 4, True)
        self.animacion = self.imagen_r
        self.image = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.ancho_imagen = self.image.get_width()
        self.alto_imagen = self.image.get_height()
        self.rect = self.image.get_rect()
        self.desplazamiento_x = 10
        self.dx = 0
        self.rect.x = pos_char_x
        self.rect.y = pos_char_y
        self.proyectil_en_aire = False

        self.limites_frames_por_segundo = 10
        self.time_frame = 10
    def update(self):
        self.dx = self.desplazamiento_x
        self.verificar_frames()
        print(self.proyectil_en_aire)
        self.rect.x += self.dx
    def start_proyectile(self):
        if(self.orientacion_x_char):
            self.animacion = self.imagen_r
        else:
            self.animacion = self.imagen_l
    def draw_proyectil(self, screen, orientacion_personaje_x):
        if self.proyectil_en_aire:
            if self.rect.x < screen.get_width() and orientacion_personaje_x == 1:
                self.cambiar_animacion(self.imagen_r)
            # elif self.rect.x <= 0 and orientacion_personaje_x == -1:
            #     screen.blit(self.image, self.rect)
            #     self.cambiar_animacion(self.imagen_r)
            elif(self.rect.x > screen.get_width()):
                self.proyectil_en_aire = False
            screen.blit(self.image, self.rect)
            
    def set_animacion(self, num_frame):
        self.frame = num_frame
                
    def verificar_frames(self):
        if(self.time_frame <= 0):
            if(self.frame < len(self.animacion)):
                self.image = self.animacion[self.frame]
                self.time_frame = self.limites_frames_por_segundo
                self.frame += 1
            else:
                self.frame = 0
        else:
            self.time_frame -= 1

    def cambiar_animacion(self, nueva_lista_animaciones: list[pygame.Rect]):
        self.animacion = nueva_lista_animaciones

            