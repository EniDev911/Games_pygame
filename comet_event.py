import pygame
from commet import Commet

class CometFallEvent:
    # AL cargar crear un contador
    def __init__(self):
        self.percent = 0
        self.percent_speed = 50

        # Definir el grupo de cometas
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # Apareciendo las bolas de fuego
        self.all_comets.add(Commet())

    def attempt_fall(self):
        if self.is_full_loaded():
            print('Comienzan los cometas')
            self.meteor_fall()
            self.reset_percent()


    def update_bar(self, surface):
        # agregar porcentaje a la barra
        self.add_percent()

        # Aparecer la lluvia de cometas
        self.attempt_fall()

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
