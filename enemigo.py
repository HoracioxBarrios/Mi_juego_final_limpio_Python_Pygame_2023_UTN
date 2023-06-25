from utilidades import *

class Enemigo:
    def __init__(self, pos_x, pos_y, vida) -> None:
        self.damage = 10
        self.vida = vida
        self.vel_y = 0
        self.vel_x = 0
        self.pos_x = 0
        self.pos_y = 0
        self.frame = 0
        self.caminando_r = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, False)
        self.caminando_l = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, True)
        self.animacion_r = self.caminando_r
        self.animacion_l = self.caminando_l
        self.imagen_enemigo = self.animacion_r[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.ancho_imagen = self.imagen_enemigo.get_width()
        self.alto_imagen = self.imagen_enemigo.get_height()
        self.rectangulo_principal = self.imagen_enemigo.get_rect()
        self.rectangulo_principal.x = pos_x
        self.rectangulo_principal.y = pos_y

    def set_damage(self, damage):
        self.vida -= damage
    def set_vida(self, vida):
        self.vida = vida
                
    def get_vida(self):
        return self.vida
    
    def
            