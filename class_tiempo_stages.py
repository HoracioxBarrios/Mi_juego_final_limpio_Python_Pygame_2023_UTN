import pygame
import sys



class TiempoStages:
    def __init__(self, screen, x , y):
        self.type_fuente = "Impact"
        self.tamanio_fuente = 30
        self.color_texto = (238, 51, 10)
        self.fuente = pygame.font.SysFont(self.type_fuente, self.tamanio_fuente)
        self.start_time = pygame.time.get_ticks()
        self.texto_time = "Tiempo: "
        self.time_text = self.fuente.render(self.texto_time, True, self.color_texto)
        self.game_over = False
        self.screen = screen
        self.x = x
        self.y = y
    
    def draw_time(self):
        self.screen.blit(self.time_text, (self.x, self.y))
    
    def update_time(self):
        current_time = pygame.time.get_ticks()
        elapsed_time = (current_time - self.start_time) / 1000
        self.time_text = self.fuente.render("Time: {:.2f}".format(elapsed_time), True, self.color_texto)
        
        if elapsed_time >= 10:
            self.game_over = True
            self.time_text = self.fuente.render("Game Over", True, self.color_texto)
        
        self.draw_time()




