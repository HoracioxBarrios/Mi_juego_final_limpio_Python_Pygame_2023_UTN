import pygame, sys
from class_boton import Button
from configuracion import *
from game import *
from vid.pyvidplayer import Video
from class_tiempo_stages import TiempoStages
pygame.init()


SCREEN = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Dragon Ball Sprite")

background_main = pygame.image.load("asset\Kid Goku Wallpaper.png")
background_main_rescalado = pygame.transform.scale(background_main,(ANCHO_PANTALLA,ALTO_PANTALLA))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("asset/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("Black")

        # PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        # PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        # SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        game()
        #---------------------
                
        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(20).render("Estas en la pantalla de Opciones", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(ANCHO_PANTALLA/2, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(ANCHO_PANTALLA/2, 460), 
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
    pygame.mixer.music.load('sonido\DRAGON BALL Z Cha-La Head Guitarra Christianvib.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.5)
    while True:
        SCREEN.blit(background_main_rescalado,(0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("Dragon Ball Sprite", True, (247, 35, 12))#color tupla (0, 0, 0)o "white" literal
        MENU_RECT = MENU_TEXT.get_rect(center=(ANCHO_PANTALLA /2, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("asset\Play Rect.png"), pos=(ANCHO_PANTALLA /2, 200), 
                            text_input="Jugar", font=get_font(20), base_color="White", hovering_color=(248, 209, 5))
        OPTIONS_BUTTON = Button(image=pygame.image.load("asset\Options Rect.png"), pos=(ANCHO_PANTALLA /2, 350), 
                            text_input="Opciones", font=get_font(20), base_color="White", hovering_color=(248, 209, 5))
        QUIT_BUTTON = Button(image=pygame.image.load("asset\Quit Rect.png"), pos=(ANCHO_PANTALLA /2, 500), 
                            text_input="Salir", font=get_font(20), base_color="White", hovering_color=(248, 209, 5))

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
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def intro():
    #vid\Dragon Ball Opening Latino HD 720p.mp4
    vid = Video("vid\intro.mp4")#vid\intro.mp4
    vid.set_size((ANCHO_PANTALLA, ALTO_PANTALLA))
    
    while True:
        #donde corre el video
        
        if vid.active == True: # si es true cirre ek video
            vid.draw(SCREEN, (0, 0)) 
        else:
            vid.close()
            main_menu()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.close()
                #llamada a main menu ()
                main_menu()





intro()