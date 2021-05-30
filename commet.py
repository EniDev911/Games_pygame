import pygame
import random

# Esta clase representa a nuestro cometas del juego
class Commet(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        # Definir la imagen asociada al cometa
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = random.randint(0, 800)

    def fall(self):
        self.rect.y += self.velocity
