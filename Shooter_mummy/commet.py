import pygame
import random

# Esta clase representa a nuestro cometas del juego
class Commet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # Definir la imagen asociada al cometa
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # Verificar si el número de cometa es 0
        if len(self.comet_event.all_comets) == 0:
            print('Evento finalizado')
            # resetear barra a 0
            self.comet_event.reset_percent()
            # aparecer los dos primeros monsters
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()



    def fall(self):
        self.rect.y += self.velocity

        # Comprobar si los cometas tocan el suelo
        if self.rect.y >= 500:
        	# Retirar las bolas de fuego
            self.remove()

            # Si ya no hay más bolas de fuego
            if len(self.comet_event.all_comets) == 0:
                print('Evento finalizado')

                self.comet_event.reset_percent()
                self.comet_event.fall = False


        # Verificar si la bola de fuego golpea al jugador
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
        ):
            print('Golpeado el jugador')
            # Retirar la bola de fuego
            self.remove()
            # 20 points
            self.comet_event.game.player.damage(20)




