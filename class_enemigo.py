import pygame
from utilidades import *
from configuracion import *
from class_vida import BarraVida

class Enemigo(pygame.sprite.Sprite):  
    def __init__(self, screen : pygame.Surface, pos_x : int, pos_y :int, lista_pisos: list) -> None:
        """
        Constructor de la clase Enemigo.
        Hereda de :pygame.sprite.Sprite para aprobechar funcionalidades 
        de sprite.
        Args:
            screen (pygame.Surface): La pantalla del juego donde se mostrará 
            el enemigo.
            pos_x (int): La posición inicial en el eje x del enemigo.
            pos_y (int): La posición inicial en el eje y del enemigo.
            lista_pisos (list): Lista de pisos en el juego.
        Devuelve: None
        """
        super().__init__()
        self.caminando_r = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, False)
        self.caminando_l = get_surface_form_sprite_sheet('asset\enemigo\spites_enemigo.png', 8, 1, 0, 0, 7, True)
        self.gravity_vel_y = 0
        self.frame = 5
        self.velocidad_caminar = 15
        self.orientacion_x = -1
        self.esta_en_aire = True
        self.esta_caminando = False
        self.animacion = self.caminando_l
        self.image = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.imagen_width = self.image.get_width()
        self.imagen_height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.desplazamiento_x = 0
        self.dy = 0
        self.dx = 0
        self.limites_frames_por_segundo = 5
        self.time_colision = 0
        self.limite_colision = 5
        self.time_frame = 5
        self.lista_pisos = lista_pisos
        self.damage = 250
        self.vida = 1000
        self.barra_vida = BarraVida(screen,self.vida, 100, 5 , self.rect.x, self.rect.y -10)
        self.delta_ms = 0
        self.esta_muerto = False
        self.game_over_win = False
        
        
    def add_gravity(self)-> None:
        """
        Aplica gravedad al enemigo. Aumenta su velocidad vertical hacia abajo.
        incrementa la velocidad en y hasta un maximo de 10
        Recibe : None
        Devuelve: None
        """
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y
        
    def verificar_colision(self, lista_pisos : list)-> None:
        """
        Verifica la colisión del enemigo con los pisos, pared de la screen.

        Args:
            lista_pisos (list): Lista de pisos en el juego.
        Devuelve: None
        """
        for piso in lista_pisos:
            #x
            if piso[1].colliderect(self.rect.x + self.dx, self.rect.y, self.imagen_width, self.imagen_height):
                self.dx = 0
                if self.time_colision == 5:
                    #colisiona y va a la  la der
                    self.orientacion_x *= -1
                    
                    self.time_colision -= 1
                    
                else:
                    self.time_colision = self.limite_colision

            if piso[1].colliderect(self.rect.x + self.dx, self.rect.y, self.imagen_width, self.imagen_height):
                self.dx = 0
                if self.orientacion_x == 1 and self.time_colision == 5:
                    #colisiona y va a la  la izquierda
                    self.orientacion_x *= 1
                
                    
                    self.time_colision -= 1
                else:
                    self.time_colision = self.limite_colision
                
            #y        
            if piso[1].colliderect(self.rect.x, self.rect.y + self.dy, self.imagen_width, self.imagen_height):
                if self.gravity_vel_y < 0:
                    self.dy = piso[1].bottom - self.rect.top
                    self.gravity_vel_y = 0
                elif self.gravity_vel_y >= 0:
                    self.dy = piso[1].top - self.rect.bottom
                    self.gravity_vel_y = 0
                    self.esta_en_aire = False
        #contra screen          
        if self.rect.left + self.dx < 0:
            self.dx = 0
            if self.time_colision == 5:
                # Colisiona y cambia de dirección a la derecha
                self.orientacion_x *= -1
                self.time_colision -= 1
            else:
                self.time_colision = self.limite_colision

        elif self.rect.right + self.dx > ANCHO_PANTALLA:
            self.dx = 0
            if self.time_colision == 5:
                # Colisiona y cambia de dirección a la izquierda
                self.orientacion_x *= -1
                self.time_colision -= 1
            else:
                self.time_colision = self.limite_colision


    def update(self, screen, personaje :any, fn : any, path : str, credits_finished : bool)-> None:
        """
        Actualiza el enemigo en el juego.

        Args:
            screen (pygame.Surface): La pantalla del juego donde se mostrará 
            el enemigo.
            personaje (objeto): El personaje principal del juego.
            fn (function): Función de animación.
            path (str): Ruta de la imagen.
            credits_finished (bool): Estado del juego (si los créditos han 
            terminado).
        Devuelve: None
        """

        self.dx = self.desplazamiento_x
        self.dy = 0
        
        if(self.orientacion_x != 1):
            self.acciones('caminar_l')
        elif(self.orientacion_x == 1):
            self.acciones('caminar_r')
            
        self.verificar_frames()
        self.add_gravity()
        self.verificar_colision(self.lista_pisos)

        self.rect.x += self.dx
        self.rect.y += self.dy

        self.barra_vida.update(self.rect.x -10, self.rect.y, self.vida)
        self.barra_vida.draw(screen)
        self.draw(screen)

    def acciones(self, accion: str):
        """
        Ejecuta las acciones del enemigo.

        Args:
            accion (str): Acción a ejecutar ('caminar_r' o 'caminar_l').
        Devuelve: Nome
        """
        match(accion):
            case "caminar_r":
                self.caminar(accion)
            case "caminar_l":
                self.caminar(accion)

    def caminar(self, accion : str)-> None:
        """
        Hace que el enemigo camine en la dirección especificada.

        Args:
            accion (str): Acción de caminar ('caminar_r' o 'caminar_l').
        Devuelve: None
        """
        
        if(not self.esta_en_aire):
            if(accion == "caminar_r"):
                self.orientacion_x = 1
                self.cambiar_animacion(self.caminando_r)
                self.desplazamiento_x = self.velocidad_caminar
                
                self.esta_caminando = True
            else:
                self.orientacion_x = -1
                self.cambiar_animacion(self.caminando_l)
                self.desplazamiento_x = -self.velocidad_caminar
                
                self.esta_caminando = True

    def cambiar_animacion(self, nueva_lista_animaciones: list[pygame.Rect])-> None:
        """
        Cambia la animación del enemigo.

        Args:
            nueva_lista_animaciones (list): Nueva lista de animaciones del enemigo.
        Devuelve: None
        """
        self.animacion = nueva_lista_animaciones  
        
    def draw(self, screen)-> None:
        """
        Dibuja el enemigo en la pantalla del juego.

        Args:
            screen (pygame.Surface): La pantalla del juego donde se mostrará el enemigo.
        Devuelve: None
        """
        screen.blit(self.image, self.rect)
        
    def verificar_frames(self)-> None:
        '''
        Verifica los frames para animar al enemigo.        
        Recibe: None
        Devuelve: None
        
        '''
        if(self.time_frame <= 0):
            if(self.frame < len(self.animacion)):
                self.image = self.animacion[self.frame]
                self.time_frame = self.limites_frames_por_segundo
                self.frame += 1
            else:
                self.frame = 0
        else:
            self.time_frame -= self.delta_ms      
  
    @property
    def get_rect(self):
        """
        Obtiene el rectángulo del enemigo.
        Recibe: None

        Devuelve:
            pygame.Rect: Rectángulo del enemigo.
        """
        return self.rect
 
    

  
 