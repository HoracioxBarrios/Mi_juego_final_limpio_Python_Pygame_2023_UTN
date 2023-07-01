from auxiliar import Auxiliar
from clase_enemigo import Enemigo
import pygame as pg
from constantes import (
    ANCHO_VENTANA, DEBUG, DIRECTION_L, DIRECTION_R
)

class Player:
    def __init__(self, cantidad_balas_inicial):
        self.__lista_balas = list()
        self.recargar_balas(cantidad_balas_inicial)

    def recargar_balas(self, cantidad: int):
        for i in range(cantidad):
            self.__lista_balas.append(
                Proyectil(10, 20, 'Ruta.png', 60, 50, 15)
            )
    
    def disparar(self):
        self.__lista_balas.pop(0)


class Proyectil:

    def __init__(self, x: int, y: int, path_imagen: str, frame_rame_ms: int, move_rate_ms: int, velocidad_x: int) -> None:
        self.__proyectil_imagen = Auxiliar.getSurfaceFromSpriteSheet(
            path_imagen, 1, 1
        )
        self.__frame_actual = 0
        self.__direccion = DIRECTION_R
        self.__animacion_actual = self.__proyectil_imagen
        self.__imagen_actual = self.__animacion_actual[self.__frame_actual]
        self.__rect_proyectil = self.__imagen_actual.get_rect()
        self.__rect_proyectil.y = y
        self.__rect_proyectil.centerx = x

        self.__move_x = 0
        self.__move_y = 0

        self.__colision_rect = pg.Rect(self.__rect_proyectil)

        self.__tiempo_transcurrido_animacion = 0
        self.__frame_rate_ms = frame_rame_ms
        
        self.__tiempo_transcurrido_movim = 0
        self.__move_rate_ms = move_rate_ms

        self.__velocidad_x = velocidad_x

    @property
    def rect_colision(self) -> pg.Rect:
        return self.__colision_rect

    def colisiono_enemigo(self, lista_enemigos: list[Enemigo]) -> bool:
        for enemigo in lista_enemigos:
            if self.__colision_rect.colliderect(enemigo.get_rect_colision()):
                return True
        return False
    
    def colisiono_player(self, lista_players: list[Player]) -> bool:
        for player in lista_players:
            if self.__colision_rect.colliderect(player.get_rect_colision()):
                return True
        return False
    
    def colisiono_personaje(self, lista_personajes: list[Player | Enemigo]):
        for personaje in lista_personajes:
            if self.__colision_rect.colliderect(personaje.get_rect_colision()):
                return True
        return False
    
    def colisiono_pantalla(self, direccion: str) -> bool:
        match direccion:
            case 'izq':
                if self.__rect_proyectil.x == 3:
                    return True
            case 'der':
                if self.__rect_proyectil.centerx - 3 >= ANCHO_VENTANA:
                    return True
        return False
    
    def desplazar_en_x(self, direccion: int) -> None:
        match direccion:
            case 0: # izq
                self.__move_x = -self.__velocidad_x
            case 1: # der
                self.__move_x = self.__velocidad_x
        self.__animacion_actual = self.__proyectil_imagen

    def destruir_proyectil(self, lista_enemigos: list[Enemigo], lista_proyectiles: list) -> bool:

        for proyectil in lista_proyectiles:
            if self.colisiono_pantalla('der') or\
                self.colisiono_pantalla('izq') or\
                self.colisiono_enemigo(lista_enemigos):
                return True
        return False
    
    def destruir_personaje(self, lista_proyectiles, lista_personajes: list[Player | Enemigo]) -> bool:
        for proyectil in lista_proyectiles:
            if self.colisiono_pantalla('der') or\
                self.colisiono_pantalla('izq') or\
                self.colisiono_personaje(lista_personajes):
                return True
        return False
    
    def __cambio_eje_x(self, delta_x):
        self.__rect_proyectil.x += delta_x
        self.__colision_rect.x += delta_x
    
    def __cambio_eje_y(self, delta_y):
        self.__rect_proyectil.y += delta_y
        self.__colision_rect.y += delta_y

    def __hacer_animacion(self, delta_ms) -> None:
        self.__tiempo_transcurrido_animacion += delta_ms
        if self.__tiempo_transcurrido_animacion >= self.__frame_rate_ms:
            self.__tiempo_transcurrido_animacion = 0
            if self.__frame_actual < (len(self.__animacion_actual) - 1):
                self.__frame_actual += 1
            else:
                self.__frame_actual = 0
    
    def __generar_movimiento(self, delta_ms) -> None:
        self.__tiempo_transcurrido_movim += delta_ms
        if self.__tiempo_transcurrido_movim >= self.__move_rate_ms:
            self.__tiempo_transcurrido_movim = 0
            self.__cambio_eje_y(self.__move_y)
            self.__cambio_eje_x(self.__move_x)
    
    def update(self, display: pg.Surface, delta_ms: int, lista_personajes: list[Enemigo | Player], lista_proyectiles: list) -> None:
        self.__rect_proyectil.x += self.__velocidad_x
        self.__generar_movimiento(delta_ms)
        self.__hacer_animacion(delta_ms)
        self.desplazar_en_x(self.__direccion)
        if not self.destruir_personaje(lista_proyectiles, lista_personajes):
            self.__draw(display)

    def __draw(self, display: pg.Surface):
        if DEBUG:
            pg.draw.rect(display, color=(255, 0, 0), rect=self.__colision_rect)
        self.__imagen_actual = self.__animacion_actual[self.__frame_actual]
        display.blit(self.__imagen_actual, self.__rect_proyectil)
