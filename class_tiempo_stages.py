import pygame
import sys



class TiempoStages:
    def __init__(self, screen, x , y, limit):
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
        self.limit = limit
        self.elapsed_time = 0
        self.sonido = pygame.mixer.Sound("sonido\sonido_radar.wav")
        self.time_control = 60
        self.time_control_limit = 60
        

    def draw_time(self):
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
            self.time_text = self.fuente.render("Game Over", True, self.color_texto)
            
        self.draw_time()
    
    def sound(self):
        self.sonido.set_volume(0.5)
        self.sonido.play()




