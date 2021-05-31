import pygame
from commet import Commet

class CometFallEvent:
    # AL cargar crear un contador
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        # Definir el grupo de cometas
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # bucle para la aparición de las bolas de fuego
        for i in range(1, 10):
            # Apareciendo las bolas de fuego
            self.all_comets.add(Commet(self))

    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print('Comienzan los cometas')
            self.meteor_fall()
            self.fall_mode = True # Activamos el evento


    def update_bar(self, surface):
        # agregar porcentaje a la barra
        self.add_percent()


        # barra negra (en el fondo)
        pygame.draw.rect(surface, (0,0,0), [
            0, # eje x
            surface.get_height() - 20, # eje y
            surface.get_width(), # longitud de la ventana
            10 # grosor de la barra
            ])

        # barra roja (indicador de eventos)
        pygame.draw.rect(surface, (187,11,11), [
            0, # eje x
            surface.get_height() - 20, # eje y
            (surface.get_width() / 100) * self.percent, # longitud de la ventana
            10 # grosor de la barra
            ])
