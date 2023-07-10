import pygame
from utilidades import get_surface_form_sprite_sheet
class Kame:
    def __init__(self, screen,ancho_bar, alto_bar ,poder_enemigo, poder_personaje, pos_x, pos_y):
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
        
        self.caida_kame = 5 # representa el poder de jaki su kame que viene hacia goku
        self.aumento_kame = 40 #representa el contraresto del kame . goku contraresta el kame de jaki
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

    def draw(self, screen : pygame.Surface):
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

    def update(self):
        # self.ancho_bar_2 = self.poder_personaje * 100 / self.poder_enemigo
        if(self.image_1.get_width() > 0):
            self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
            self.image_2.fill((39, 117, 211))
        self.caida_poder()
        self.draw(self.screen) 
       
    def caida_poder(self):
        if(self.image_1.get_width() > 0):
            self.ancho -= self.caida_kame
            self.image_1 = pygame.Surface(((self.ancho / 2) - self.caida_kame, self.alto))
            self.image_1.fill((182, 209, 242))
    
    def contra_poder(self):
        self.ancho += self.aumento_kame

    def verificar_frames(self):
        '''
        El personaje se moverá y se animará correctamente con respecto 
        al tiempo transcurrido, lo que resultará en un movimiento más suave 
        y consistente sin depender de la tasa de cuadros (FPS) del juego
        
        '''
        if(self.frame < len(self.choque_list) -1):
            self.frame += 1
        else:
            self.frame = 0

    def draw_choque(self):
        self.rect_choque.x = (self.ancho / 2) - 130 #pos choque
        self.rect_choque.y = self.rect.y - 45
        if(self.frame < len(self.choque_list) -1):
            image = self.choque_list[self.frame]
            self.screen.blit(image, self.rect_choque)