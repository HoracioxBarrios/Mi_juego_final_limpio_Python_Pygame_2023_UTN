import pygame, sys
import json
import re
from vid.pyvidplayer import Video
def get_surface_form_sprite_sheet(path : str, columnas : int, filas : int, cortar_en_fila: int, cortar_columna_desde=0, cortar_columna_hasta=0, flip=False):
    """
    Obtiene una lista de superficies de imagen a partir de un sprite sheet.
    Recibe:
        Args:
        - path (str): Ruta de la imagen sprite sheet.
        - columnas (int): Número de columnas en el sprite sheet.
        - filas (int): Número de filas en el sprite sheet.
        - cortar_en_fila (int): Número de fila a cortar.
        - cortar_columna_desde (int, opcional): Columna desde la cual cortar 
        (por defecto es 0).
        - cortar_columna_hasta (int, opcional): Columna hasta la cual cortar 
        (por defecto es 0).
        - flip (bool, opcional): Indica si se debe voltear horizontalmente los 
        fotogramas (por defecto es False).

    Devuelve:
    - lista (list): Lista de superficies de imagen correspondientes a los 
    fotogramas individuales.
    """
    lista = []
    superficie_imagen = pygame.image.load(path)

    fotograma_ancho = int(superficie_imagen.get_width()/columnas)
    fotograma_alto = int(superficie_imagen.get_height()/filas)

    for columna in range(cortar_columna_desde, cortar_columna_hasta + 1):
        x = fotograma_ancho * columna
        y = fotograma_alto * cortar_en_fila
        superficie_fotograma = superficie_imagen.subsurface(
            x, y, fotograma_ancho, fotograma_alto)
        # superficie_fotograma = pygame.transform.scale(superficie_fotograma, (fotograma_ancho * 3, fotograma_alto * 3))
        if flip:
            superficie_fotograma = pygame.transform.flip(
                superficie_fotograma, True, False)
        lista.append(superficie_fotograma)

    return lista


def get_surface_individual_imagen(path, flip, cant_imagens):
    """
    Obtiene una lista de superficies de imagen a partir de imágenes individuales.

    Parámetros:
    - path (str): Ruta de la imagen.
    - flip (bool): Indica si se debe voltear horizontalmente las imágenes.
    - cant_imagens (int): Cantidad de imágenes individuales.

    Retorna:
    - lista (list): Lista de superficies de imagen correspondientes a las imágenes individuales.
    """

    lista = []
    for index_imagen in range(cant_imagens):
        patron = r'\d+'
        resultado = re.sub(patron, str(index_imagen), path)
        superficie_imagen = pygame.image.load(resultado)
        fotograma_ancho = int(superficie_imagen.get_width()/1)
        fotograma_alto = int(superficie_imagen.get_height()/1)
        x = fotograma_ancho
        y = fotograma_alto
        superficie_fotograma = superficie_imagen.subsurface(x, y, fotograma_ancho, fotograma_alto)
        # if flip:
        #     superficie_fotograma = pygame.transform.flip(
        #         superficie_fotograma, True, False)
        # lista.append(superficie_fotograma)
        
def obtener_rectangulos_colision(rectangulo_principal: pygame.Rect):
    """
    Obtiene un diccionario con los rectángulos de colisión de un rectángulo principal.

    Parámetros:
    - rectangulo_principal (pygame.Rect): Rectángulo principal.

    Retorna:
    - dicc_rectangulos_lados (dict): Diccionario con los rectángulos de colisión de cada lado.
    """
    dicc_rectangulos_lados = {}
    dicc_rectangulos_lados["main"]: dict[pygame.Rect] = rectangulo_principal
    dicc_rectangulos_lados["lado_abajo"]: dict[pygame.Rect] = pygame.Rect(
        rectangulo_principal.left, rectangulo_principal.bottom - 10, rectangulo_principal.width, 10)
    dicc_rectangulos_lados["lado_derecha"]: dict[pygame.Rect] = pygame.Rect(
        rectangulo_principal.right - 10, rectangulo_principal.top,  10, rectangulo_principal.height)
    dicc_rectangulos_lados["lado_izquierda"]: dict[pygame.Rect] = pygame.Rect(
        rectangulo_principal.left, rectangulo_principal.top, 10, rectangulo_principal.height)
    dicc_rectangulos_lados["lado_arriba"]: dict[pygame.Rect] = pygame.Rect(
        rectangulo_principal.left, rectangulo_principal.top, rectangulo_principal.width, 10)
    return dicc_rectangulos_lados




def obtener_ractangulo_principal(superficies, frame):
    """
    Obtiene el rectángulo principal de una lista de superficies de imagen.

    Parámetros:
    - superficies (list): Lista de superficies de imagen.
    - frame (int): Índice del frame para obtener el rectángulo principal.

    Retorna:
    - rectangulo_principal (pygame.Rect): Rectángulo principal correspondiente al frame dado.
    """
    animaciones = []
    animaciones = superficies
    imagen = animaciones[frame]
    rectangulo_principal = imagen.get_rect()
    return rectangulo_principal


def dibujar_grid(screen : pygame.Surface, color : any, tile_size : int, width_screen: int, height_screen : int, margen : int):
    """
    Dibuja una cuadrícula en la pantalla.
    Recibe :
        Args:
        - screen: Superficie de la pantalla de juego.
        - color: Color de las líneas de la cuadrícula.
        - tile_size: Tamaño de los tiles en la cuadrícula.
        - width_screen: Ancho de la pantalla.
        - height_screen: Alto de la pantalla.
        - margen: Margen de la cuadrícula.

    Retorna:
    - None
    """
    for c in range(21):
		#vertical lines
        pygame.draw.line(screen, color, (c * tile_size, 0), (c * tile_size, height_screen - margen))
        #horizontal lines
        pygame.draw.line(screen, color, (0, c * tile_size), (width_screen, c * tile_size))

def leerJson(path : str)-> dict:
    """
    Lee el contenido de un archivo JSON.
    Recibe:
    Args:
    - path (str): Ruta del archivo JSON.

    Retorna:
    - contenido (dict): Contenido del archivo JSON en forma de diccionario.
    """
    with open(path, 'r') as archivo:
        contenido = json.load(archivo)
    return contenido



def cambiar_musica(path : str, vol= 0.4)-> None:
    """
    Cambia la música del juego.
    Recibe:
    Args:
    - path (str): Ruta del archivo de música.
    - vol (float, opcional): Volumen de la música (por defecto es 0.4).

    Retorna:
    - None
    """
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(vol)


def intro_transition(path : str, screen : pygame.Surface)-> None:
    """
    Muestra una transición de introducción utilizando un video.
    Recibe:
        Args:
        - path (str): Ruta del archivo de video.
        - screen: Superficie de la pantalla de juego.

    Retorna: None
    """
    vid = Video(path)
    vid.set_size((screen.get_width(), screen.get_height()))
    vid.set_volume(0.5)
    pygame.mixer.music.stop()
    running = True
    while running:
        pygame.display.update()
        if vid.active == True:
            print(vid.active)
            vid.draw(screen, (0, 0))
        else:
            print(vid.active)
            vid.close()
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         vid.close()







def transicion_stages(path_vid_transicion : str, to_play : bool)-> None:
    '''
    Realiza una transición entre etapas mostrando un video de transición.
    Recibe :
        Args:
        path_vid_transicion (str): Ruta del archivo de video de transición.
        to_play (bool): Indica si se debe reproducir el juego después de la transición.

    Devuelve: None
    '''
    vid = Video(path_vid_transicion)
    # vid.set_size((ANCHO_PANTALLA, ALTO_PANTALLA))
    # runnig = True
    # while runnig:
    #     if vid.active:
    #         vid.draw(SCREEN, (0, 0))
    #     else:
    #         print("se cerro e vid")
    #         vid.close()
    #     pygame.display.update()
    # if to_play:
    #     lista_game_over_respuesta = game()
    #     resp_game_over = lista_game_over_respuesta[0]
    #     list_resp_score_game = lista_game_over_respuesta[1]
    #     if resp_game_over == "Game Over":
    #         over_game.show_game_over(resp_game_over, main_menu, list_resp_score_game)
    #     else:# Win
    #         over_game.show_game_over(resp_game_over, main_menu, list_resp_score_game)