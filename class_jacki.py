import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('asset\jack_chun.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.vida = 5000
        self.esta_muerto = False

    def update(self, screen):
        self.draw(screen)
    def draw(self, screen):
        screen.blit(self.image, self.rect)