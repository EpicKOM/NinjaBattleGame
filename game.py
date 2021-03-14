import pygame
import random
from player import Ninja
from enemies import Zombie


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.key_pressed = {}
        self.player = Ninja(self)
        self.player_group = pygame.sprite.Group(self.player)
        self.all_zombies_right = pygame.sprite.Group()
        self.all_zombies_left = pygame.sprite.Group()
        self.kill = 0
        self.total_points = 0
        self.spawn_left_zombie()
        # self.spawn_right_zombie()

    def spawn_right_zombie(self):
        zombie_right = Zombie(self)
        zombie_right.random_zombie = random.choice(['zombie_male_right', 'zombie_female_right'])
        zombie_right.image = pygame.image.load('assets/{}.png'.format(zombie_right.random_zombie))
        zombie_right.image = pygame.transform.scale(zombie_right.image, (99, 120))
        zombie_right.rect.x = 1080 + random.randint(0, 300)
        self.all_zombies_right.add(zombie_right)

    def spawn_left_zombie(self):
        zombie_left = Zombie(self)
        zombie_left.random_zombie = random.choice(['zombie_male_left', 'zombie_female_left'])
        zombie_left.image = pygame.image.load('assets/{}.png'.format(zombie_left.random_zombie))
        zombie_left.image = pygame.transform.scale(zombie_left.image, (99, 120))
        zombie_left.rect.x = 0 - zombie_left.image.get_width() - random.randint(0, 300)
        self.all_zombies_left.add(zombie_left)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

