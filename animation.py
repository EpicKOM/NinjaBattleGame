import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, action):
        super().__init__()
        self.image_name = f'assets/{sprite_name}/idle/{action}.png'
        self.image = pygame.image.load(self.image_name)
        self.current_image = 0
        self.images = ''
        self.animation = False
        self.throw_animation = False

    def stop_animation(self):
        self.current_image = 0

    def start_animation(self):
        self.animation = True

    def animate(self, sprite_name, action):
        self.images = animations.get(f'{sprite_name}_{action}')[0]
        self.image_name = animations.get(f'{sprite_name}_{action}')[1]
        if self.animation:
            self.image = self.images[round(self.current_image)]
            self.current_image += 0.2
            if round(self.current_image) >= len(self.images):
                self.current_image = 0
                self.animation = False
                self.throw_animation = False


# definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name, action):
    images = []
    path_name = []

    path = f"assets/{sprite_name}/{action}"
    for num in range(0, 10):
        image_path = f'{path}/{action}{num}.png'
        path_name.append(image_path)
        image = pygame.image.load(image_path)
        images.append(pygame.transform.scale(image, (100, 120)))
    total = [images, path_name]
    return total


animations = {'ninja_throw_right': load_animation_images('ninja', 'throw_right'),
              'ninja_throw_left': load_animation_images('ninja', 'throw_left'),
              'ninja_run_right': load_animation_images('ninja', 'run_right'),
              'ninja_run_left': load_animation_images('ninja', 'run_left'),
              'zombie_male_walk_right': load_animation_images('zombie', 'male_walk_right'),
              'zombie_male_walk_left': load_animation_images('zombie', 'male_walk_left'),
              }
