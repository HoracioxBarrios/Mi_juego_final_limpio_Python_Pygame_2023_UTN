import pygame
import sys
import sqlite3
from class_boton import Button


def get_font(font_obtenida, size)-> pygame.font:
    """
    Devuelve un objeto de fuente pygame.font.Font con la fuente y 
    tamaño especificados.
    Recibe:
    Args:
        font_obtenida (str): Ruta de la fuente de la fuente a utilizar.
        size (int): Tamaño de la fuente a utilizar.

    Devuelve:
        pygame.font.Font: Objeto de fuente pygame.font.Font.
    """
    return pygame.font.Font(font_obtenida, size)

    
class GameOver:
    
    def __init__(self, screen : pygame.Surface)-> None:
       
        """
        Inicializa la clase GameOver con la pantalla del juego especificada.
        Win o Game Over
        Recibe:
        Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        Devuelve: None
        """
        self.score = [0, 0, 0]
        self.score_ubi_x = 0
        self.score_ubi_y = 400
        self.screen = screen
        self.ancho_screen = screen.get_width()
        self.alto_screen = screen.get_height()
        self.font_obtenida = "fonts/font.ttf"

        # Crea una conexión a la base de datos utilizando el manejador 
        # de contexto
        with sqlite3.connect('scores.db') as conn:
            c = conn.cursor()
            # Crear la tabla si no existe
            c.execute('''CREATE TABLE IF NOT EXISTS scores (score INTEGER)''')

    def draw_score(self, scores : list)-> None:
        """
        Dibuja los puntajes en la pantalla.
        Recibe:
        Args:
            scores (list): Lista de puntajes a dibujar en la pantalla.
        Devuelve: None
        """
        score_gap = 50
        font = pygame.font.SysFont("Arial", 48)
        color = (255, 255, 255)

        for i in range(len(scores)):
            score = scores[i]
            score_text = font.render("Score: " + str(score), True, color)
            score_rect = score_text.get_rect(midtop=(self.ancho_screen // 2, self.score_ubi_y + score_gap * (i + 1)))
            self.screen.blit(score_text, score_rect)
            

    def show_game_over(self, msg, fn: any, list_score):
        """
        Muestra la pantalla de "Game Over" con opciones para volver a 
        jugar o salir del juego.
        Recibe:
            Args:
                msg (str): Mensaje a mostrar en la pantalla, puede ser "Game Over" 
                o "Win".
                fn (any): Función a llamar cuando se presiona el botón de volver 
                a jugar.
                list_score (list o int): Puntuación o lista de puntuaciones a 
                mostrar en la pantalla. Si es un entero,se convierte en una 
                lista con un solo elemento.
        Devuelve: None
        """
        pygame.mixer.music.load('sonido/DRAGON BALL Z Cha-La Head Guitarra Christianvib.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)
        if msg == "Game Over":
            self.back_groung_game_over = pygame.image.load("asset\game_over_2.jpg")
            self.back_groung_game_over = pygame.transform.scale(self.back_groung_game_over,
                                                                 (self.ancho_screen, self.alto_screen))
        else:  # Win
            self.back_groung_game_over = pygame.image.load("asset/win.jpg")
            self.back_groung_game_over = pygame.transform.scale(self.back_groung_game_over,
                                                                 (self.ancho_screen, self.alto_screen))

        if isinstance(list_score, list):
            scores = list_score + [0] * (3 - len(list_score))
        else:
            scores = [list_score] + [0] * 2

        scores.sort(reverse=True)

        # Guardar el puntaje en la base de datos utilizando el manejador 
        # de contexto
        list_score = scores[0]  # Suponiendo que el puntaje se encuentra en la primera posición de la lista
        with sqlite3.connect('scores.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO scores VALUES (?)", (list_score,))

        # Cargar los puntajes anteriores desde la base de datos y ordenarlos de mayor a menor
        with sqlite3.connect('scores.db') as conn:
            c = conn.cursor()
            c.execute("SELECT score FROM scores ORDER BY score DESC LIMIT 5")
            previous_scores = c.fetchall()

        while True:
            self.screen.blit(self.back_groung_game_over, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = get_font(self.font_obtenida, 48).render(msg, True, (247, 35, 12))
            MENU_RECT = MENU_TEXT.get_rect(center=(self.ancho_screen / 2, 80))

            PLAY_BUTTON = Button(image=pygame.image.load("asset/Play Rect.png"), pos=(self.ancho_screen / 2, 170),
                                text_input="Volver a Jugar", font=get_font(self.font_obtenida, 20), base_color="White",
                                hovering_color=(248, 209, 5))
            QUIT_BUTTON = Button(image=pygame.image.load("asset/Quit Rect.png"), pos=(self.ancho_screen / 2, 340),
                                text_input="Salir", font=get_font(self.font_obtenida, 20), base_color="White",
                                hovering_color=(248, 209, 5))

            self.screen.blit(MENU_TEXT, MENU_RECT)
            self.draw_score(previous_scores)
            for button in [QUIT_BUTTON, PLAY_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            fn()
                        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                            pygame.quit()
                            sys.exit()
            pygame.display.update()
