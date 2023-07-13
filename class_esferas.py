import pygame
import random
from utilidades import *
from class_personaje import Personaje



class Esferas(pygame.sprite.Sprite):
    def __init__(self, screen : pygame.Surface, x : int, y : int, path_img : str, ancho :int, alto :int, id_propia : int) -> None:
        """
        Constructor de la clase Esferas. Inicializa los atributos de la 
        instancia de la clase.
        
        Hereda de : pygame.sprite.Sprite para aprobechar funcionalidades 
        manejo de sprites.
        Args:
        screen: La superficie en la que se dibujará la esfera.
        x: La coordenada x inicial de la esfera.
        y: La coordenada y inicial de la esfera.
        path_img: La ruta de la imagen de la esfera.
        ancho: El ancho de la imagen de la esfera.
        alto: El alto de la imagen de la esfera.
        id_propia: El ID propio de la esfera.
        
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
        self.score = 1000
        self.id = id_propia
        self.return_ID = None
        self.sonido = pygame.mixer.Sound("sonido\item.wav")
    def add_gravity(self)-> None:
        """
        Agrega gravedad a la esfera. Actualiza la velocidad de caída 
        vertical de la esfera.
        Recibe : None
        Devuelve: None
        """
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

    def update(self,screen: any, personaje: Personaje)-> None:
        """
        Actualiza la esfera en la pantalla. Dibuja la esfera en la 
        pantalla y verifica si hay colisión con el personaje pasado 
        como argumento.
        Args:
        screen: La superficie en la que se dibujará la esfera.
        personaje: Una instancia de la clase Personaje con la que se 
        verificará la colisión.
        """
        self.draw(screen)
        self.colison_personaje(personaje)

    def draw(self, screen : any)-> None:
        """
        Dibuja la esfera en la pantalla.
        Args:
        screen: La superficie en la que se dibujará la esfera.
        Devuelve: None
        """
        screen.blit(self.image, self.rect)
        
    def colison_personaje(self, personaje: Personaje)-> None:
        """
        Verifica si hay colisión entre la esfera y el personaje pasado 
        como argumento.
        Si hay colisión, establece el atributo `return_ID` como el ID 
        propio de la esfera,
        reproduce un sonido y actualiza la puntuación del personaje.
        Args:
        personaje: Una instancia de la clase Personaje con la que se 
        verificará la colisión.
        Devuelve: None
        """
        if self.rect.colliderect(personaje.rect):
            self.return_ID = self.id
            self.sound()
            self.get_score(personaje)

    def sound(self):
        """
        Reproduce un sonido asociado a la esfera.
        Recibe: None
        Devuelve: None
        """
        self.sonido.set_volume(0.5)
        self.sonido.play()

    def get_score(self, pesonaje:Personaje)-> None:
        """
        Actualiza la puntuación del personaje al recoger la esfera.
        Args:
        pesonaje: Una instancia de la clase Personaje cuya 
        puntuación se actualizará.
        Devuelve: None
        """
        pesonaje.score += self.score
        


       