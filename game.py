import pygame, sys
from utilidades import *
from configuracion import *
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
from vid.pyvidplayer import Video
from class_poder_final import PoderFinalVid
from class_kame import Kame
import random
from class_game_over import GameOver
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
    poder_final = PoderFinalVid(0,0, screen)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.5)
    poder_kame = Kame(screen, ANCHO_PANTALLA,50, 1000, 1000, 0, 620)
    over_game = GameOver(screen, 5540) #score ejemplo 


    # time_stage instancia
    game_over = False
    stage_run = False
    index_stage = 0
    running = True
    stage_actual = None
    radar_on = False
    crono_on = False
    start_time = False
    time_limit = 35 # relog limite time
    lista_esferas = []
    lista_esferas_generada = False
    slide_boss = 600
    dx_slide_boss = 20
    
    balloon_position = (200, 250)
    balloon_color = (255, 255, 255)
    text_color = (0, 0, 0)
    text_position = (balloon_position[0] + 20, balloon_position[1] + 20)
    text = ["Has demostrado tu valentia\nllegando hasta aquí muchacho...", "Pero esta ves...\nno te sera tan facíl\npasar la prueba", "Asi que...\nPREPARATE!!", "A ver si puedes\ncontrarestar este ataque!!!"]
    text_goku = ["No te tengo miedo...", "Pero tampoco puedo confiarme...", "Dare todo en este ultimo ataque!!!"]
    time_text = 84
    time_text_limit = 84
    text_index = 0
    boss_img = False
    load_musica_battle = False
    load_music_intro = False
    path = "asset\jacky-pose.png"
    
    parte_final_2 = False
    contador_escena = 0
    flag_video_final = False
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
                elif evento.key == pygame.K_e:
                    poder_kame.contra_poder()

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
                tiempo_stage = TiempoStages(screen,420, 50, time_limit)
                start_time = True
            tiempo_stage.update_time()
            tiempo_stage.draw_time()
            if(tiempo_stage.elapsed_time >= time_limit):
                # show_game_over_screen(screen, ancho_pantalla, alto_pantalla)
                over_game.show_game_over()
        if(start_time):
            if(not lista_esferas_generada):
                for i in range(1, 8):  # El rango debe ser de 1 a 8 para generar las rutas correctas
                    path_esfera = "asset/esferas/{i}.png".format(i=i)
                    x = random.randint(0, ancho_screen_para_esferas)
                    y = random.randint(0, alto_screen_para_esferas)
                    esfera = Esferas(screen, x, y, path_esfera, ancho=45, alto=45, id_propia = i)
                    lista_esferas.append(esfera)
                    lista_esferas_generada = True
            for esfera in lista_esferas:
                esfera.update(screen, personaje)
                if(esfera.return_ID):
                    lista_esferas = filter_es(esfera.return_ID, lista_esferas)
                    esfera.return_ID = None
                    personaje.contador_esferas += 1


        if(index_stage == 3 and contador_escena < 2):
            if(not load_music_intro):
                load_music_intro = True
                pygame.mixer.music.load("sonido\intro_music.wav")
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(0.5)
            font = pygame.font.Font(None, 36)
            image = pygame.image.load(path)
            darken_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
            darken_surface.fill((0, 0, 0, 200))
            screen.blit(darken_surface, (0, 0))
            if(slide_boss > 200):
                slide_boss -= dx_slide_boss
           
            draw_text_and_image(screen, image, slide_boss)
            if(slide_boss == 200):
                if(time_text > 0 ):
                    if(text_index < len(text) ):
                        draw_text2(screen, text[text_index], font, text_color, balloon_position, balloon_color, max_width = 350 )
                        time_text -= 1
                else:
                    time_text = time_text_limit
                    text_index += 1
            if(text_index >= len(text)):# voz goku
                path = "asset\goku_chico.png"
                slide_boss = 600
                text_index = 0
                text = text_goku
                
                contador_escena += 1
            if contador_escena == 2 and not flag_video_final :
                flag_video_final = True
                video_pelea_final_1()
                if(not load_musica_battle):
                    load_musica_battle = True
                    pygame.mixer.music.load("sonido\musica_resto_pelea.wav")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)
                    parte_final_2 = True
        if(parte_final_2):
            poder_final.update()
            poder_kame.update()
        print("contador esc ",contador_escena)
                
        
        pygame.display.flip()
        delta_ms = relog.tick(fps)
        
        
        personaje.delta_ms = delta_ms
        enemigo.delta_ms = delta_ms
        poder.delta_ms = delta_ms

    
# def draw_text_and_image(screen, text, image, text_font, text_color, text_position, slide_boss):
#     text_surface = text_font.render(text, True, text_color)
#     screen.blit(text_surface, text_position)
#     image_rect = image.get_rect()
#     image_rect.x = slide_boss
#     image_rect.y = 0
#     screen.blit(image, image_rect)

def draw_text_and_image(screen, image, slide_boss):
    image_rect = image.get_rect()
    image_rect.x = slide_boss
    image_rect.y = 0
    screen.blit(image, image_rect)
    
# def draw_text(screen, text, text_font, text_color, text_position):
#     text_surface = text_font.render(text, True, text_color)
#     screen.blit(text_surface, text_position)
def draw_text2(screen, text, text_font, text_color, balloon_position, balloon_color, max_width):
    balloon_padding_top = 20  # Ajusta el valor del padding superior del globo
    balloon_padding_sides = 10  # Padding a los lados del globo
    balloon_margin = 10

    # Dividir el texto en líneas según el ancho máximo
    lines = []
    words = text.split()
    current_line = words[0]
    for word in words[1:]:
        if text_font.size(current_line + ' ' + word)[0] <= max_width - balloon_padding_sides * 2:
            current_line += ' ' + word
        else:
            lines.append(current_line)
            current_line = word
    lines.append(current_line)

    # Calcular el alto del globo en función del número de líneas
    balloon_height = len(lines) * text_font.get_height() + balloon_padding_top + balloon_padding_sides

    balloon_rect = pygame.Rect(0, 0, max_width, balloon_height)
    balloon_rect.midtop = balloon_position

    balloon_radius = 10

    pygame.draw.rect(screen, balloon_color, balloon_rect, border_radius=balloon_radius)
    pygame.draw.polygon(screen, balloon_color, [(balloon_rect.bottomright[0], balloon_rect.bottomright[1] - balloon_padding_sides),
                                                 (balloon_rect.bottomright[0] + balloon_margin, balloon_rect.bottomright[1]),
                                                 (balloon_rect.bottomright[0], balloon_rect.bottomright[1] + balloon_padding_sides)])

    line_height = text_font.get_height()
    y = balloon_rect.y + balloon_padding_top // 2
    for line in lines:
        text_surface = text_font.render(line, True, text_color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (balloon_rect.centerx, y)
        screen.blit(text_surface, text_rect)
        y += line_height


def filter_es(id, lista_esferas: list[Esferas]):
    new_list = []
    for esf in lista_esferas:
        if(esf.id != id):
            new_list.append(esf)
    return new_list

#------------------------------------------------  vid





def video_pelea_final_2():
    pygame.init()
    ancho = 1000
    alto = 700
    pygame.mixer.music.load("vid/video final goku vs roshi- cortado -parte 2.wav")
    # vid_2 = Video("vid\goku vs roshi video con audio completo .mp4")#vid final con
    # vid_2.set_size((ancho, alto))
    pygame.mixer.music.play()
    screen = pygame.display.set_mode((ancho, alto))
    while True:
        screen.fill("White")
        
        # if vid_2.active == True: # si es true cirre ek video
        #         vid_2.draw(screen, (0, 0))
        # else:
        #     vid_2.close()
            
            # main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     vid.close()
                #llamada a main menu ()
                # main_menu()
        pygame.display.update()

    

# pygame.mixer.music.load("vid\intrio video epic.wav")
# pygame.mixer.music.play()

def video_pelea_final_1():
    pygame.init()
    ancho = 1000
    alto = 700
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Epic Vid")

    vid_1 = Video("vid/video final goku vs roshi-coratodo-parte-1.avi")#vid final con
    vid_1.set_size((ancho, alto))

    runnig = True
    while runnig:
        
        pygame.display.update()
        if vid_1.active == True: # si es true cirre ek video
                vid_1.draw(screen, (0, 0))
                vid_1.set_volume(0.5)
        else:
            vid_1.close()
            # video_pelea_final_2()
            runnig = False
            # main_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     vid.close()
                #llamada a main menu ()
                # main_menu()
    



# video_pelea_final_1()

#------------------------------------------------


pygame.quit()