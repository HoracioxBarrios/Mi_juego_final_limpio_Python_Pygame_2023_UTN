import pygame

class BarraVida:
    def __init__(self, screen : pygame.Surface, vida_maxima : int, ancho_bar : int, alto_bar: int, pos_x : int, pos_y : int)-> None:
        """
        Clase que representa una barra de vida en el juego.
        Recibe:
        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            vida_maxima (int): Valor máximo de vida.
            ancho_bar (int): Ancho de la barra de vida.
            alto_bar (int): Alto de la barra de vida.
            pos_x (int): Posición en el eje x de la barra de vida.
            pos_y (int): Posición en el eje y de la barra de vida.
        Devuelve: None
        """
        self.x = pos_x
        self.y = pos_y
        self.ancho = ancho_bar
        self.alto = alto_bar
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_maxima

        self.image = pygame.Surface((self.ancho, self.alto))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.screen = screen
        self.ancho_bar_2 = self.vida_actual * 100 / self.vida_maxima
        self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.x = pos_x
        self.rect_2.y = pos_y
        self.image_2.fill((0, 255, 0))
        

    def draw(self, screen : pygame.Surface)-> None:
        """
        Dibuja la barra de vida en la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.

        Devuelve:   None
        """
        screen.blit(self.image, self.rect)# rojo - barra de atras
        screen.blit(self.image_2, self.rect) # verde - barra de delante


    def update(self, personaje_rect_x, personaje_rect_y, vida_actual)-> None:
        """
        Actualiza la posición y el ancho de la barra de vida.
        (se va a ubicar arriba del personaje  y del enemigo)
        Recibe:
            Args:
            personaje_rect_x (int): Posición en el eje x del personaje.
            personaje_rect_y (int): Posición en el eje y del personaje.
            vida_actual (int): Valor actual de vida.

        Devuelve: None
        """
        self.rect.x = personaje_rect_x  # Actualiza la posición horizontal
        self.rect.y = personaje_rect_y
        self.ancho_bar_2 = vida_actual * 100 / self.vida_maxima
        if(self.image_2.get_width() > 0):
            self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
            self.image_2.fill((0, 255, 0))
    
        


    

