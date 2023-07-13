import pygame
from utilidades import *

class PoderFinalVid(pygame.sprite.Sprite):
    def __init__(self, pos_x : int, pos_y : int, screen : pygame.Surface)-> None:
        """
        Inicializa un objeto PoderFinalVid.

        Args:
            pos_x (int): La posición x del objeto.
            pos_y (int): La posición y del objeto.
            screen (Surface): La superficie de la pantalla en la que se dibujará el objeto.
        """
        super().__init__()
        self.lista_animacion = []
        self.frame = 0
        self.screen = screen
        for i in range(43):
            path_index = "asset/pelea_final_img/{0}.png".format(i)
            image = get_surface_form_sprite_sheet(path_index, 1, 1, 0, 0, 0, False)
            image = pygame.transform.scale(image[0], (1000, 650))
            self.lista_animacion.append(image)

        self.rect = self.lista_animacion[0].get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        
    def update(self)-> None:
        """
        Actualiza el objeto en cada fotograma.
        Recibe: None
        Devuelve: None
        """
        self.verificar_frames()
        self.draw()

    def draw(self)-> None:
        '''
        Dibuja el objeto en la pantalla.
        recibe . None
        Devuelve: None
        '''
        image = self.lista_animacion[self.frame]
        self.screen.blit(image, self.rect)
       
       
    def verificar_frames(self)-> None:
        """
        Verifica y actualiza el fotograma actual del objeto.
        Si se ha alcanzado el último fotograma, se reinicia el ciclo de animación.
        Recibe: None
        Devuelve: None
        """
        if(self.frame < len(self.lista_animacion) -1):
            self.frame += 1
        else:
            self.frame = 0


        
    