import pygame, sys
from utilidades import *
from configuracion import *
from class_Stage import StagePadre
from class_personaje import Personaje
from class_enemigo import Enemigo
from class_proyectil import Proyectil
from levels.class_stage_1 import Stage_1
from modo.modo_dev import *
from class_tiempo_stages import TiempoStages

pygame.init()

def game():
    

    

    ancho_pantalla = ANCHO_PANTALLA
    alto_pantalla = ALTO_PANTALLA

    screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

    running = True
    fps = FPS

    relog = pygame.time.Clock()






    #Instancias

    #instancio el stage actual. luego podria tener varios stages en una lista y llamarlo segun elecion desde los indices
    stage_actual = Stage_1(screen)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    
    enemigo = Enemigo(screen, 800, 200, stage_actual.tile_list)
    personaje = Personaje(5, 600, stage_actual.tile_list, screen, enemigo)
    poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
    poder_list:list[Proyectil] = []
    poder_list.append(poder)

    sprites_personajes = pygame.sprite.Group()
    sprites_personajes.add(personaje, enemigo)

    # time_stage instancia
    tiempo_stage = TiempoStages(screen, 0, 0)
    
    
    
    while running:

        screen.blit(stage_actual.bg, (0, 0))#bg
        
        stage_actual.draw()#pisos
        
        #time_stage----
        tiempo_stage.update_time()
        #--------------
        
        
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

    

        pygame.display.update()

        delta_ms = relog.tick(fps)
        
        
        personaje.delta_ms = delta_ms
        enemigo.delta_ms = delta_ms
        poder.delta_ms = delta_ms

    pygame.quit()