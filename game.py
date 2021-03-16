import pygame
import random
import time
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
        self.spawn_right_zombie()
        self.spawn_left_zombie()
        self.spawn_right_zombie()
        self.spawn_left_zombie()
        self.spawn_right_zombie()
        self.spawn_left_zombie()
        self.spawn_right_zombie()
        self.game_finish = False

    def spawn_right_zombie(self):
        zombie_right = Zombie(self)
        zombie_right.rect.x = 1080 + random.randint(0, 300)
        self.all_zombies_right.add(zombie_right)

    def spawn_left_zombie(self):
        zombie_left = Zombie(self)
        zombie_left.rect.x = 0 - zombie_left.image.get_width() - random.randint(0, 300)
        self.all_zombies_left.add(zombie_left)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def game_over(self):
        for zombie in self.all_zombies_right:
            zombie.remove()

        for zombie in self.all_zombies_left:
            zombie.remove()
        self.player.animation_speed = 0.1
        self.player.start_animation()
        self.player.gover_animation = True
        self.game_finish = True