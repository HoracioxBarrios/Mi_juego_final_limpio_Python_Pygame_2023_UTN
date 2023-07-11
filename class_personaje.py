import pygame
from utilidades import *
from configuracion import *
from class_proyectil import Proyectil
from class_vida import BarraVida
from class_enemigo import Enemigo

class Personaje(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, lista_pisos, screen, enemigo: Enemigo, score):
        super().__init__()
        self.quieto_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, True)
        self.quieto_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, False)
        self.corriendo_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, False)
        self.corriendo_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, True)
        self.saltando_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, False)#para recortar una sola imagen, se ponen el desde y el hasta con el mismo valor
        self.saltando_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, True)
        self.shot_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, True)
        self.shot_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, False)
        self.estatico = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 2, 3, 3, True)
        self.gravity_vel_y = 0
        self.velocidad_caminar = 11
        self.desplazamiento_x = 0
        self.potencia_salto = 19
        self.enemigo = enemigo
        self.limites_frames_por_segundo = 5
        self.time_frame = 5
        self.orientacion_x = 1
        self.shot_on = False
        self.esta_caminando = False
        self.esta_en_aire = False
        self.control_personaje = True
        self.shot_time = 25
        self.shot_time_limit = 25
        self.dy = 0
        self.dx = 0
        self.frame = 0
        self.score = score
        self.animacion = self.quieto_r
        self.image = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        #--------------------------------
        self.rect : pygame.Rect = self.image.get_rect()
        self.new_width = 70

        # Calcula el desplazamiento horizontal para centrar el rectángulo
        horizontal_offset = (self.rect.width - self.new_width) // 2

        # Actualiza el ancho del rectángulo
        self.rect.width = self.new_width

        # Ajusta la posición horizontal del rectángulo
        self.rect.x += horizontal_offset
        #--------------------------------
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.imagen_width = self.image.get_width()
        self.imagen_height = self.image.get_height()
        self.lista_pisos = lista_pisos

        self.sonido_pasos = pygame.mixer.Sound('sonido\correr.wav')
        self.sonido_poder = pygame.mixer.Sound('sonido\poder.wav')
        self.sonido_kame = pygame.mixer.Sound("sonido\kame.wav")
        self.sonido_salto = pygame.mixer.Sound('sonido\salto.wav')
        self.sonido_salto_grito = pygame.mixer.Sound("sonido\salto_voz.wav")
        self.sonido_explosion = pygame.mixer.Sound("sonido\explocion.wav")
        self.time_sound = 10
        
        self.vida = 1000
        self.barra_vida = BarraVida(screen,self.vida, 100, 5 , self.rect.x, self.rect.y -10)
        self.daño = 250
        self.delta_ms = 0
        self.poder = Proyectil(self.orientacion_x, self.rect.x, self.rect.y)
        self.poder_list: list[Proyectil] = []

        self.contador_esferas = 0
        self.time_damage_recibido = 20
        self.time_damage_recibido_limit = 20
    def add_gravity(self):
     
        self.gravity_vel_y += 1
        if(self.gravity_vel_y > 10):
            self.gravity_vel_y = 10
        self.dy = self.gravity_vel_y

    def verificar_colision(self, lista_pisos):
        for piso in lista_pisos:
            piso : list[pygame.Rect]
            if piso[1].colliderect(self.rect.x + self.dx , self.rect.y, self.imagen_width // 1.5, self.imagen_height):# que no detecte teniendo el ancho de la img sino menos  :self.imagen_width // 1.5
                self.dx = 0
                    
            if piso[1].colliderect(self.rect.x, self.rect.y + self.dy , self.imagen_width //1.5, self.imagen_height):
                if self.gravity_vel_y < 0:
                    self.dy = piso[1].bottom - self.rect.top
                    self.gravity_vel_y = 0
                elif self.gravity_vel_y >= 0:
                    self.dy = piso[1].top - self.rect.bottom
                    self.gravity_vel_y = 0
                    self.esta_en_aire = False
        # que no salga de screen
        if self.rect.left + self.dx < 0:
            self.dx = 0
        elif self.rect.right + self.dx > ANCHO_PANTALLA:
            self.dx = 0

    def update(self, screen, index_stage):
        self.controlar_sonido_caminar()
        self.dx = self.desplazamiento_x
        self.dy = 0
        self.shotTimeState()
        self.verificar_frames()
        self.add_gravity()
        self.verificar_colision(self.lista_pisos)
        self.colison_enemigo()
        if(len(self.poder_list) > 0):
            self.poder_list[0].update(self.delta_ms)
            self.poder_list[0].verificar_colision(self.enemigo.rect, screen)
            self.poder_list[0].draw_proyectil(screen, self.orientacion_x)
    
        if(len(self.poder_list) > 0 and self.poder_list[0].tiempo_explocion <= 0):
            self.poder_list[0].tiempo_explocion = 10
            self.hacer_daño()
            self.descargar_poder()
            
        keys = pygame.key.get_pressed()
        if(index_stage == 3 and not self.control_personaje):
            print(index_stage)
            self.cambiar_animacion(self.estatico)
        if(self.control_personaje):
            if(keys[pygame.K_RIGHT]):
                
                if(keys[pygame.K_w]):
                    self.acciones('shot')
                self.acciones('caminar_r')
            elif(keys[pygame.K_LEFT]):
                
                if(keys[pygame.K_w]):
                    self.acciones('shot')
                self.acciones('caminar_l')
            else:
                self.acciones('quieto')


        self.rect.x += self.dx    
        self.rect.y += self.dy

        self.barra_vida.update(self.rect.x -2, self.rect.y, self.vida)
        if(index_stage != 3):
            self.barra_vida.draw(screen)
        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def acciones(self, accion: str, shot_en_aire = False):

        match(accion):
            case "caminar_r":
                self.caminar(accion)
            case "caminar_l":
                self.caminar(accion)
            case "saltar":
                self.saltar()
            case "quieto":
                self.quieto()
            case "shot":
                self.shot()

    def caminar(self, accion):
        if(not self.esta_en_aire and self.control_personaje):
            if(accion == "caminar_r"):
                self.orientacion_x = 1
                self.cambiar_animacion(self.corriendo_r)
                self.desplazamiento_x = self.velocidad_caminar
                self.esta_caminando = True
            else:
                self.orientacion_x = -1
                self.cambiar_animacion(self.corriendo_l)
                self.desplazamiento_x = -self.velocidad_caminar
                self.esta_caminando = True

    def controlar_sonido_caminar(self):
        if(self.esta_caminando and self.time_sound <= 0 and not self.esta_en_aire):
                self.sonido_pasos.set_volume(0.3)
                self.sonido_pasos.play()
                self.time_sound = 10
        else:
            self.time_sound -= 1

    def hacer_daño(self):
        self.enemigo.vida -= self.daño
    def saltar(self):
        if(not self.esta_en_aire and self.control_personaje):
            self.esta_en_aire = True
            self.sonido_salto_grito.play()
            self.sonido_salto_grito.set_volume(1)
            self.sonido_salto.set_volume(0.2)
            self.sonido_salto.play()
            
            if(self.orientacion_x == 1):
                self.gravity_vel_y = -self.potencia_salto
                self.cambiar_animacion(self.saltando_r)
            else:
                self.gravity_vel_y  = -self.potencia_salto
                self.cambiar_animacion(self.saltando_l)
    def cargar_poder(self):
        if(len(self.poder_list) < 1):
            self.poder_list.append(self.poder)

    def descargar_poder(self):
        if(len(self.poder_list) > 0):
            self.poder_list.pop(0)

    def shot(self):
        if(not self.esta_en_aire):
            self.cargar_poder()
            self.poder_list[0].rect.x = self.rect.x + 15 
            self.poder_list[0].rect.y = self.rect.y + 29
            self.poder_list[0].proyectil_en_aire = True
            self.control_personaje = False
            self.shot_on = True
            self.sonido_poder.play()
            self.sonido_poder.set_volume(0.1)
            self.sonido_kame.play()
            self.sonido_kame.set_volume(0.5)
            self.desplazamiento_x = 0
            if(self.orientacion_x == 1):
                self.cambiar_animacion(self.shot_r)
            else:
                self.cambiar_animacion(self.shot_l)

    def shotTimeState(self):
        if(self.shot_on and self.shot_time > 0):
            self.shot_time -= 1
            if self.shot_time <= 0:
                if(self.orientacion_x == 1):
                    self.cambiar_animacion(self.quieto_r)
                else:
                    self.cambiar_animacion(self.quieto_l)
                self.control_personaje = True
                self.shot_on = False
                self.shot_time = self.shot_time_limit

    


    def quieto(self):
        if(not self.esta_en_aire and not self.shot_on):
            self.esta_caminando = False
            if(self.orientacion_x == 1):
                self.desplazamiento_x = 0
                self.cambiar_animacion(self.quieto_r)
            elif(self.orientacion_x == -1):
                self.desplazamiento_x = 0
                self.cambiar_animacion(self.quieto_l)

    

    def cambiar_animacion(self, nueva_lista_animaciones: list[pygame.Rect]):
        self.animacion = nueva_lista_animaciones    


    def verificar_frames(self):
        '''
        El personaje se moverá y se animará correctamente con respecto 
        al tiempo transcurrido, lo que resultará en un movimiento más suave 
        y consistente sin depender de la tasa de cuadros (FPS) del juego
        
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
    def colison_enemigo(self):
            if(self.time_damage_recibido <= 0):
                if self.rect.colliderect(self.enemigo.rect):
                    self.vida -= self.enemigo.damage
                    self.time_damage_recibido = self.time_damage_recibido_limit
                    if(self.score > 0):
                        self.score -= 1000
                    else:
                        self.score = 0
            else:
                self.time_damage_recibido -= 1
    @property
    def get_dy(self):
        return self.dy
    
    @get_dy.setter
    def set_dy(self, nuevo_valor_y):
        self.dy = nuevo_valor_y
        self.rect.y += self.dy

    @property
    def get_dx(self):
        return self.dx
    
    @get_dx.setter
    def set_dx(self, nuevo_valor_x):
        self.dx = nuevo_valor_x
        self.rect.x = self.dx


    @property
    def get_rect(self):
        return self.rect
    
    @property
    def get_width(self):
        return self.imagen_width
    @property
    def get_height(self):
        return self.imagen_height
    @property
    def get_gravity_vel_y(self):
        return self.gravity_vel_y
    
    @get_gravity_vel_y.setter
    def set_gravity_vel_y(self, nuevo_valor_gravedad):
        self.gravity_vel_y = nuevo_valor_gravedad

    
    


  
