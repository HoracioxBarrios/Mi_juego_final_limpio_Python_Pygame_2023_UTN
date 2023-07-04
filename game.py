import pygame, sys
from utilidades import *
from configuracion import *
from class_Stage import StagePadre
from class_personaje import Personaje
from class_enemigo import Enemigo
from class_proyectil import Proyectil
from levels.class_stage_1 import Stage_1
from levels.class_stage_2 import Stage_2
from levels.class_stage_3 import Stage_3
from modo.modo_dev import *
from class_tiempo_stages import TiempoStages
from class_esferas import Esferas

import random
pygame.init()

def game():   

    
    ancho_pantalla = ANCHO_PANTALLA
    alto_pantalla = ALTO_PANTALLA

    screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

    
    fps = FPS

    relog = pygame.time.Clock()



# Instancias
    # Rutas de las imágenes de las esferas
    


    # Dimensiones de la pantalla
    ancho_screen = 900
    alto_screen = 500

    # Lista para almacenar las instancias de las esferas
    esferas = []

    for i in range(1, 8):  # El rango debe ser de 1 a 8 para generar las rutas correctas
        # Generar la ruta de la imagen de la esfera utilizando la variable 'i'
        path_esfera = "asset/esferas/{i}.png".format(i=i)
        
        # Generar coordenadas aleatorias dentro del rango de la pantalla
        x = random.randint(0, ancho_screen)
        y = random.randint(0, alto_screen)
        
        # Crear instancia de la esfera con las coordenadas aleatorias
        esfera = Esferas(screen, x, y, path_esfera, ancho=40, alto=40)
        
        # Agregar la instancia a la lista de esferas
        esferas.append(esfera)





    #instancio el stage actual. luego podria tener varios stages en una lista y llamarlo segun elecion desde los indices
    stage_1 = Stage_1(screen)
    stage_2 = Stage_2(screen)
    stage_3 = Stage_3(screen)
    stage_list = [stage_1, stage_2, stage_3]
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    
    # enemigo = Enemigo(screen, 800, 200, stage_actual.tile_list)
    # personaje = Personaje(5, 600, stage_actual.tile_list, screen, enemigo)
    # poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
    # poder_list:list[Proyectil] = []
    # poder_list.append(poder)

    # sprites_personajes = pygame.sprite.Group()
    # sprites_personajes.add(personaje, enemigo)

    # time_stage instancia
    tiempo_stage = TiempoStages(screen, 0, 0)
    game_over = False
    stage_run = False
    index_stage = 0
    running = True
    stage_actual = None
    while running:
        # for index in range(len(stage_list)):
        if not stage_run:
            stage_run = True
            stage_actual = stage_list[index_stage]
            enemigo = Enemigo(screen, 800, 200, stage_actual.tile_list)
            personaje = Personaje(5, 600, stage_actual.tile_list, screen, enemigo)
            poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
            poder_list:list[Proyectil] = []
            poder_list.append(poder)

            sprites_personajes = pygame.sprite.Group()
            sprites_personajes.add(personaje, enemigo)
                

        
        if(enemigo.vida <= 0):
            if(index_stage < len(stage_list) -1):
                index_stage += 1
                stage_run = False
        
        screen.blit(stage_actual.bg, (0, 0))#bg
        
        stage_actual.draw()#pisos
        
        #time_stage----
        tiempo_stage.update_time()
        #--------------
        


        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                sys.exit()
        #orden de verificación
            #gravedad
            #colision
            #incremento o decrementos de los rect en y, x
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_SPACE:
                    personaje.acciones("saltar")
                elif evento.key == pygame.K_w:
                    personaje.acciones("shot")
                elif evento.key == pygame.K_TAB:
                    cambiar_modo()    

        #Modo Dev
        if get_modo():
            pygame.draw.rect(screen, (255, 255, 255), personaje.get_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), enemigo.get_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), personaje.poder.rect, 2)
            dibujar_grid(screen, BLANCO, stage_actual.tile_size, ancho_pantalla, alto_pantalla, 0)

        sprites_personajes.update(screen)
        sprites_personajes.draw(screen)

        #esfera 
        # Dibujar todas las esferas en la pantalla
        for esfera in esferas:
            esfera.draw(screen)
    

        pygame.display.update()

        delta_ms = relog.tick(fps)
        
        
        personaje.delta_ms = delta_ms
        enemigo.delta_ms = delta_ms
        poder.delta_ms = delta_ms

    pygame.quit()