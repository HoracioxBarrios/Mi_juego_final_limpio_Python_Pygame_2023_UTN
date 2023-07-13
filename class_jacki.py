import pygame
from class_personaje import Personaje



class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x : int, pos_y : int)-> None:
        '''
        Class boss 
        Recibe:
        pos x : representa la posicion inicial en eje x
        pos y : representa la posicion inicial en eje y
        Devuelve: None
        '''
        super().__init__()
        self.image = pygame.image.load('asset\jack_chun.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vida = 5000
        self.esta_muerto = False
        self.final_win = False
        self.game_over_win = False
        
        
        
    def update(self, screen , personaje: Personaje, fn: any, path : str, credits_finished : bool)-> None:
        """
        Actualiza el estado del jefe en cada iteración del bucle principal del juego.
        Recibe:
            Args:
            screen (pygame.Surface): La superficie de la pantalla del juego.
            personaje (Personaje): La instancia del personaje controlado por 
            el jugador.
            fn (function): La función para reproducir un video de derrota.
            path (str): La ruta del archivo de video.
            credits_finished (bool): Indica si los créditos del juego han terminado.
        Devuelve: None
        """
        self.draw(screen)
        self.colision_personaje(personaje, fn, path, screen, credits_finished)
        
    def draw(self, screen):
        """
        Dibuja la imagen del jefe en la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): La superficie de la pantalla del juego.
        Devuelve: None
        """
        screen.blit(self.image, self.rect)  
        
        
    def cambiar_imagen(self, screen)-> None:
        """
        Cambia la imagen del jefe a '7_esferas.png' para el final.
        Recibe:
            Args:
            screen (pygame.Surface): La superficie de la pantalla del juego.
        Devuelve: None
        """
        self.image = pygame.image.load('asset/7_esferas.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = screen.get_width() / 2
        self.rect.y = (screen.get_height() / 2 )+ 200 

    def colision_personaje(self, personaje: Personaje,fn, path, screen,  credits_finished: bool):
        """
        Comprueba si hay una colisión entre el jefe y el personaje.
        Recibe:
            Args:
            personaje (Personaje): La instancia del personaje controlado por 
            el jugador.
            fn (function): La función para reproducir un video de derrota.
            path (str): La ruta del archivo de video.
            screen (pygame.Surface): La superficie de la pantalla del juego.
            credits_finished (bool): Indica si los créditos del juego han terminado.
        Devuelve: None
        """
        if self.rect.colliderect(personaje.rect) and not credits_finished:
            self.game_over_win = fn(screen, path)# muestra el video de jacky derrotado y retorna true
            if self.game_over_win:
                self.esta_muerto = True
                personaje.score += 1