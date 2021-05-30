import pygame
from game import Game
import math

pygame.init()

# Generar nuestra ventana de juego
pygame.display.set_caption("Juego de caida de cometas")
screen = pygame.display.set_mode((1080, 680))


# cargamos la imagen fondo para el juego
background = pygame.image.load('assets/bg.jpg')

# cargamos la imagen del banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (550,530))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# cargamos el boton para iniciar la partida
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3)
play_button_rect.y = math.ceil(screen.get_height() / 1.8)

# Cargar nuestro juego
game = Game()

running = True


while running:
    # Aplicar el fondo de nuestro juego
    screen.blit(background, (0, -240))

    # Verificar si nuestro jugador a comenzado o no
    if game.is_playing:
        game.update(screen)

    # Verificar si nuestro juego no ha comenzado
    else:
        # Agregar la pantalla de bienvenida
        screen.blit(play_button, play_button_rect)
        screen.blit(banner,banner_rect)
    # Pantalla de actualización
    pygame.display.flip()
    # Si el jugador cierra esta ventana
    for event in pygame.event.get():
        # que el evento cierra una ventana
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fin del juego")

        # detectar si un jugador deja caer una tecla en el teclado
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # detectar si se presiona la tecla de espacio para lanzar nuestro proyectil
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        # detectar si un jugador suelta la tecla en el teclado
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verificar si el boton esta colisionando con el boton
            if play_button_rect.collidepoint(event.pos):
                # poner el juego en modo lanzado
                game.start()