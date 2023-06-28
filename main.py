import pygame
from utilidades import *
from creador_mundo import *
from personaje import Personaje
from enemigo import Enemigo
from stage import Stage
pygame.init()

ancho_pantalla = 1000
alto_pantalla = 700

screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

running = True
FPS = 60
BLANCO = (255, 255, 255)
relog = pygame.time.Clock()
bg_fondo = pygame.image.load("asset\game_background_1.png")
bg_fondo = pygame.transform.scale(bg_fondo, (ancho_pantalla, alto_pantalla))


world_data = leerJson('stages.json')
stage = world_data["stages"][0]["stage_1"]
# print(stage)

tile_size = 50
margen = 0
path_music_world = world_data["stages"][0]["musica_path"] 
world = World(stage, tile_size, 'asset\StoneBlock.png', screen, path_music_world)
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
flag = True

char_list = []
personaje = Personaje(50, 50, world.tile_list)
enemigo = Enemigo(600, 50, world.tile_list)
stage = Stage()
all_sprites = pygame.sprite.Group()
all_sprites.add(personaje, enemigo)

while running:

    screen.blit(bg_fondo, (0, 0))
    lista_pisos =  world.draw()

    
    

    dibujar_grid(screen, BLANCO, tile_size, ancho_pantalla, alto_pantalla, 0)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
    #orden de verificación
        #gravedad
        #colision
        #incremento o decrementos de los rect en y, x
    pygame.draw.rect(screen, (255, 255, 255), personaje.get_rect, 2)
    pygame.draw.rect(screen, (255, 255, 255), enemigo.get_rect, 2)

    
    # stage.verificar_colision(lista_pisos, enemigo)
    all_sprites.draw(screen)

    all_sprites.update()
    pygame.display.update()

    ms = relog.tick(FPS)

pygame.quit()