import pygame

class Kame:
    def __init__(self, screen,ancho_bar, alto_bar ,poder_enemigo, poder_personaje, pos_x, pos_y):
        #goku
        self.image_goku = pygame.image.load("asset\goku_poder_final.png")
        self.image_goku = pygame.transform.scale(self.image_goku, (182, 155))
        self.rect_goku = self.image_goku.get_rect()
        self.rect_goku.x = 0
        self.rect_goku.y = 500
        #jacky chun
        self.image_jack = pygame.image.load("asset\jacky_poder_final.png")
        self.image_jack = pygame.transform.scale(self.image_jack, (182,155))
        self.rect_jack  = self.image_goku.get_rect()
        self.rect_jack .x = 820
        self.rect_jack .y = 500

        self.ancho = ancho_bar
        self.alto = alto_bar
        self.poder_enemigo = poder_enemigo
        self.poder_personaje = poder_personaje
        self.screen = screen
        self.ancho_bar_2 = ancho_bar

        self.image_1 = pygame.Surface((self.ancho / 2, self.alto))
        self.image_1.fill((0, 255, 0))
        self.rect = self.image_1.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        self.caida_kame = 5
        self.aumento_kame = 30
        self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
        self.image_2.fill((0, 0, 255))
        self.rect_2 = self.image_2.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def draw(self, screen : pygame.Surface):
        screen.blit(self.image_goku, self.rect_goku)
        screen.blit(self.image_jack, self.rect_jack)
        screen.blit(self.image_2, self.rect) # Azul Roshi
        screen.blit(self.image_1, self.rect)# celeste Goku 


    def update(self):
        # self.ancho_bar_2 = self.poder_personaje * 100 / self.poder_enemigo
        if(self.image_1.get_width() > 0):
            self.image_2 = pygame.Surface((self.ancho_bar_2, self.alto))
            self.image_2.fill((0, 0, 255)) 
        self.caida_poder()
        self.draw(self.screen) 

        # key = pygame.key.get_pressed()

        # if(key[pygame.K_e]):
        #     self.ancho += self.aumento_kame
        #     print('ANCHO:::>',self.ancho)

        # print("dibujando barra kame")
    def caida_poder(self):
        if(self.image_1.get_width() > 0):
            self.ancho -= self.caida_kame
            self.image_1 = pygame.Surface(((self.ancho / 2) - self.caida_kame, self.alto))
            self.image_1.fill((0, 255, 0))
    
    def contra_poder(self):
        self.ancho += self.aumento_kame

    

