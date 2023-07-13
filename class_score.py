import pygame

class ScoreStage:
    def __init__(self, screen : pygame.Surface, x : int, y: int ,score: int)-> None:
        """
        Clase que representa el puntaje en un escenario del juego.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            x (int): Posición en el eje x del puntaje.
            y (int): Posición en el eje y del puntaje.
            score (int): Puntaje actual.
        Devuelve: None
        """
        
        self.type_fuente = "DSEG"
        self.tamanio_fuente = 55
        self.color_texto = (255, 60, 60)
        self.fuente = pygame.font.SysFont(self.type_fuente, self.tamanio_fuente)
        self.texto_score = "Score: "
        self.score_text = self.fuente.render(self.texto_score, True, self.color_texto)
        self.game_over = False
        self.screen = screen
        self.x = x
        self.y = y
        self.elapsed_time = 0
        self.score = score
        
        
    def draw_score(self)-> None:
        """
        Dibuja el puntaje en la pantalla.
        Recibe. None
        Devuelve. None
        """
        self.score_text = self.fuente.render("Score: {0}".format(self.score), True, self.color_texto)
        self.screen.blit(self.score_text, (self.x, self.y))

    def update_score(self)-> None:
        """
        Actualiza el puntaje en la pantalla.
        Recibe: None
        Devuelve: None
        """
        self.draw_score()

