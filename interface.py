import pygame
import sys
from class_boton import Button
from configuracion import ANCHO_PANTALLA, ALTO_PANTALLA
# from main import preludio, options
font_obtenida = "fonts/font.ttf"
background_main = pygame.image.load("asset/Kid Goku Wallpaper.png")
background_main_rescalado = pygame.transform.scale(background_main, (ANCHO_PANTALLA, ALTO_PANTALLA))
def main_menu(SCREEN):
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
                   pass # preludio(SCREEN)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                  pass  # options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def get_font(size):
    return pygame.font.Font(font_obtenida, size)

