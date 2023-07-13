from utilidades import *
import pygame
class Proyectil:
    def __init__(self, orientacion_x_char : bool, pos_char_x : int, pos_char_y : int) -> None:
        """
        Clase que representa un proyectil en el juego.
        Recibe:
            Args:
            orientacion_x_char (bool): Orientación en el eje x del personaje 
            que dispara el proyectil.
            pos_char_x (int): Posición en el eje x del personaje que dispara 
            el proyectil.
            pos_char_y (int): Posición en el eje y del personaje que dispara 
            el proyectil.
        Devuelve: None
        """
        self.damage = 1
        self.vel_y = 0
        self.vel_x = 5
        self.frame = 0
        self.orientacion_x_char = orientacion_x_char
        self.imagen_r = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, False)
        self.imagen_l = get_surface_form_sprite_sheet('asset\poder\sprites_poder.png', 3, 1, 0, 0, 2, True)
        self.explocion = get_surface_form_sprite_sheet('asset\poder_colision_enemigo\sprite_explocion.png', 5, 1, 0, 0, 4, True)
        self.animacion = self.imagen_r
        self.image = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.imagen_width = self.image.get_width()
        self.imagen_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.desplazamiento_x = 0
        self.dx = 0
        self.rect.x = pos_char_x
        self.rect.y = pos_char_y
        self.proyectil_en_aire = False
        self.dibujando = False
        self.time_explocion = 10
        self.limites_frames_por_segundo = 10
        self.time_frame = 10
        self.impacto = False
        self.limite_tiempo_explocion = 10
        self.tiempo_explocion = 10
        self.dibijando_animacion_explocion = False
        self.delta_ms = 0
        self.colision = False
        
        self.sonido = pygame.mixer.Sound("sonido/086113_8-bit-cannonwav-40194.mp3")
        
        
        
    def update(self, delta_ms : int)-> None:
        """
        Actualiza el proyectil en función del tiempo transcurrido.
        Recibe:
            Args:
            delta_ms (int): Tiempo transcurrido desde la última actualización 
            en milisegundos.
        Devuelve: None
        """
        self.dx = self.desplazamiento_x
    
        if(self.impacto):
            self.time_explocion -= 1
            if(self.time_explocion <= 0):
                self.time_explocion = 10
                self.impacto = False
                self.colision = False

        self.verificar_frames(delta_ms)
        self.rect.x += self.dx
        
        
        
    def start_proyectile(self)-> None:
        """
        Inicia el proyectil, estableciendo la animación inicial según la 
        orientación del personaje.
        Recibe . None
        Devuelve: None
        """
        if(self.orientacion_x_char):
            self.animacion = self.imagen_r
        else:
            self.animacion = self.imagen_l
            
            
            
    def draw_proyectil(self, screen : pygame.surface.Surface, orientacion_personaje_x)-> None:
        """
        Dibuja el proyectil en la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
            orientacion_personaje_x (int): Orientación en el eje x del personaje.
        Devuelve: None
        """
        if self.proyectil_en_aire:
            if(self.rect.x < screen.get_width() and self.rect.x > 0):
                if orientacion_personaje_x == 1 and not self.dibujando:
                    self.cambiar_animacion(self.imagen_r)
                    self.desplazamiento_x = 10
                elif orientacion_personaje_x == -1 and not self.dibujando: 
                    self.cambiar_animacion(self.imagen_l)
                    self.desplazamiento_x = -10
                screen.blit(self.image, self.rect)
                self.dibujando = True
            else:
                self.proyectil_en_aire = False
                self.dibujando = False
                
                
    def set_animacion(self, num_frame : int)-> None:
        """
        Establece la animación del proyectil a partir del número de frame.
        Recibe:
            Args:
            num_frame (int): Número de frame.
        Devuelve: None
        """
        self.frame = num_frame
                
                
                
    def verificar_frames(self, delta_ms : int)-> None:
        """
        Verifica y actualiza los frames de animación del proyectil.
        Recibe:
            Args:
            delta_ms (int): Tiempo transcurrido desde la última actualización 
            en milisegundos.
        Devuelve: None
        """
        if(self.time_frame <= 0):
            if(self.frame < len(self.animacion)):
                self.image = self.animacion[self.frame]
                self.time_frame = self.limites_frames_por_segundo
                self.frame += 1
            else:
                self.frame = 0
        else:
            self.time_frame -= delta_ms
            
            

    def cambiar_animacion(self, nueva_lista_animaciones: list[pygame.Rect])-> None:
        """
        Cambia la animación actual del proyectil.
        Recibe:
            Args:
            nueva_lista_animaciones (list): Nueva lista de animaciones.
        Devuelve: None
        """
        self.animacion = nueva_lista_animaciones
        
        

    def draw_explocion(self, screen : pygame.Surface)-> None:
        """
        Dibuja la animación de explosión en la pantalla.
        Recibe:
            Args:
            screen (pygame.Surface): Superficie de la pantalla del juego.
        Devuelve: None
        """
        if(self.tiempo_explocion > 0):
            self.cambiar_animacion(self.explocion)
            screen.blit(self.image, self.rect)
            self.tiempo_explocion -= 1
        else:
            self.tiempo_explocion = self.limite_tiempo_explocion
            
        
    def verificar_colision(self, char : pygame.Rect, screen : pygame.Surface)-> None:
        """
        Verifica la colisión del proyectil con el personaje.
        Recibe:
            Args:
            char : (Enemigo) Rectángulo de colisión del enemigo .
            screen (pygame.Surface): Superficie de la pantalla del juego.
        Devuelve: None
        """
        if self.rect.colliderect(char):
            self.desplazamiento_x = 0
            if(self.time_explocion > 0):
                self.colision = True
                self.impacto = True
                self.dibujando = False
                self.proyectil_en_aire = False
                self.fin_animacion_explocion = True
                self.draw_explocion(screen)
                self.sound()
                
                
                
    def sound(self):
        """
        Reproduce el sonido de impacto del proyectil.
        Recibe: None
        Devuelve: None
        """
        self.sonido.set_volume(0.5)
        self.sonido.play()