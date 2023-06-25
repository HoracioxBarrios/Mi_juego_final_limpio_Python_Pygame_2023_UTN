 
import pygame

class World():
    def __init__(self, mapa_list : list[list], tile_size, path_block: str, screen, music_path ) -> None:
        self.tile_list = []
        self.bloque_img = pygame.image.load(path_block)
        # agua_img = pygame.image.load("sprites/agua.png")
        self.tile_size = tile_size
        self.mapa_list = mapa_list
        self.row_count = 0
        self.screen = screen
        self.music = pygame.mixer.music.load(music_path)

    
        for row in self.mapa_list:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(self.bloque_img, (self.tile_size, self.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * self.tile_size
                    img_rect.y = self.row_count * self.tile_size
                    self.tile_list.append((img, img_rect))
                # if tile == 2:
                #     img = pygame.transform.scale(agua_img, (tile_size, tile_size))
                #     img_rect = img.get_rect()
                #     img_rect.x = col_count * tile_size
                #     img_rect.y = row_count * tile_size
                #     self.tile_list.append((img, img_rect))
                col_count += 1
            self.row_count += 1
    def draw(self):
        for tile in self.tile_list:
            self.screen.blit(tile[0], (tile[1])) # aca esta la screen , y la tupla de coordenadas ya que tile tiene esos valores.
        return self.tile_list

    def play_music(self, nivel_de_volumen, play_infinito = -1):
        '''
        play a music
        recibe el nivel de volumen de 0 a 1 float
        para que play sea infinito hay que poner -1 o 0 una vez
        devuelve: none       
        '''
        pygame.mixer.music.play(play_infinito)
        pygame.mixer.music.set_volume(nivel_de_volumen)
