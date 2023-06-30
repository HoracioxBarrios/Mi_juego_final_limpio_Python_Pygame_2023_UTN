import pygame
from utilidades import *
from creador_mundo import *
from personaje import Personaje
from enemigo import Enemigo
from stage import Stage
from proyectil import Proyectil
from clase_vida import BarraVida
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

#Instancias
char_list = []
personaje = Personaje(500, 50, world.tile_list, screen)
enemigo = Enemigo(screen, 800, 50, world.tile_list)
poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
poder_list:list[Proyectil] = []
poder_list.append(poder)
stage = Stage()
sprites_personajes = pygame.sprite.Group()
sprites_personajes.add(personaje, enemigo)



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
        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_SPACE:
                personaje.acciones("saltar")
            elif evento.key == pygame.K_w:
                if(not poder.proyectil_en_aire):
                    poder_list[0].rect.x = personaje.rect.x + 15 
                    poder_list[0].rect.y = personaje.rect.y + 29
                    poder_list[0].proyectil_en_aire = True
                    personaje.acciones("shot", poder.proyectil_en_aire)
                


    pygame.draw.rect(screen, (255, 255, 255), personaje.get_rect, 2)
    pygame.draw.rect(screen, (255, 255, 255), enemigo.get_rect, 2)
    
    # stage.verificar_colision(lista_pisos, enemigo)

    sprites_personajes.update(screen)
    sprites_personajes.draw(screen)
    poder.update()
    poder.verificar_colision(enemigo.rect, screen)
    poder.draw_proyectil(screen, personaje.orientacion_x)

   

    pygame.display.update()

    delta_ms = relog.tick(FPS)
    
    
    personaje.delta_ms = delta_ms
    enemigo.delta_ms = delta_ms
    poder.delta_ms = delta_ms

pygame.quit()