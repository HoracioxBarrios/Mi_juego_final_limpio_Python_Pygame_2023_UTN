from utilidades import *

class Proyectil:
    def __init__(self) -> None:
        self.danio = 10
        self.vel_y = 0
        self.vel_x = 5
        self.pos_x = 0
        self.pos_y = 0
        self.imagen_r = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, False)
        self.imagen_l = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, True)