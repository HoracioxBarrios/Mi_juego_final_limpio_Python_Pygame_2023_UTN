import random
from auxiliar import Auxiliar
import pygame as pg

from constantes import ANCHO_VENTANA, DEBUG, DIRECTION_L, DIRECTION_R, GROUND_COLLIDE_H, GROUND_LEVEL

class Enemigo:

    def __init__(self, x: int, y: int, personaje: str, columna_walk: int, columna_idle, columna_hit, columna_attack, columna_caida, columna_salto, speed_walk, speed_run, gravedad, poder_salto, frame_rate_ms, move_rate_ms, alto_salto, p_scala=1, intervalo_salto=150) -> None:
        self.__walk_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_walk, 1)
        self.__walk_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_walk, 1, flip=True)
        self.__stay_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_idle, 1)
        self.__stay_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_idle, 1, flip=True)
        self.__hit_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_hit, 1)
        self.__hit_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_hit, 1, flip=True)
        self.__jump_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_salto, 1)
        self.__jump_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_salto, 1, flip=True)
        self.__caida_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_caida, 1)
        self.__caida_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_caida, 1, flip=True)
        self.__ataque_r = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_attack, 1)
        self.__ataque_l = Auxiliar.getSurfaceFromSpriteSheet("ruta_de_la_imagen/{0}/Run.png".format(personaje), columna_attack, 1, flip=True)

        self.__frame = 0
        self.__move_x = 0
        self.__move_y = 0
        self.__orientacion = 0

        self.__cadencia = 250
        self.__ultimo_disparo = pg.time.get_ticks()

        self.__velocidad_correr = speed_run
        self.__gravedad_enemigo = gravedad
        self.__poder_salto = poder_salto
        self.__animacion_actual = self.__stay_l

        self.__direccion = random.randint(0 ,1)
        self.__velocidad_caminata = speed_walk

        self.__imagen = self.__animacion_actual[self.__frame]
        self.__rect = self.__imagen.get_rect()
        self.__rect.x = x
        self.__rect.y = y

        self.__rect_colision = pg.Rect(
            x+self.__rect.width/3,
            y, self.__rect.width/3,
            self.__rect.height
            )
        self.__rect_colision.height = 30
        self.__rect_colision.width = 30
        self.__rect_colision.x = self.__rect.x
        self.__rect_colision.y = y

        self.__piso_colision_rect = pg.Rect(self.__rect_colision)
        self.__piso_colision_rect.height = GROUND_COLLIDE_H
        self.__piso_colision_rect.y = y + self.__rect.height - GROUND_COLLIDE_H

        self.__techo_colision_rect = pg.Rect(self.__rect_colision)
        self.__techo_colision_rect.height = 10
        self.__techo_colision_rect.width = 30
        self.__techo_colision_rect.x = self.__rect.x
        self.__techo_colision_rect.y = y

        # self.__sonido_ataque = pg.mixer.Sound("ruta_a_audio.mp3")

        self.__esta_saltando = False
        self.__esta_cayendo = False
        self.__tiempo_transcurrido_animacion = 0
        self.__move_rate_ms = move_rate_ms
        self.__eje_y_start_salto = 0
        self.__altura_salto = alto_salto

        self.__tiempo_transcurrido = 0
        self.__tiempo_ultimo_salto = 0
        self.__intervalo_salto = intervalo_salto

    def caminar(self, direccion: int) -> None:
        match direccion:
            case 0:
                self.__animacion_actual = self.__walk_r
                self.__move_x = self.__velocidad_caminata
            case 1:
                self.__animacion_actual = self.__walk_l
                self.__move_x = -1 * self.__velocidad_caminata
    
    def golpear(self, direccion: int) -> None:
        match direccion:
            case 0:
                self.__animacion_actual = self.__hit_r
            case 1:
                self.__animacion_actual = self.__hit_l
        
        self.__move_x = 0
        self.__move_y = 0
        self.__frame = 0
    
    def saltar(self, on_off = True) -> None:
        if on_off and not self.__esta_saltando and not self.__esta_cayendo:
            self.__eje_y_start_salto = self.__rect.y
            self.__move_x = int(self.__move_x/2)

            if self.__direccion == DIRECTION_R:
                self.__move_y = self.__poder_salto
                self.__animacion_actual = self.__jump_r
            else:
                self.__move_y = -self.__poder_salto
                self.__animacion_actual = self.__jump_l
            self.__frame = 0
            self.__esta_saltando = True
        if not on_off:
            self.__esta_saltando = on_off
            self.de_pie()
    
    def de_pie(self) -> None:
        if self.__animacion_actual != self.__stay_r and\
            self.__animacion_actual != self.__stay_l:
            if self.__direccion == DIRECTION_R:
                self.__animacion_actual = self.__stay_r
            else:
                self.__animacion_actual = self.__stay_l
            self.__frame = 0
            self.__move_x = 0
            self.__move_y = 0
    
    def movimiento_random(self):
        if self.__direccion == DIRECTION_R:
            self.caminar(self.__direccion)
            if self.__rect.x >= ANCHO_VENTANA - 20:
                self.golpear(self.__direccion)

        elif self.__direccion == DIRECTION_L:
            self.caminar(self.__direccion)
            if self.__rect.x == 40:
                self.golpear(self.__direccion)
    
    def movimiento_hacia_player(self, lista_player):
        for player in lista_player:
            if self.__rect.x <= player.rect.x:
                self.__orientacion = DIRECTION_R
                self.__animacion_actual = self.__stay_r
            if self.__rect.x > player.rect.x:
                self.__orientacion = DIRECTION_L
                self.__animacion_actual = self.__stay_l
    
    def __cambio_eje_x(self, delta_x):
        self.__rect.x += delta_x
        self.__rect_colision.x += delta_x
        self.__piso_colision_rect.x += delta_x
        self.__techo_colision_rect.x += delta_x
    
    def __cambio_eje_y(self, delta_y):
        self.__rect.y += delta_y
        self.__rect_colision.y += delta_y
        self.__piso_colision_rect.y += delta_y
        self.__techo_colision_rect.y += delta_y
    
    def esta_en_plataforma(self, lista_plataformas) -> bool:
        if self.__piso_colision_rect.bottom >= GROUND_LEVEL:
            return True
        else:
            for plataforma in lista_plataformas:
                if self.__piso_colision_rect.colliderect(plataforma.rect_colision_piso):
                    return True
        return False
    
    def __generar_movimiento(self, delta_ms, lista_plataformas):
        self.__tiempo_transcurrido += delta_ms

        if self.__tiempo_transcurrido >= self.__move_rate_ms:
            self.__tiempo_transcurrido = 0

            # Chequear algo del salto
            if abs(self.__eje_y_start_salto - self.__rect.y) > self.__altura_salto and self.__esta_saltando:
                self.__move_y = 0
            
            self.__cambio_eje_y(self.__move_y)
            self.__cambio_eje_x(self.__move_x)

            if not self.esta_en_plataforma(lista_plataformas):
                if self.__move_y == 0:
                    self.__esta_cayendo = True
                    self.__cambio_eje_y(self.__gravedad_enemigo)
            else:
                if self.__esta_saltando:
                    self.saltar(False)
                self.__esta_cayendo = False

    def __fue_vencido(self, lista_player, lista_proyectiles) -> bool:
        retorno = False
        # chequear impacto con un proyectil
        for player in lista_player:
            for proyectil in lista_proyectiles:
                if self.__rect_colision.colliderect(proyectil.rect_colision):
                    self.golpear(self.__direccion)
                    player.puntos += 70
                    retorno = True
            if self.__techo_colision_rect.colliderect(player.__piso_colision_rect):
                self.golpear(self.__direccion)
                player.puntos += 100
                retorno = True

        # Chequeamos que el player nos este pisando
        # for player in lista_player:
        #     if self.__techo_colision_rect.colliderect(player.__piso_colision_rect):
        #         self.golpear(self.__direccion)
        #         player.puntos += 100
        #         retorno = True

        return retorno
    
    def __hacer_animacion(self, delta_ms) -> None:
        self.__tiempo_transcurrido_animacion += delta_ms
        if self.__tiempo_transcurrido_animacion >= self.__move_rate_ms:
            self.__tiempo_transcurrido_animacion = 0
            if self.__frame < (len(self.__animacion_actual) - 1):
                self.__frame += 1
            else:
                self.__frame = 0
    
    def update(self, display, delta_ms, lista_plataformas, lista_jugadores, lista_proyectiles) -> None:
        """
        Actualiza el movimiento y animación del enemigo, en caso de haber sido impactado, realizara
        la animación y movimiento de golpear/atacar.
        
        Param:
            delta_ms: El tiempo transcurrido del juego.
            lista_plataformas: Es la lista de las platformas disponible en el nivel.
            lista_jugadores: Es la lista de jugadores actuales en el nivel.
            lista_proyectiles: Es la lista de proyectiles de los jugadores actuales en el nivel.
        Retorno: None
        """
        self.__generar_movimiento(delta_ms, lista_plataformas)
        self.__hacer_animacion(delta_ms)
        self.__fue_vencido(lista_jugadores, lista_proyectiles)
        self.__draw(display)
    
    def __draw(self, display: pg.Surface) -> None:
        if DEBUG:
            pg.draw.rect(display, color=(255, 0, 0), rect=self.__rect_colision)
        self.__imagen = self.__animacion_actual[self.__frame]
        display.blit(self.__imagen, self.__rect)

