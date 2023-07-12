import pygame, sys
from utilidades import intro_transition, cambiar_musica, dibujar_grid
from configuracion import *
from class_personaje import Personaje
from class_enemigo import Enemigo
from class_proyectil import Proyectil
from levels.class_stage_1 import Stage_1
from levels.class_stage_2 import Stage_2
from levels.class_stage_3 import Stage_3
from levels.class_stage_4 import Stage_4
from modo.modo_dev import get_modo, cambiar_modo
from class_tiempo_stages import TiempoStages
from class_esferas import Esferas
from class_radar import Radar
from class_jacki import Boss
from vid.pyvidplayer import Video
from class_poder_final import PoderFinalVid
from class_kame import Kame
import random
from class_score import ScoreStage
pygame.init()

def game()-> list:
    '''
    corre el juego con lasinstancias de los obj
    recibe : None
    Devuelve : any
    '''

    # Dimensiones de la pantalla
    ancho_pantalla = ANCHO_PANTALLA
    alto_pantalla = ALTO_PANTALLA
    screen = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
    fps = FPS
    relog = pygame.time.Clock()

    # Instancias
    # Rutas de las imágenes de las esferas

    ancho_screen_para_esferas = 950
    alto_screen_para_esferas = 555

    #instancio el stage actual. luego podria tener varios stages en una lista y llamarlo segun elecion desde los indices
    stage_1 = Stage_1(screen)
    stage_2 = Stage_2(screen)
    stage_3 = Stage_3(screen)
    stage_4 = Stage_4(screen)
    stage_list = [stage_1, stage_2, stage_3, stage_4]
    poder_final = PoderFinalVid(0,0, screen)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.4)
    poder_kame = Kame(screen, ANCHO_PANTALLA,50, 1000, 1000, 0, 620)
    # over_game = GameOver(screen) #score ejemplo
    score = ScoreStage(screen , 0, 0, 0)
    # time_stage instancia
    stage_run = False
    index_stage = 0 #define el stage inicial
    running = True
    stage_actual = None
    radar_on = False
    crono_on = False
    start_time = False
    
    lista_esferas = []
    lista_esferas_generada = False
    slide_boss = 600
    
    dx_slide_boss = 20

    balloon_position = (200, 250)
    balloon_color = (255, 255, 255)
    text_color = (0, 0, 0)
    text = ["Has demostrado tu valentia\nllegando hasta aquí muchacho...", "Pero esta ves...\nno te sera tan facíl\npasar la prueba", "Asi que...\nPREPARATE!!", "A ver si puedes\ncontrarestar este ataque!!!"]
    text_goku = ["No te tengo miedo...", "Pero tampoco puedo confiarme...", "Dare todo en este ultimo ataque!!!"]
    time_text = 84
    time_text_limit = 84
    text_index = 0
    load_musica_battle = False
    load_music_intro = False
    path_jacky = "asset\jacky-pose.png"
    path_krillin = "asset\krillin_intro_game.png"
    path_por_defecto = path_krillin
    parte_final_2 = False
    contador_escena = 0
    flag_video_final = False
    score_game = 0
    
    
    
    game_over_win = False
    game_over_defeat = False
    credits_finished = False
    
    while running and not game_over_win and not game_over_defeat:
        # Estage
        if not stage_run:
            stage_run = True
            stage_actual = stage_list[index_stage]
            if(index_stage < 3):
                enemigo = Enemigo(screen, 800, 200, stage_actual.tile_list)
            else:
                enemigo = Boss(800, 570)
            personaje = Personaje(150, 600, stage_actual.tile_list, screen, enemigo, 0)
            poder = Proyectil(1, personaje.rect.x, personaje.rect.y)
            poder_list:list[Proyectil] = []
            print('personaje',personaje.score)
            print('score_game', score_game)
            personaje.score = score_game

            poder_list.append(poder)
        score_game = personaje.score
        score.score = score_game
        if(personaje.vida <= 0):
            # over_game.show_game_over("Game Over")
            game_over_defeat = True
        if(personaje.contador_esferas >= 7): #backup de score del personaje
            if(index_stage < len(stage_list) -1):
                index_stage += 1
                intro_transition("vid/stage_{0}.avi".format(index_stage), screen)
                if(index_stage < 3):
                    cambiar_musica(path = "sonido\musica_stage_{0}.mp3".format(index_stage))
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
            enemigo.rect.x = 1200

        screen.blit(stage_actual.bg, (0, 0))#bg

        stage_actual.draw()#pisos

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN :
                
                if evento.key == pygame.K_SPACE and personaje.control_personaje:
                    personaje.acciones("saltar")
                elif evento.key == pygame.K_w and personaje.control_personaje:
                    personaje.acciones("shot")
                elif evento.key == pygame.K_TAB and personaje.control_personaje:
                    cambiar_modo()
                elif evento.key == pygame.K_e and parte_final_2:
                    personaje.score += 2
                    poder_kame.contra_poder()

        #Modo Dev
        if get_modo():
            pygame.draw.rect(screen, (255, 255, 255), personaje.get_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), enemigo.get_rect, 2)
            pygame.draw.rect(screen, (255, 255, 255), personaje.poder.rect, 2)
            dibujar_grid(screen, BLANCO, stage_actual.tile_size, ancho_pantalla, alto_pantalla, 0)


       
        
        personaje.update(screen, index_stage)

        if(not enemigo.esta_muerto):
            enemigo.update(screen, personaje, final_game_vid ,"vid\proyecto final creditos -v2.avi", credits_finished)
            if enemigo.game_over_win:# termina el video y el enemigo avisa si ganamos.
                game_over_win = True

        


        if(radar_on):# Dibujar todas las esferas en la pantalla
            radar.update(screen, personaje)
            if(radar.catch_radar):
                crono_on = True
                radar_on = False
                radar = None

        if(crono_on):
            if(not start_time):
                tiempo_stage = TiempoStages(screen,420, 50, time_limit_stages)
                start_time = True
            tiempo_stage.update_time()
            tiempo_stage.draw_time()
            if(tiempo_stage.elapsed_time >= time_limit_stages):# show_game_over_screen(screen, ancho_pantalla, alto_pantalla)
                # over_game.score = score.score
                # over_game.show_game_over("Game Over")
                game_over_defeat = True
        if(start_time):
            if(not lista_esferas_generada):# genera las esferas
                for i in range(1, 8):  # El rango debe ser de 1 a 8 para generar las rutas correctas
                    path_esfera = "asset/esferas/{i}.png".format(i=i)
                    x = random.randint(0, ancho_screen_para_esferas)
                    y = random.randint(0, alto_screen_para_esferas)
                    esfera = Esferas(screen, x, y, path_esfera, ancho=50, alto=50, id_propia = i)
                    lista_esferas.append(esfera)
                    lista_esferas_generada = True
            for esfera in lista_esferas:
                esfera.update(screen, personaje)
                if(esfera.return_ID):
                    lista_esferas = filter_es(esfera.return_ID, lista_esferas)
                    esfera.return_ID = None
                    personaje.contador_esferas += 1
        #######################intro Inicio##########################
        #resulto en main
        #######################Intro Final###########################
        if(index_stage == 3 and contador_escena < 2):
            personaje.control_personaje = False
            if(not load_music_intro):
                load_music_intro = True
                cambiar_musica("sonido\intro_music.wav")
                path_por_defecto = path_jacky
            #cargamos fuente para interaccion
            font = pygame.font.Font(None, 36)
            #cargamos imagen de la interaccion - de gou, jacky
            image = pygame.image.load(path_por_defecto)
            #oscurese la pantalla - le damos un efecto mate
            oscurecer_pantalla(screen)
            if(slide_boss > 200):
                slide_boss -= dx_slide_boss

            draw_text_and_image(screen, image, slide_boss)# coversacion entre goku y jacky
            if(slide_boss == 200):
                if(time_text > 0 ):
                    if(text_index < len(text) ):
                        draw_text2(screen, text[text_index], font, text_color, balloon_position, balloon_color, max_width = 350 )
                        time_text -= 1
                else:
                    time_text = time_text_limit
                    text_index += 1
            if(text_index >= len(text)):# text voz goku
                path_por_defecto = "asset\goku_chico.png" # por defecto antes era jacky
                slide_boss = 600
                text_index = 0
                text = text_goku

                contador_escena += 1
            if contador_escena == 2 and not flag_video_final :# finaliza la coversacion entre goku y jacky 
                flag_video_final = True 
                correr_video("vid/video final goku vs roshi-coratodo-parte-1.avi", ancho_pantalla, alto_pantalla)
                if(not load_musica_battle):# preparamos la pelea final en stage final
                    load_musica_battle = True
                    pygame.mixer.music.load("sonido\musica_resto_pelea.wav")
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.5)
                    parte_final_2 = True
                    tiempo_stage_final_stage = TiempoStages(screen,420, 50, 40)
        if(parte_final_2):# lucha Kame, incrementa con el tiempo el poder del boss
            poder_final.update()
            poder_kame.update()
            tiempo_stage_final_stage.update_time(final=True)
            if(tiempo_stage_final_stage.elapsed_time > 5 and tiempo_stage_final_stage.elapsed_time < 10):
                poder_kame.caida_kame = 7
            elif(tiempo_stage_final_stage.elapsed_time > 10 and tiempo_stage_final_stage.elapsed_time < 15):
                poder_kame.caida_kame = 9
            elif(tiempo_stage_final_stage.elapsed_time > 15 and tiempo_stage_final_stage.elapsed_time < 20):
                poder_kame.caida_kame = 15
                
                
            if(poder_kame.image_1.get_width() <= 15):
                # over_game.score = score.score
                # over_game.show_game_over("Game Over")
                pygame.mixer.music.stop()
                correr_video("vid\goku resultado_explosion.avi", ancho_pantalla, alto_pantalla)
                game_over_defeat = True
            elif(poder_kame.image_1.get_width() >= poder_kame.limit_power_screen):
                pygame.mixer.music.stop()
                correr_video("vid\jacki resultado_explosion.avi", ancho_pantalla, alto_pantalla)
                parte_final_2 = False
                # cambiar_musica("sonido/final_game.mp3")
                personaje.control_personaje = True
                enemigo.cambiar_imagen(screen)
              
                # if final_game_vid(screen, "vid\proyecto final creditos -v2.avi"):# me seguro que consega juntar las 7 esferas al final
                #     game_over_win = True
                        # ver si funca
                
        


        score.update_score()
        pygame.display.flip()
        delta_ms = relog.tick(fps)

        personaje.delta_ms = delta_ms
        enemigo.delta_ms = delta_ms
        poder.delta_ms = delta_ms


    # volver al menu principal y (llevar el score y el game over) 
    lista_game_over_score = []
    lista_scores = []
    if game_over_defeat:
        lista_game_over_score.append("Game Over")
        lista_scores.append(score_game)
        lista_game_over_score.append(lista_scores)
        return lista_game_over_score
    elif game_over_win:
        lista_game_over_score.append("Win")
        lista_scores.append(score_game)
        lista_game_over_score.append(lista_scores)
        return lista_game_over_score

def draw_text_and_image(screen, image, slide_boss, pos_y = 0):
    image_rect = image.get_rect()
    image_rect.x = slide_boss
    image_rect.y = pos_y
    screen.blit(image, image_rect)
def oscurecer_pantalla(screen):
    darken_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    darken_surface.fill((0, 0, 0, 200))
    screen.blit(darken_surface, (0, 0))

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

def correr_video(path, ancho, alto):
    pygame.init()
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Dragon Ball Sprite")
    vid_1 = Video(path)#vid final
    vid_1.set_size((ancho, alto))
    vid_1.set_volume(0.3)

    runnig = True
    while runnig:
        pygame.display.update()
        if vid_1.active == True: # si es true cirre ek video
                vid_1.draw(screen, (0, 0))
                vid_1.set_volume(0.5)
        else:
            vid_1.close()
            runnig = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid_1.close()
                runnig = False
    

    


#------------------------------------------------
# vid Creditos
def final_game_vid(SCREEN, path):
    pygame.mixer.music.stop()
    vid = Video(path)
    vid.set_size((ANCHO_PANTALLA, ALTO_PANTALLA))
    vid.set_volume(0.5)
    while True:
        if vid.active == True:
            vid.draw(SCREEN, (0, 0))
        else:
            vid.close()
            credits_finished = True
            return  credits_finished # Actualiza la variable de bandera

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                credits_finished = True
                return  credits_finished

        pygame.display.update()
      


        

# ver si esta bien lo de la linea 270