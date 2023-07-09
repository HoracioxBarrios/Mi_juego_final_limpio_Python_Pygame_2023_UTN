import pygame
import sys
from class_boton import Button
from configuracion import *
from game import *
from class_tiempo_stages import TiempoStages

pygame.init()

font_obtenida = "fonts/font.ttf"
SCREEN = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Dragon Ball Sprite")

background_main = pygame.image.load("asset/Kid Goku Wallpaper.png")
background_main_rescalado = pygame.transform.scale(background_main, (ANCHO_PANTALLA, ALTO_PANTALLA))


def get_font(size):
    return pygame.font.Font(font_obtenida, size)


def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        game()

        pygame.display.update()


def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(20).render("Estas en la pantalla de Opciones", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ANCHO_PANTALLA / 2, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(ANCHO_PANTALLA / 2, 460),
                              text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    pygame.mixer.music.load('sonido/DRAGON BALL Z Cha-La Head Guitarra Christianvib.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)

    while True:
        SCREEN.blit(background_main_rescalado, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Dragon Ball Sprite", True, (247, 35, 12))
        MENU_RECT = MENU_TEXT.get_rect(center=(ANCHO_PANTALLA / 2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("asset/Play Rect.png"), pos=(ANCHO_PANTALLA / 2, 200),
                             text_input="Jugar", font=get_font(20), base_color="White",
                             hovering_color=(248, 209, 5))
        OPTIONS_BUTTON = Button(image=pygame.image.load("asset/Options Rect.png"), pos=(ANCHO_PANTALLA / 2, 350),
                                text_input="Opciones", font=get_font(20), base_color="White",
                                hovering_color=(248, 209, 5))
        QUIT_BUTTON = Button(image=pygame.image.load("asset/Quit Rect.png"), pos=(ANCHO_PANTALLA / 2, 500),
                             text_input="Salir", font=get_font(20), base_color="White",
                             hovering_color=(248, 209, 5))

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    preludio(SCREEN)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def intro():
    vid = Video("vid/intro.mp4")
    vid.set_size((ANCHO_PANTALLA, ALTO_PANTALLA))

    while True:
        if vid.active:
            vid.draw(SCREEN, (0, 0))
        else:
            vid.close()
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                main_menu()

        pygame.display.update()


def preludio(screen):
    
    
    background_main = pygame.image.load("asset\kamehouse.jpg")
    background_main_rescalado = pygame.transform.scale(background_main, (ANCHO_PANTALLA, ALTO_PANTALLA))
    cambiar_musica("sonido\intro_karaoke_dragonball_buscar_esferas (mp3cut.net).mp3", 0.2)
    fps = 30
    relog = pygame.time.Clock()
    
    index_stage = 0
    text_color = (0, 0, 0)
    text_index = 0
    balloon_position_krillin = (250, 300)
    balloon_color = (255, 255, 255)
    
    path_goku_intro = "asset/goku_intro_game_res.png"
    
    
    text = ["¡Hola, Goku!\nEstaba pensando que \n quizas seria bueno que practiqumos un poco."]

    text_goku = ["Tenes mucha razon Krillin,\nprepararse para el gran torneo... 123 Empecemos!"]
    dx_slide_boss = 20
    slide_krillin = 800
    contador_escena_start_game = 0
    path_krillin = "asset/krillin_intro_game.png"
    path_por_defecto = path_krillin
    time_text = 180 
    time_text_limit = 180
    finished_animation = False  # Variable para indicar si la animación ha finalizado
    while not finished_animation:  # Salir del bucle cuando la animación haya terminado
        SCREEN.blit(background_main_rescalado, (0, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if index_stage == 0 and contador_escena_start_game < 2:
            # load_music_intro = True
            #cambiar musica estaba aca
            font = pygame.font.Font(None, 36)
            image = pygame.image.load(path_por_defecto)
            oscurecer_pantalla(screen)
            if slide_krillin > 400:
                slide_krillin -= dx_slide_boss

            draw_text_and_image(screen, image, slide_krillin, 300)
            if slide_krillin == 400:
                if time_text > 0:
                    if text_index < len(text):
                        draw_text2(screen, text[text_index], font, text_color,
                                   balloon_position_krillin, balloon_color, max_width=350)
                        time_text -= 1
                else:
                    time_text = time_text_limit
                    text_index += 1
            if text_index >= len(text):
                path_por_defecto = path_goku_intro
                slide_krillin = 800
                text_index = 0
                text = text_goku
                contador_escena_start_game += 1

            if contador_escena_start_game >= 2:
                finished_animation = True  # La animación ha finalizado
        relog.tick(fps)
              
        pygame.display.update()
    play()



intro()
