import pygame
from utilidades import *
from configuracion import *
from class_world import *
import json
class Stage_1(StagePadre):
    def __init__(self, screen : pygame.Surface):
        
        self.tile_list = []
        #traigo del json los datos para el mapa
        self.ancho_screen = screen.get_width()
        self.alto_screen = screen.get_height()
        self.bg = pygame.image.load("asset\game_background_2.png")
        self.bg = pygame.transform.scale(self.bg, (self.ancho_screen, self.alto_screen))

        self.bloque_img = pygame.image.load('asset\StoneBlock.png')
        self.tile_size = 50
        self.world_data = leerJson('stages.json')
        self.mapa_list = self.world_data["stages"][1]["stage_2"]  # mapa 1 self.world_data["stages"][0]["stage_1"]
        self.world_music = self.world_data["stages"][0]["musica_path"]
        self.mapa_list = self.mapa_list
        self.row_count = 0
        self.music = pygame.mixer.music.load(self.world_music)
        self.generar_coordenadas_mapa()
        self.margen = 0
        
        
        
        
        
     
        super().__init__(screen)
        # Agrega aquí la inicialización específica para el mundo hijo

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
    

    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], tile[1])
        return self.tile_list

    def play_music(self, nivel_de_volumen, play_infinito=-1):
        pygame.mixer.music.play(play_infinito)
        pygame.mixer.music.set_volume(nivel_de_volumen)

    