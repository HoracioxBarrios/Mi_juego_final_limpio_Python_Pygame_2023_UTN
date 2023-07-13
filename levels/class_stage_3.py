import pygame
from utilidades import leerJson
from configuracion import *
from class_Stage import *

class Stage_3(StagePadre):
    def __init__(self, screen: pygame.Surface):
        """
        Inicializa la etapa 1 del juego. el stage 1
        Recibe:
        Args:
        - screen: pygame.Surface
            Superficie de la pantalla del juego.
        Utiliza el metodo generar coordenadas_ mapa que hereda del StagePadre
        lo que genera coordenadas donde van a ubicarse unos rectangulos que representan
        al piso, pared, etc.
        
        devuelve: None
        """
        super().__init__(screen)
        
        self.bg = pygame.image.load("asset/fondo_3.jpg")
        self.bg = pygame.transform.scale(self.bg, (self.ancho_screen, self.alto_screen))

        self.bloque_img = pygame.image.load('asset\StoneBlock.png')
        self.tile_size = 50
        self.world_data = leerJson('stages.json')
        self.mapa_list = self.world_data["stages"][2]["stage_3"]
        self.world_music = self.world_data["stages"][0]["musica_path"]
        self.row_count = 0
        self.music = pygame.mixer.music.load(self.world_music)
        self.generar_coordenadas_mapa()
        self.run = False
