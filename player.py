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

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # Si al jugador no le quedan puntos de vida
            self.game.game_over()

    def update_health_bar(self, surface):
        # definir un color para nuestro indicador de vida (verde claro)
        bar_color = (111,210,46)
        # definir un color para nuestro fondo del indicador de vida (gris oscuro)
        back_bar_color = (60,63,60)
        # definir la posición de nuestro medidor de vida, así como su ancho y grosor
        bar_position = [self.rect.x + 50, self.rect.y + 20, self.health, 7]
        # definir la posición de nuestra fondo de medidor de vida, así como su ancho y grosor
        back_bar_position = [self.rect.x + 50, self.rect.y + 20, self.max_health, 7]
        # dibuja nuestra barra de vida
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


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
