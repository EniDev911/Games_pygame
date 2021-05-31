import pygame
import random
import animation

# Crear una clase que maneje la noción de monstruo en nuestro juego
class Monster(animation.AnimateSprite):


    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 500
        self.velocity = random.randint(1, 3)


    def damage(self, amount):
        # Infligir daño
        self.health -= amount
        # Comprobar si su nuevo número de vida es menor o igual a 0
        if self.health <= 0:
            # Reaparecer como un nuevo monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health
            self.velocity = random.randint(1,3)

            # Si la barra de evento esta cargada al máximo
            if self.game.comet_event.is_full_loaded():
                # Retirar monsters
                self.game.all_monsters.remove(self)

                # Aparecer la lluvia de cometas
                self.game.comet_event.attempt_fall()


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

        # Si el monstruo choca con el jugador
        else:
        # Infligir daño (al jugador)
            self.game.player.damage(self.attack)

