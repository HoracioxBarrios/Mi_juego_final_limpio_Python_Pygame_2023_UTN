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
from levels.class_stage_4 import Stage_4
from modo.modo_dev import *
from class_tiempo_stages import TiempoStages
from class_esferas import Esferas
from class_radar import Radar
from class_jacki import Boss

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
    ancho_screen_para_esferas = 950
    alto_screen_para_esferas = 555

    # Lista para almacenar las instancias de las esferas
    

    # for i in range(1, 8):  # El rango debe ser de 1 a 8 para generar las rutas correctas
    #     # Generar la ruta de la imagen de la esfera utilizando la variable 'i'
    #     path_esfera = "asset/esferas/{i}.png".format(i=i)#i reemplaza a i en cada iteracion
        
    #     # Generar coordenadas aleatorias dentro del rango de la pantalla
    #     x = random.randint(0, ancho_screen_para_esferas)
    #     y = random.randint(0, alto_screen_para_esferas)
        
    #     # Crear instancia de la esfera con las coordenadas aleatorias
    #     esfera = Esferas(screen, x, y, path_esfera, ancho=40, alto=40, id_propia = i)
        
    #     # Agregar la instancia a la lista de esferas
    #     lista_esferas.append(esfera)
    
    



    #instancio el stage actual. luego podria tener varios stages en una lista y llamarlo segun elecion desde los indices
    stage_1 = Stage_1(screen)
    stage_2 = Stage_2(screen)
    stage_3 = Stage_3(screen)
    stage_4 = Stage_4(screen)
    stage_list = [stage_1, stage_2, stage_3, stage_4]
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    


    # time_stage instancia
    game_over = False
    stage_run = False
    index_stage = 3
    running = True
    stage_actual = None
    radar_on = False
    crono_on = False
    start_time = False
    time_limit = 10
    lista_esferas = []
    lista_esferas_generada = False
    slide_boss = 600
    dx_slide_boss = 20
    texto = "Hola Mundo"
    lista_letras = list(texto)
    print(lista_letras)
    while running:
        # Estage
        if not stage_run:
            stage_run = True
            stage_actual = stage_list[index_stage]
            if(index_stage < 3):
                enemigo = Enemigo(screen, 800, 200, stage_actual.tile_list)
            else:
                enemigo = Boss(800, 570)
            personaje = Personaje(150, 600, stage_actual.tile_list, screen, enemigo)
            poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
            poder_list:list[Proyectil] = []

            poder_list.append(poder)
        
             

        
        if(personaje.contador_esferas >= 7):
            if(index_stage < len(stage_list) -1):
                index_stage += 1
                tiempo_stage = None
                stage_run = False
                crono_on = False
                radar_on = False
                start_time = False
                lista_esferas_generada = False
               


        if(enemigo.vida <= 0 and not radar_on and not enemigo.esta_muerto):
            radar = Radar(screen, enemigo.rect.x, enemigo.rect.y, "asset/radar.png", 50, 50, 10)
            radar_on = True
            enemigo.esta_muerto = True
            
        screen.blit(stage_actual.bg, (0, 0))#bg
        
        stage_actual.draw()#pisos
        
        #time_stage----
        
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


        #esfera 
        # Dibujar todas las esferas en la pantalla
        personaje.update(screen, index_stage)

        if(not enemigo.esta_muerto):
            enemigo.update(screen)   

        if(radar_on):
            print('dibujando')
            radar.update(screen, personaje)
            if(radar.catch_radar):
                crono_on = True
                radar_on = False
                radar = None
            
        if(crono_on):
            if(not start_time):
                tiempo_stage = TiempoStages(screen, 0, 0, time_limit)
                start_time = True
            tiempo_stage.update_time()
            tiempo_stage.draw_time()
            if(tiempo_stage.elapsed_time >= time_limit):
                show_game_over_screen(screen, ancho_pantalla, alto_pantalla)
        if(start_time):
            if(not lista_esferas_generada):
                for i in range(1, 8):  # El rango debe ser de 1 a 8 para generar las rutas correctas
                    path_esfera = "asset/esferas/{i}.png".format(i=i)
                    x = random.randint(0, ancho_screen_para_esferas)
                    y = random.randint(0, alto_screen_para_esferas)
                    esfera = Esferas(screen, x, y, path_esfera, ancho=40, alto=40, id_propia = i)
                    lista_esferas.append(esfera)
                    lista_esferas_generada = True
            for esfera in lista_esferas:
                esfera.update(screen, personaje)
                if(esfera.return_ID):
                    lista_esferas = filter_es(esfera.return_ID, lista_esferas)
                    esfera.return_ID = None
                    personaje.contador_esferas += 1
        if(index_stage == 3):
            font = pygame.font.Font(None, 36)
            image = pygame.image.load("asset\jacky-pose.png")
            darken_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            darken_surface.fill((0, 0, 0, 200))
            screen.blit(darken_surface, (0, 0))
            if(slide_boss > 200):
                slide_boss -= dx_slide_boss
            for letra in lista_letras:
                draw_text_and_image(screen, letra , image, font, (255, 255, 255), (100, 100), slide_boss)
                
        pygame.display.update()
        delta_ms = relog.tick(fps)
        
        
        personaje.delta_ms = delta_ms
        enemigo.delta_ms = delta_ms
        poder.delta_ms = delta_ms

    
def draw_text_and_image(screen, text, image, text_font, text_color, text_position, slide_boss):
    text_surface = text_font.render(text, True, text_color)
    screen.blit(text_surface, text_position)
    image_rect = image.get_rect()
    image_rect.x = slide_boss
    image_rect.y = 0
    screen.blit(image, image_rect)

def draw_text_and_image_with_transition(screen, text, image, text_font, text_color, text_position, image_position, transition_duration):
    alpha = 0
    target_alpha = 255
    start_time = pygame.time.get_ticks()

    while alpha < target_alpha:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - start_time
        if elapsed_time >= transition_duration:
            alpha = target_alpha
        else:
            alpha = int((elapsed_time / transition_duration) * target_alpha)

        screen.fill((255, 255, 255))  # Rellena la pantalla de blanco con opacidad completa

        # Calcular opacidad inversa para el texto
        text_alpha = 255 - alpha
        text_surface = text_font.render(text, True, (text_color[0], text_color[1], text_color[2], text_alpha))
        screen.blit(text_surface, text_position)

        # Calcular opacidad inversa para la imagen
        image_alpha = 255 - alpha
        image.set_alpha(image_alpha)
        screen.blit(image, image_position)

        pygame.display.flip()


def show_game_over_screen(screen, width, height):
    game_over_font = pygame.font.Font(None, 64)  # Fuente y tamaño del texto "Game Over"
    game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))  # Texto "Game Over" en blanco

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        screen.fill((0, 0, 0, 0.5))  # Rellena la pantalla con negro
        screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))  # Dibuja el texto centrado en la pantalla

        pygame.display.flip()

def filter_es(id, lista_esferas: list[Esferas]):
    new_list = []
    for esf in lista_esferas:
        if(esf.id != id):
            new_list.append(esf)
    return new_list



pygame.quit()