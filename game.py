import pygame
from player import Player
from monster import Monster
# crear una clase que representará nuestro juego
class Game:
    def __init__(self):
        # Generar nuestro juego y crear una instancia de jugador
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Grupo de monstruos
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)