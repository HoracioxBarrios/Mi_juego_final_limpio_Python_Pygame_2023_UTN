import pygame

class TiempoStages:
    def __init__(self, screen : pygame.Surface, x : int, y : int, limit : int)-> None:
        """
        Clase que representa el tiempo en un escenario del juego.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            x (int): Posición en el eje x del tiempo.
            y (int): Posición en el eje y del tiempo.
            limit (int): Límite de tiempo en segundos.
        Devuelve: None
        """
        self.type_fuente = "DSEG"
        self.tamanio_fuente = 48
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
        
        self.sound_time_delay = 28
        self.sound_time_delay_limit = 28
        
        
    def draw_time(self)-> None:
        """
        Dibuja el tiempo en la pantalla.
        Recibe . None
        Devuelve: None
        """
        self.screen.blit(self.time_text, (self.x, self.y))
        if self.elapsed_time >= self.limit:
            self.game_over = True
            self.time_text = self.fuente.render("Terminó el Tiempo", True, self.color_texto)

    def update_time(self, final = False)-> None:
        """
        Actualiza el tiempo en la pantalla.
        Recibe:
            Args:
            final (bool, optional): Indica si se quiere el tiempo en el final stage. 
            Por defecto, es False.
        Devuelve: None
        """
        current_time = pygame.time.get_ticks()
        self.elapsed_time = (current_time - self.start_time) / 1000
        self.time_text = self.fuente.render("Time: {:.2f}".format(self.elapsed_time), True, self.color_texto)

        self.draw_time()
        if final == False:
            if self.sound_time_delay <= 0:
                self.sound()
                self.sound_time_delay = self.sound_time_delay_limit
            else:
                self.sound_time_delay -= 1

    def sound(self)-> None:
        """
        Reproduce el sonido del radar. el tiempo que tiene uno de 
        juntar las esferas. 
        Recibe. None
        Devuelve: None
        
        """       
        self.sonido.set_volume(0.5)
        self.sonido.play()
