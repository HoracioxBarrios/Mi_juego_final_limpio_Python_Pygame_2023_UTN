import pygame
from utilidades import leerJson

class StagePadre:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.tile_list = []
        self.margen = 0

    def generar_coordenadas_mapa(self):
        for row in self.mapa_list:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.bloque_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = self.row_count * self.tile_size
                    self.tile_list.append((img, img_rect))
                col_count += 1
            self.row_count += 1

    @property
    def ancho_screen(self):
        return self.screen.get_width()

    @property
    def alto_screen(self):
        return self.screen.get_height()

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
        return self.tile_list
