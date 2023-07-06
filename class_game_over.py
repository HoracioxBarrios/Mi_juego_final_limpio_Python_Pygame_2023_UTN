import pygame
import sys
from class_boton import Button

def get_font(font_obtenida, size):
    return pygame.font.Font(font_obtenida, size)

class GameOver:
    def __init__(self, screen, score):
        self.score = score
        self.score_ubi_x = 0 
        self.score_ubi_y = 400
        self.screen = screen
        self.ancho_screen = screen.get_width()
        self.alto_screen = screen.get_height()
        self.back_groung_game_over = pygame.image.load("asset/game over.jpg")
        self.back_groung_game_over = pygame.transform.scale(self.back_groung_game_over, (self.ancho_screen, self.alto_screen))
        self.font_obtenida = "fonts/font.ttf"

    def draw_score(self):
        scores = [self.score] if type(self.score) != list else self.score
        scores.extend([0] * (3 - len(scores)))

        score_gap = 50
        font = pygame.font.SysFont("Arial", 48)
        color = (255, 255, 255)

        for i in range(len(scores)):
            score = scores[i]
            score_text = font.render("Score: " + str(score), True, color)
            score_rect = score_text.get_rect(midtop=(self.ancho_screen // 2, self.score_ubi_y + score_gap * (i + 1)))
            self.screen.blit(score_text, score_rect)

        

    def show_game_over(self):
        pygame.mixer.music.load('sonido/DRAGON BALL Z Cha-La Head Guitarra Christianvib.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        while True:
            self.screen.blit(self.back_groung_game_over, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(self.font_obtenida, 48).render("Game Over", True, (247, 35, 12))
            MENU_RECT = MENU_TEXT.get_rect(center=(self.ancho_screen / 2, 80))

            PLAY_BUTTON = Button(image=pygame.image.load("asset/Play Rect.png"), pos=(self.ancho_screen/2, 170), 
                                text_input="Volver a Jugar", font=get_font(self.font_obtenida, 20), base_color="White", hovering_color=(248, 209, 5))
            # OPTIONS_BUTTON = Button(image=pygame.image.load("asset/Options Rect.png"), pos=(self.ancho_screen/2, 350), 
            #                     text_input="Opciones", font=get_font(self.font_obtenida, 20), base_color="White", hovering_color=(248, 209, 5))
            QUIT_BUTTON = Button(image=pygame.image.load("asset/Quit Rect.png"), pos=(self.ancho_screen / 2, 340), 
                                text_input="Salir", font=get_font(self.font_obtenida, 20), base_color="White", hovering_color=(248, 209, 5))

            self.screen.blit(MENU_TEXT, MENU_RECT)
            self.draw_score()
            for button in [PLAY_BUTTON, QUIT_BUTTON]:#OPTIONS_BUTTON, 
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
            
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pass # a otro lado
                        # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        #     pass # a otro lado
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
            
