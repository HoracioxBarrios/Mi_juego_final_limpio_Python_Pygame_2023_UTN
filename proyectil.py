from utilidades import *

class Proyectil:
    def __init__(self, orientacion_x_char, pos_char_x, pos_char_y) -> None:
        self.damage = 1
        self.vel_y = 0
        self.vel_x = 5
        self.pos_x = pos_char_x
        self.pos_y = pos_char_y
        self.frame = 0
        self.orientacion_x_char = orientacion_x_char
        self.imagen_r = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, False)
        self.imagen_l = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, True)
        self.explocion = get_surface_form_sprite_sheet('asset\poder_colision_enemigo\sprite_explocion.png', 5, 1, 0, 0, 4, True)
        self.animacion_r = self.imagen_r
        self.animacion_l = self.imagen_l
        self.imagen_proyectil = self.animacion_r[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.ancho_imagen = self.imagen_proyectil.get_width()
        self.alto_imagen = self.imagen_proyectil.get_height()
        self.rectangulo_principal = self.imagen_proyectil.get_rect()
        self.rectangulo_principal.x = 0
        self.rectangulo_principal.y = 0

    def start_proyectile(self):
        if(self.orientacion_x_char):
            self.animacion = self.imagen_r
        else:
            self.animacion = self.imagen_l
    def draw_proyectil(self, screen):
        pass
    def set_animacion(self, num_frame):
        self.frame = num_frame
                

            