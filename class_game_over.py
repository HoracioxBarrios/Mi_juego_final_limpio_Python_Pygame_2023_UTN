import pygame, sys
from class_boton import Button

class GameOver:
    def __init__(self, screen, score, font):
        self.score = score
        self.continue_button = Button(image=pygame.image.load("asset\Continue Button.png"), pos=(ANCHO_PANTALLA / 2, 400),
                                      text_input="Continuar", font=get_font(20), base_color="White",
                                      hovering_color=(248, 209, 5))
        self.screen = screen
        self.ancho_screen = screen.get_width()
        self.alto_screen = screen.get_heigth()
        self.back_groung_game_over = "" # falta path
        self.back_groung_game_over = pygame.transform.scale(self.back_groung_game_over, (screen))
        self.font_obtenida = font
    def get_font(self, size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font(self.font_obtenida, size)

    def show(self, ):
        while True:
            self.screen.blit(self.back_groung_game_over, (0, 0))

            game_over_text = Button (self.get_font(40).render("Game Over", True, (247, 35, 12)))
            game_over_rect = game_over_text.get_rect(center=(self.ancho_screen/ 2, 200))

            score_text = self.get_font(30).render(f"Puntaje: {self.score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.ancho_screen/ 2, 300))

            self.screen.blit(game_over_text, game_over_rect)
            self.screen.blit(score_text, score_rect)

            mouse_pos = pygame.mouse.get_pos()
            self.continue_button.changeColor(mouse_pos)
            self.continue_button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.continue_button.checkForInput(mouse_pos):
                        return

            pygame.display.update()


    # def show_game_over_screen(screen, width, height):
    #     game_over_font = pygame.font.Font(None, 64)  # Fuente y tamaño del texto "Game Over"
    #     game_over_text = game_over_font.render("Game Over", True, (255, 255, 255))  # Texto "Game Over" en blanco

    #     while True:
    #         for event in pygame.event.get():
    #             if event.type == QUIT:
    #                 pygame.quit()
    #                 return

    #         screen.fill((0, 0, 0))  # Rellena la pantalla con negro
    #         screen.blit(game_over_text, (width/2 - game_over_text.get_width()/2, height/2 - game_over_text.get_height()/2))  # Dibuja el texto centrado en la pantalla

    #         pygame.display.flip()