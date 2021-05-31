import pygame


# Definir la clase responsable de la animación
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0
        self.images = animations.get(sprite_name)
    # Definir el método para animar sprite
    def animate(self):

        self.current_image += 1

        # Verificar si hemos legado a la última animación
        if self.current_image >= len(self.images):
            # volvemos a poner la animación del comienzo
            self.current_image = 0

        # Modificar la imagen actual
        self.image = self.images[self.current_image]




# Definir la función para cargar las imagenes de un sprite
def load_animation_images(sprite_name):
    # Cargar las imagenes que corresponden al sprite
    images = []
    # almacenar la ruta de las imagenes
    path = f"assets/{sprite_name}/{sprite_name}"

    # Bucles para cargar las imagenes
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    # devolver las imagenes cargadas
    return images

# Definir un diccionario para contener las imágenes cargadas para cada sprite
# Ej: mummy -> [...mummy1.png, ...mummy2.png,...]
animations = {
    'mummy': load_animation_images('mummy')
}