import pygame

# Crear una clase que maneje la noción de monstruo en nuestro juego
class Monster(pygame.sprite.Sprite):


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 500
        self.velocity = 2


    def damage(self, amount):
        pass

    def update_health_bar(self, surface):
        # definir un color para nuestro indicador de vida (verde claro)
        bar_color = (111,210,46)
        # definir un color para nuestro fondo del indicador de vida (gris oscuro)
        back_bar_color = (60,63,60)
        # definir la posición de nuestro medidor de vida, así como su ancho y grosor
        bar_position = [self.rect.x + 10, self.rect.y -20, self.health, 5]
        # definir la posición de nuestra fondo de medidor de vida, así como su ancho y grosor
        back_bar_position = [self.rect.x + 10, self.rect.y -20, self.max_health, 5]
        # dibuja nuestra barra de vida
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self):

        # EL desplazamiento solo se realiza si no hay colisión con un grupo de jugadores
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity


