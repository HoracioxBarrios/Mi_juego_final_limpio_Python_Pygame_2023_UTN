from utilidades import *

class Proyectil:
    def __init__(self, orientacion_x_char, pos_char_x, pos_char_y) -> None:
        self.damage = 10
        self.vel_y = 0
        self.vel_x = 5
        self.pos_x = pos_char_x
        self.pos_y = pos_char_y
        self.frame = 0
        self.orientacion_x_char = orientacion_x_char
        self.imagen_r = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, False)
        self.imagen_l = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, True)
        self.animacion = self.imagen_r
        self.imagen_proyectil = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.ancho_imagen = self.imagen_proyectil.get_width()
        self.alto_imagen = self.imagen_proyectil.get_height()
        self.rectangulo_principal = self.imagen_proyectil.get_rect()

    def start_proyectile(self):
        if(self.orientacion_x_char):
            self.animacion = self.imagen_r
        else:
            self.animacion = self.imagen_l
    def draw_proyectil(self, screen):
        pass
                

            