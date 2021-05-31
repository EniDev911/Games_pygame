import pygame
from player import Player
from comet_event import CometFallEvent
from monster import Monster
# crear una clase que representará nuestro juego
class Game:
    def __init__(self):
        # Definir si el jugador a comenzado o no
        self.is_playing = False
        # Generar nuestro juego y crear una instancia de jugador
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generar eventos
        self.comet_event = CometFallEvent(self)
        # Grupo de monstruos
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # reiniciar el juego, eliminar monstruos, reiniciar el jugador a 100
        # puntos de salud, juego en espera
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False


    def update(self, screen):

        # Aplicar mi imagen de jugador
        screen.blit(self.player.image, self.player.rect)

        # actualizar barra de vida del jugador
        self.player.update_health_bar(screen)

        # actualizar la barra de evento del juego
        self.comet_event.update_bar(screen)

        # recuperar proyectiles del jugador
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperar los monstruos de nuestro jugador
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # recuperar los cometas de nuestro jugador
        for comet in self.comet_event.all_comets:
            comet.fall()


        # aplicar todas las imágenes de mi grupo de proyectiles
        self.player.all_projectiles.draw(screen)

        # aplicar todas las imágenes de mi grupo de monstruos
        self.all_monsters.draw(screen)

        # aplicar todas las imagenes de grupo de cometas
        self.comet_event.all_comets.draw(screen)

        # Comprobar si el jugador quiere ir hacia la derecha y dentro del límite
        if self.pressed.get(pygame.K_RIGHT) and (self.player.rect.x +
            self.player.rect.width < screen.get_width()): self.player.move_right()
        # Comprobar si el jugador quiere ir hacia la izquierda y dentro del límite
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)