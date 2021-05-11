import pygame
from game import Game

pygame.init()

# Generar nuestra ventana de juego
pygame.display.set_caption("Juego de caida de cometas")
screen = pygame.display.set_mode((1080, 680))


# importar fondo para el juego
background = pygame.image.load('assets/bg.jpg')

# Cargar nuestro juego
game = Game()

running = True


while running:
    # Aplicar el fondo de nuestro juego
    screen.blit(background, (0, -240))
    # Aplicar mi imagen de jugador
    screen.blit(game.player.image, game.player.rect)

    # recuperar proyectiles del jugador
    for projectile in game.player.all_projectiles:
        projectile.move()

    # recuperar los monstruos de nuestro jugador
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)


    # aplicar todas las imágenes de mi grupo de proyectiles
    game.player.all_projectiles.draw(screen)

    # aplicar todas las imágenes de mi grupo de monstruos
    game.all_monsters.draw(screen)

    # Comprobar si el jugador quiere ir hacia la derecha y dentro del límite
    if game.pressed.get(pygame.K_RIGHT) and (game.player.rect.x +
        game.player.rect.width < screen.get_width()): game.player.move_right()
    # Comprobar si el jugador quiere ir hacia la izquierda y dentro del límite
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
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

