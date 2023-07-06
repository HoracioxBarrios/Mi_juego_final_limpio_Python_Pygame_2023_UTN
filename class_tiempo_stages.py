import pygame

class TiempoStages:
    def __init__(self, screen, x, y, limit):
        self.type_fuente = "DSEG"
        self.tamanio_fuente = 48
        self.color_texto = (238, 51, 10)
        self.color_fondo = (255, 255, 255)
        self.fuente = pygame.font.SysFont(self.type_fuente, self.tamanio_fuente)
        self.start_time = pygame.time.get_ticks()
        self.texto_time = "Tiempo: "
        self.time_text = self.fuente.render(self.texto_time, True, self.color_texto)
        self.game_over = False
        self.screen = screen
        self.x = x
        self.y = y
        self.limit = limit
        self.elapsed_time = 0
        self.sonido = pygame.mixer.Sound("sonido/sonido_radar.wav")
        self.time_control = 60
        self.time_control_limit = 60
        self.rect_width = 220
        self.rect_height = 70
        self.rect_radius = 10
        self.rect = pygame.Rect(self.x - 10, self.y - 10, self.rect_width, self.rect_height)
        self.background_rect = pygame.Rect(self.x - 15, self.y - 15, self.rect_width + 10, self.rect_height + 10)

    def draw_time(self):
        pygame.draw.rect(self.screen, self.color_fondo, self.background_rect)  # Dibujar el fondo
        pygame.draw.rect(self.screen, self.color_texto, self.rect, border_radius=self.rect_radius)  # Dibujar el marco
        self.screen.blit(self.time_text, (self.x, self.y))
        if self.time_control <= 0:
            self.sound()
            self.time_control = self.time_control_limit
        else:
            self.time_control -= 1

    def update_time(self):
        current_time = pygame.time.get_ticks()
        self.elapsed_time = (current_time - self.start_time) / 1000
        self.time_text = self.fuente.render("Time: {:.2f}".format(self.elapsed_time), True, self.color_texto)

        if self.elapsed_time >= self.limit:
            self.game_over = True
            self.time_text = self.fuente.render("Terminó el Tiempo", True, self.color_texto)

        self.draw_time()

    def sound(self):
        self.sonido.set_volume(0.5)
        self.sonido.play()
