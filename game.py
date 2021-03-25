import pygame
import random
from player import Ninja
from enemies import Zombie
from sounds import SoundManager


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.key_pressed = {}
        self.player = Ninja(self)
        self.player_group = pygame.sprite.Group(self.player)
        self.all_zombies_right = pygame.sprite.Group()
        self.all_zombies_left = pygame.sprite.Group()
        self.kill = 0
        self.dismiss_monsters = False
        self.total_points = 0
        self.game_finish = False
        self.finish_scene = True
        self.kamehameha_mode = False
        self.sound_manager = SoundManager()

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

    def vanish_all_monsters(self):
        for zombie in self.all_zombies_right:
            zombie.current_image = 0
        for zombie in self.all_zombies_left:
            zombie.current_image = 0
        self.sound_manager.play('poof', 0.06, 0)
        self.dismiss_monsters = True

    def game_over(self, surface):
        GO_font = pygame.font.SysFont("arial", 95, True)
        retry_font = pygame.font.SysFont("arial", 25, True)
        kill_icon = pygame.image.load('assets/design/cross.png')
        kill_icon = pygame.transform.scale(kill_icon, (32, 43))

        GO_text = GO_font.render("Game Over", True, (255, 255, 255))
        retry_text = retry_font.render("Appuyer sur espace pour recommencer une partie.", True, (255, 255, 255))
        surface.blit(GO_text, ((surface.get_width() - GO_text.get_width()) / 2, 60))
        surface.blit(kill_icon, (((surface.get_width() - GO_text.get_width())/2) + GO_text.get_width() / 2, 250))
        surface.blit(retry_text, ((surface.get_width() - retry_text.get_width()) / 2, 680))

