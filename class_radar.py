import pygame
import random
from utilidades import *
from class_personaje import Personaje



class Radar(pygame.sprite.Sprite):
    def __init__(self, screen : pygame.Surface, x : int, y: int, path_img: str, ancho : int, alto : int, id_propia : int) -> None:
        """
        Clase que representa un radar en el juego.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            x (int): Posición en el eje x del radar.
            y (int): Posición en el eje y del radar.
            path_img (str): Ruta de la imagen del radar.
            ancho (int): Ancho del radar.
            alto (int): Alto del radar.
            id_propia (int): Identificador único del radar.
        Devuelve: None
        """
        self.image = pygame.image.load(path_img)
        self.image = pygame.transform.scale(self.image, (ancho, alto))
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.x = x
        self.rect.y = y
        self.gravity_vel_y = 0
        self.dy = 0
        self.dx = 0
        self.id = id_propia
        self.catch_radar = False
        self.sonido = pygame.mixer.Sound("sonido\obtencion_radar.mp3")
        
        
    def add_gravity(self)-> None:
        """
        Agrega gravedad al radar.
        Recibe: None
        Devuelve: None
        """
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

    def update(self, screen : pygame.Surface, personaje: Personaje)-> None:
        """
        Actualiza el radar en función del personaje y la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            personaje (Personaje): Instancia del personaje en el juego.
        Devuelve: None
        """
        self.colison_personaje(personaje)
        self.draw(screen)
        
        
    def draw(self, screen : pygame.Surface)-> None:
        """
        Dibuja el radar en la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        Devuelve: None
        """
        screen.blit(self.image, self.rect)
        
        

    def colison_personaje(self, personaje: Personaje)-> None:
        """
        Verifica la colisión del radar con el personaje.
        Recibe: 
            Args:
            personaje (Personaje): Instancia del personaje en el juego.
        Devuelve: None
        """
        if self.rect.colliderect(personaje.rect):
            self.catch_radar = True
            self.sonido.set_volume(1)
            self.sonido.play()