import pygame

# definir la clase que manejara el proyectil de nuestro jugador
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # Girar el proyectil
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # verificamos si el proyectil entra en colisión con el enemigo
        if self.player.game.check_collision(self, self.player.game.all_monsters):
            # Eliminar el proyectil
            self.remove()


        # comprobar si nuestro proyectil ya no está presente en la pantalla
        if self.rect.x > 1080:
            # eliminar proyectiles fuera de la pantala
            self.remove()
            print("proyectil eliminado")