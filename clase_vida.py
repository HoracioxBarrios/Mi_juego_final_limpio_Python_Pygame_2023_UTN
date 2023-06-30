import pygame

class BarraVida:
    def __init__(self, screen, vida_maxima, ancho_bar, alto_bar, pos_x, pos_y, ):
        super().__init__()
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

        self.ancho_bar_2 = 50
        self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
        self.rect_2 = self.image_2.get_rect()
        self.rect_2.x = pos_x
        self.rect_2.y = pos_y
        self.image_2.fill((0, 255, 0))
        

    def draw(self, screen : pygame.Surface):
        screen.blit(self.image, self.rect)# rojo
        screen.blit(self.image_2, self.rect) # verde


    def update(self, personaje_rect_x, personaje_rect_y):
        self.rect.x = personaje_rect_x  # Actualiza la posición horizontal
        self.rect.y = personaje_rect_y
        self.rect_2


    

