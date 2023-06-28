import pygame
pygame.mixer.init()

from utilidades import *
from configuracion import *
from pydub import AudioSegment
from pydub.playback import play
from proyectil import Proyectil
from enemigo_old import Enemigo
sonido_pasos = pygame.mixer.Sound('sonido\correr.wav')
sonido_poder = pygame.mixer.Sound('sonido\poder.wav')
sonido_kame = pygame.mixer.Sound("sonido\kame.wav")
sonido_salto = pygame.mixer.Sound('sonido\salto.wav')
sonido_salto_grito = pygame.mixer.Sound("sonido\salto_voz.wav")
sonido_explosion = pygame.mixer.Sound("sonido\explocion.wav")
class Personaje:
    def __init__(self) -> None:
        self.quieto_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, True)
        self.quieto_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 0, 2, False)
        self.corriendo_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, False)
        self.corriendo_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 8, True)
        self.saltando_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, False)#para recortar una sola imagen, se ponen el desde y el hasta con el mismo valor
        self.saltando_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 0, 6, 6, True)
        self.shot_r = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, True)
        self.shot_l = get_surface_form_sprite_sheet("asset\goku2.png", 9, 6, 5, 3, 5, False)
        self.frame = 0
        self.velocidad_caminar = 7
        self.potencia_salto = 20
        self.limite_altura_salto = 6
        ###########################
        self.desplazamiento_x = 0
        self.desplazamiento_y = 0
        self.gravity_vel_y = 0 
        ############################
        self.esta_caminando = False
        self.orientacion_x = 1
        self.esta_en_aire = False
        self.control_personaje = True
        self.shot_on = False
        self.shot_time = 30
        self.shot_time_limit = 30
        self.proyectil_frame = 0
        self.proyectil_en_aire = False
        self.dx = 0
        self.dy = 0
        self.limites_frames_por_segundo  = 10
        # self.time_frame = 10
        self.proyectil_colisiono = False
        ############################
        self.time_sound = 20
        #Creacion inicial del rectangulo con superficie
        self.animacion = self.quieto_r
        self.imagen = self.animacion[self.frame]#el frame inicia arranca en 0, por ende se renderiza la pocision 0 de la lista de animaciones
        self.ancho_imagen = self.imagen.get_width()
        self.alto_imagen = self.imagen.get_height()
        self.rectangulo_principal = self.imagen.get_rect()
        ################################
        self.pos_x = 0
        self.pos_y = 0
        self.rectangulo_principal.x = 50
        self.rectangulo_principal.y = 650
        ################################
        self.diccionario_rectangulo_colisiones = obtener_rectangulos_colision(self.rectangulo_principal)

        self.proyectil = Proyectil(self.orientacion_x, 0, 0)
        #enemigo
        self.frame_enemigo = 0
        self.pos_enemigo_x = 800
        self.pos_enemigo_y =  400
        self.enemigo = Enemigo(self.pos_enemigo_x, self.pos_enemigo_y, 40)
        self.time_frame = 10
        self.time_frame_limit = 10
        self.direccion_enemigo = 1
        self.imagenes_enemigo = self.enemigo.animacion_l[self.frame_enemigo]
        self.enemigo_time_respawn_limit = 500
        self.enemigo_time_respawn = 500
        self.enemigo_respawn = True
        self.dy_enemigo = 0
        self.dx_enemigo = 0
        self.gravity_vel_y_enemigo = 0
        self.desplazamiento_x_enemigo = 0
    def acciones(self, accion: str):

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
                sonido_pasos.set_volume(0.3)
                sonido_pasos.play()
                self.time_sound = 7
        else:
            self.time_sound -= 1
            
    def saltar(self):
        if(not self.esta_en_aire and self.control_personaje):
            self.esta_en_aire = True
            sonido_salto_grito.play()
            sonido_salto_grito.set_volume(0.8)
            sonido_salto.set_volume(0.2)
            sonido_salto.play()
            if(self.orientacion_x == 1):
                self.gravity_vel_y = -self.potencia_salto
                self.cambiar_animacion(self.saltando_r)
            else:
                self.gravity_vel_y  = -self.potencia_salto
                self.cambiar_animacion(self.saltando_l)


    def quieto(self):
        if(not self.esta_en_aire and not self.shot_on):
            self.esta_caminando = False
            if(self.orientacion_x == 1):
                self.desplazamiento_x = 0
                self.cambiar_animacion(self.quieto_r)
            elif(self.orientacion_x == -1):
                self.desplazamiento_x = 0
                self.cambiar_animacion(self.quieto_l)

    def shot(self):
        if(not self.esta_en_aire):
            self.control_personaje = False
            self.shot_on = True
            sonido_poder.play()
            sonido_poder.set_volume(0.2)
            sonido_kame.play()
            sonido_kame.set_volume(0.9)
            self.desplazamiento_x = 0
            if(self.orientacion_x == 1):
                self.cambiar_animacion(self.shot_r)
            else:
                self.cambiar_animacion(self.shot_l)
            

    def updater(self, screen_height, pisos, screen):
        self.controlar_sonido_caminar()

        self.dx = self.desplazamiento_x
        self.dy = 0

        #enemigo pos
        self.dx_enemigo = self.desplazamiento_x_enemigo
        self.dy_enemigo = 0

        if(self.shot_on and self.shot_time > 0):
            self.proyectil_frame += 1
            self.shot_time -= 1
            if self.shot_time <= 0:
                if(self.orientacion_x == 1):
                    self.cambiar_animacion(self.quieto_r)
                else:
                    self.cambiar_animacion(self.quieto_l)
                self.control_personaje = True
                self.shot_on = False
                self.shot_time = self.shot_time_limit

            
        ###################
        self.gravity_vel_y += 1
        ###################
        if self.gravity_vel_y > 10:
            self.gravity_vel_y = 10
        ###################
        self.dy += self.gravity_vel_y

        ######### ENEMIGO ##########
        self.gravity_vel_y_enemigo += 1
        ###################
        if self.gravity_vel_y_enemigo > 10:
            self.gravity_vel_y_enemigo = 10

        self.dy_enemigo += self.gravity_vel_y_enemigo
        ###################

        if(self.dy > 1):
            self.esta_en_aire = True
            if(self.orientacion_x == 1):
                self.cambiar_animacion(self.saltando_r)
            else:
                self.cambiar_animacion(self.saltando_l)
        
        if(self.shot_on):
            if self.enemigo.rectangulo_principal.colliderect(self.proyectil.rectangulo_principal):
                if(self.orientacion_x == 1):
                        self.proyectil.rectangulo_principal.x = self.enemigo.rectangulo_principal.x - 50
                        self.enemigo.set_damage(self.proyectil.damage)
                        self.proyectil_colisiono = True
                else:
                        self.proyectil.rectangulo_principal.x = self.enemigo.rectangulo_principal.x
                        self.enemigo.set_damage(self.proyectil.damage)
                        self.proyectil_colisiono = True

        ######### COLISION PROYECTIL
        for piso in pisos:
            if piso[1].colliderect(self.proyectil.rectangulo_principal):
               if(self.orientacion_x == 1):
                    self.proyectil.rectangulo_principal.x = piso[1].x - 50
                    self.proyectil_colisiono = True
               else:
                    self.proyectil.rectangulo_principal.x = piso[1].x
                    self.proyectil_colisiono = True

        ############ COLISION ENEMIGO
            if piso[1].colliderect(self.enemigo.rectangulo_principal.x + self.dx_enemigo, self.enemigo.rectangulo_principal.y, self.enemigo.alto_imagen, self.enemigo.alto_imagen):
                self.dx_enemigo= 0
                
            #Corroboramos colision en Y
            if piso[1].colliderect(self.enemigo.rectangulo_principal.x, self.enemigo.rectangulo_principal.y + self.dy_enemigo, self.enemigo.ancho_imagen, self.enemigo.alto_imagen):
                # corroboramos en el salto 
                if self.enemigo.vel_y < 0:
                    self.dy_enemigo = piso[1].bottom - self.enemigo.rectangulo_principal.top
                    self.enemigo.vel_y  = 0
                # corroboramos en la caida
                elif self.enemigo.vel_y  >= 0:
                    self.dy_enemigo = piso[1].top - self.enemigo.rectangulo_principal.bottom
                    self.enemigo.vel_y  = 0
                    # self.esta_en_aire = False

        ############# COLISION PERSONAJE CON BLOCKS
        #Corroboramos colision en X
            if piso[1].colliderect(self.rectangulo_principal.x + self.dx, self.rectangulo_principal.y, self.ancho_imagen, self.alto_imagen):
                self.dx = 0
                
            #Corroboramos colision en Y
            if piso[1].colliderect(self.rectangulo_principal.x, self.rectangulo_principal.y + self.dy, self.ancho_imagen, self.alto_imagen):
                # corroboramos en el salto 
                if self.gravity_vel_y < 0:
                    self.dy = piso[1].bottom - self.rectangulo_principal.top
                    self.gravity_vel_y = 0
                # corroboramos en la caida
                elif self.gravity_vel_y >= 0:
                    self.dy = piso[1].top - self.rectangulo_principal.bottom
                    self.gravity_vel_y = 0
                    self.esta_en_aire = False
                    

        #######################
        self.rectangulo_principal.y += self.dy
        self.rectangulo_principal.x += self.dx
        ######### ENEMIGO ################
        self.enemigo.rectangulo_principal.x += self.dx_enemigo
        self.enemigo.rectangulo_principal.y += self.dy_enemigo

        if self.rectangulo_principal.bottom > screen_height:
            self.rectangulo_principal.bottom = screen_height
            self.dy = 0

        self.dibujar_en_pantalla(screen)
        

    def dibujar_en_pantalla(self, screen):
        #Dibujar personaje
        self.verificar_frames()
        screen.blit(self.imagen, self.rectangulo_principal)
        #dibujar enemigo
        print(self.enemigo.vida)
        if(self.enemigo.get_vida() > 0 and self.enemigo_respawn):
            if(self.time_frame <= 0):
                if(self.frame_enemigo < len(self.enemigo.animacion_l) -1):
                    self.frame_enemigo += 1
                    self.time_frame = self.time_frame_limit
                else:
                    self.frame_enemigo = 0
            else:
                self.time_frame -= 1
            self.desplazamiento_x_enemigo = -5
            # if self.enemigo.rectangulo_principal.x >= 50 and self.direccion_enemigo == 1:
            #     
            #     self.imagenes_enemigo = self.enemigo.animacion_l[self.frame_enemigo]
            # elif self.enemigo.rectangulo_principal.x <= screen.get_width() - 100 and self.direccion_enemigo == -1:
            #     self.imagenes_enemigo = self.enemigo.animacion_r[self.frame_enemigo]
            #     self.desplazamiento_x_enemigo += 5
            # else:
            #     # Cambiar la dirección cuando se alcanza un límite
            #     self.direccion_enemigo *= -1
            screen.blit(self.imagenes_enemigo, self.enemigo.rectangulo_principal)
        else:
            self.enemigo.enemigo_murio()
            self.enemigo_respawn = False
            self.enemigo.rectangulo_principal.x = self.pos_enemigo_x
            self.enemigo.rectangulo_principal.y = self.pos_enemigo_y
            if(self.enemigo_time_respawn <= 0):
                self.enemigo_respawn = True
                self.enemigo.set_vida(40)
                self.enemigo_time_respawn = self.enemigo_time_respawn_limit
            else:
                self.enemigo_time_respawn -= 1


        #dibujar proyectil
        if(self.shot_on):
            #incia en proyectil
            if(self.proyectil_frame < len(self.proyectil.animacion_r) - 1):
                #se comprueba que el frame no sea mayor al len de la lista
                self.proyectil.rectangulo_principal.y = self.rectangulo_principal.y + 35
                if(not self.proyectil_en_aire and self.orientacion_x == 1):#verifica que no haya otro proyectil y la orientacion
                    self.proyectil_en_aire = True
                    posicion_inicial = self.rectangulo_principal.right - 70
                    self.proyectil.rectangulo_principal.x = posicion_inicial
                elif(not self.proyectil_en_aire and self.orientacion_x == -1):#verifica que no haya otro proyectil y la orientacion
                    self.proyectil_en_aire = True
                    posicion_inicial = self.rectangulo_principal.left - 20
                    self.proyectil.rectangulo_principal.x = posicion_inicial
                    #orientacion r
                if(self.orientacion_x == 1): 
                    imagenes = self.proyectil.animacion_r[self.proyectil_frame]
                    self.proyectil.rectangulo_principal.x += 10
                    if(self.proyectil_colisiono):
                        imagenes = self.proyectil.explocion[self.proyectil_frame]
                        sonido_explosion.play()
                        sonido_explosion.set_volume(0.1)
                else:
                    #orientacion l
                    imagenes = self.proyectil.animacion_l[self.proyectil_frame]
                    self.proyectil.rectangulo_principal.x -= 10
                    if(self.proyectil_colisiono):
                        imagenes = self.proyectil.explocion[self.proyectil_frame]
                        sonido_explosion.play()
                        sonido_explosion.set_volume(0.1)
                screen.blit(imagenes, self.proyectil.rectangulo_principal)
            else:
                self.proyectil_frame = 0
                self.proyectil_colisiono = False
        else:
            self.proyectil.rectangulo_principal.x = 0
            self.proyectil_en_aire = False
          

        

    def verificar_frames(self):
        if(self.time_frame <= 0):
            if(self.frame < len(self.animacion)):
                self.imagen = self.animacion[self.frame]
                self.time_frame = self.limites_frames_por_segundo
                self.frame += 1
            else:
                self.frame = 0
        else:
            self.time_frame -= 1
    def cambiar_animacion(self, nueva_lista_animaciones: list[pygame.Rect]):
        self.animacion = nueva_lista_animaciones

        