import pygame
from projectile import Projectile
# crear una primera clase representará a nuestro jugador
class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/player.png')
        # Capa colisión
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 460


    def launch_projectile(self):
        # Crear una nueva instancia de la clase Projectile
        # projectile = Projectile()
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si el jugador no choca con un monstruo
        if  not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity
