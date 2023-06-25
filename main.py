import pygame
from utilidades import *
from creador_mundo import *
from personaje import Personaje
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
personaje = Personaje()

world_data = leerJson('stages.json')
stage = world_data["stages"][0]["stage_1"]
print(stage)

tile_size = 50
margen = 0
path_music_world = world_data["stages"][0]["musica_path"] 
world = World(stage, tile_size, 'asset\StoneBlock.png', screen, path_music_world)
pygame.mixer.music.play()
flag = True
while running:

    screen.blit(bg_fondo, (0, 0))
    lista_pisos =  world.draw()
    dibujar_grid(screen, BLANCO, tile_size, ancho_pantalla, alto_pantalla, 0)
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                personaje.acciones('saltar')
            if evento.key == pygame.K_w:
                personaje.acciones('shot')

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        personaje.acciones('caminar_l')
    if key[pygame.K_RIGHT]:
        personaje.acciones('caminar_r')
    if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
        personaje.acciones('quieto')

    personaje.updater(alto_pantalla, lista_pisos, screen)
    personaje.dibujar_en_pantalla(screen)
    pygame.display.update()

    ms = relog.tick(FPS)


pygame.quit()