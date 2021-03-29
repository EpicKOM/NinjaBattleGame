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
        self.game_results = False
        self.game_replay = False
        self.sound_manager = SoundManager()
        self.spawn_right_zombie()
        self.spawn_right_zombie()
        self.spawn_right_zombie()
        self.spawn_right_zombie()
        self.spawn_right_zombie()
        self.spawn_right_zombie()



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
        go_font = pygame.font.SysFont("arial", 95, True)
        rounds_font = pygame.font.SysFont("arial", 25, True)
        results_font = pygame.font.SysFont("arial", 30, True)

        go_text = go_font.render("Game Over", True, (255, 255, 255))
        round_text = rounds_font.render("You Survived X Rounds", True, (255, 255, 255))
        points_text = results_font.render("Points", True, (255, 234, 0))
        kills_text = results_font.render("Kills", True, (57, 192, 237))
        game_time_text = results_font.render("Game Time", True, (0, 230, 118))
        retry_text = results_font.render("Press space to restart a game.", True, (255, 255, 255))

        surface.blit(go_text, ((surface.get_width() - go_text.get_width()) / 2, 60))
        surface.blit(round_text, ((surface.get_width() - round_text.get_width()) / 2, 180))
        surface.blit(points_text, (150, 300))
        surface.blit(kills_text, (((769 - (150 + points_text.get_width()))-kills_text.get_width())/2 + 150 + points_text.get_width(), 300))
        surface.blit(game_time_text, (surface.get_width() - 150 - game_time_text.get_width(), 300))




        surface.blit(retry_text, ((surface.get_width() - retry_text.get_width()) / 2, 680))

        self.game_replay = True

