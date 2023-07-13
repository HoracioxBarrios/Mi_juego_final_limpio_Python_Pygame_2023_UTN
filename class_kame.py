import pygame
from utilidades import get_surface_form_sprite_sheet
class Kame:
    '''
    Representa al poder kame hame ha, para la ultima instancia del juego.
    lo puede usar el personaje como el enemigo.
    '''
    def __init__(self, screen : pygame.Surface,ancho_bar : int, alto_bar: int,poder_enemigo : int, poder_personaje :int, pos_x : int, pos_y : int)-> None:
        """
        Inicializa una instancia de la clase Kame.
        Recibe:
            Args:
            screen (pygame.Surface): La superficie de la pantalla del juego.
            ancho_bar (int): El ancho inicial de la barra.
            alto_bar (int): El alto de la barra.
            poder_enemigo (int): El poder del enemigo.
            poder_personaje (int): El poder del personaje.
            pos_x (int): La posición inicial en el eje X.
            pos_y (int): La posición inicial en el eje Y.
        Devuelve. None
        """
        self.choque_list = get_surface_form_sprite_sheet("asset\choque\choque_set.png", 3, 1, 0, 0, 2, False)
        self.frame = 0
        self.image_choque = self.choque_list [self.frame]
        self.rect_choque = self.image_choque.get_rect()
        self.rect_choque.x = 0
        self.rect_choque.y = 0
        #goku
        self.image_goku = pygame.image.load("asset\goku_poder_final.png")
        self.image_goku = pygame.transform.scale(self.image_goku, (182, 155))
        self.rect_goku = self.image_goku.get_rect()
        self.rect_goku.x = 0
        self.rect_goku.y = 465
        #jacky chun
        self.image_jack = pygame.image.load("asset\jacky_poder_final.png")
        self.image_jack = pygame.transform.scale(self.image_jack, (182,155))
        self.rect_jack  = self.image_goku.get_rect()
        self.rect_jack .x = 820
        self.rect_jack .y = 465

        self.ancho = ancho_bar
        self.alto = alto_bar
        self.poder_enemigo = poder_enemigo
        self.poder_personaje = poder_personaje
        self.screen = screen
        self.ancho_bar_2 = ancho_bar

        self.image_1 = pygame.Surface((self.ancho / 2, self.alto))
        self.image_1.fill((64, 144, 244))
        self.rect = self.image_1.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        self.caida_kame = 5 # representa el poder de jaki en su kame ha que viene hacia goku
        self.aumento_kame = 40 #representa el contraresto del kame ha . goku contraresta el kame de jaki
        self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
        self.image_2.fill((39, 117, 211))
        self.rect_2 = self.image_2.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.limit_power_screen = screen.get_width()
        self.time_render = 5
        self.time_render_limit = 5
        self.color_texto = (238, 51, 10)
        self.tamanio_fuente = 45
        self.type_fuente = "Impact"
        self.fuente = pygame.font.SysFont(self.type_fuente, self.tamanio_fuente)

    def draw(self, screen : pygame.Surface)-> None:
        """
        Dibuja los elementos del personaje y enemigo en la pantalla del juego.
        Recibe:
            Args:
            screen (pygame.Surface): La superficie de la pantalla del juego.
        Devuelve: None
        """
        screen.blit(self.image_goku, self.rect_goku)
        screen.blit(self.image_jack, self.rect_jack)
        screen.blit(self.image_2, self.rect) # Azul Roshi
        screen.blit(self.image_1, self.rect)# celeste Goku 
        self.verificar_frames()
        self.draw_choque()
        if(self.time_render > 0):
            text = self.fuente.render("PRESS E!!", True, self.color_texto)
            screen.blit(text, (100,530))
            self.time_render -= 1
        else:
            self.time_render = self.time_render_limit
            

    def update(self)-> None:
        """
        Actualiza el objeto y realiza las acciones correspondientes.
        Recibe : None
        Devuelve: None
        """
        if(self.image_1.get_width() > 0):
            self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
            self.image_2.fill((39, 117, 211))
        self.caida_poder()
        self.draw(self.screen) 

        
       
    def caida_poder(self)-> None:
        """
        Realiza la caída del poder, disminuyendo el ancho de la barra 
        y actualizando la imagen correspondiente. Kame ha
        Recibe : None
        Devuelve: None
        """
        if(self.image_1.get_width() > self.caida_kame):
            self.ancho -= self.caida_kame
            self.image_1 = pygame.Surface(((self.ancho / 2) - self.caida_kame, self.alto))
            self.image_1.fill((182, 209, 242))
        
            
    def contra_poder(self)-> None:
        """
        Aumenta el poder contrarrestando el poder del enemigo.
        Recibe: None
        Devuelve:None
        """
        self.ancho += self.aumento_kame
        

    def verificar_frames(self):
        """
        Verifica los cuadros de animación y ajusta el índice del cuadro 
        actual.
        Recibe:None
        Devuelve: None
        """
        
        if(self.frame < len(self.choque_list) -1):
            self.frame += 1
        else:
            self.frame = 0
            

    def draw_choque(self):
        """
        Dibuja la imagen de choque en la pantalla.
        Configura la posición de la imagen de acuerdo con el ancho de 
        la barra y el rectángulo correspondiente.
        Recibe: None
        Devuelve: None
        """
        self.rect_choque.x = (self.ancho / 2) - 130 #pos choque
        self.rect_choque.y = self.rect.y - 45
        if(self.frame < len(self.choque_list) -1):
            image = self.choque_list[self.frame]
            self.screen.blit(image, self.rect_choque)