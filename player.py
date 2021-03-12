import pygame
from weapons import Kunai
import animation


class Ninja(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('ninja', 'idle_right')
        self.game = game
        self.image = pygame.transform.scale(self.image, (100, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 505
        self.rect.y = 550
        self.velocity = 5
        self.jump_velocity = 20
        self.jump_deceleration = 1
        self.isJump = False
        self.jump_animation = False
        self.all_kunai_right = pygame.sprite.Group()
        self.all_kunai_left = pygame.sprite.Group()
        self.jump_stop = -20
        self.max_health = 100
        self.health = 100
        self.attack = 20
        self.health_bar_position = 10

    def idle_right(self):
        self.health_bar_position = 10
        self.image_name = 'assets/ninja/idle/idle_right.png'
        self.image = pygame.image.load(self.image_name)
        self.image = pygame.transform.scale(self.image, (100, 120))

    def idle_left(self):
        self.health_bar_position = -15
        self.image_name = 'assets/ninja/idle/idle_left.png'
        self.image = pygame.image.load(self.image_name)
        self.image = pygame.transform.scale(self.image, (100, 120))

    def update_health_bar(self, surface):
        if self.health >= self.max_health*0.5:
            bar_color = (0, 183, 74)
        elif self.max_health * 0.2 < self.health < self.max_health*0.5:
            bar_color = (255, 169, 0)
        else:
            bar_color = (249, 49, 84)

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (46, 46, 46), [self.rect.x + self.health_bar_position, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, bar_color, [self.rect.x + self.health_bar_position, self.rect.y - 15, self.health, 7])

    def launch_kunai_right(self):
        self.health_bar_position = 10
        kunai_right = Kunai(self)
        kunai_right.image = pygame.image.load('assets/projectiles/kunai_right.png')
        kunai_right.image = pygame.transform.scale(kunai_right.image, (50, 10))
        kunai_right.rect.x = self.rect.x + 55
        kunai_right.rect.y = self.rect.y + 60
        self.all_kunai_right.add(kunai_right)
        self.start_animation()

    def launch_kunai_left(self):
        self.health_bar_position = -15
        kunai_left = Kunai(self)
        kunai_left.image = pygame.image.load('assets/projectiles/kunai_left.png')
        kunai_left.image = pygame.transform.scale(kunai_left.image, (50, 10))
        kunai_left.rect.x = self.rect.x - 45
        kunai_left.rect.y = self.rect.y + 60
        self.all_kunai_left.add(kunai_left)
        self.start_animation()

    def run_right(self):
        self.throw_animation = False
        self.health_bar_position = 13
        if not self.game.check_collision(self, self.game.all_zombies_right) and not self.game.check_collision(self, self.game.all_zombies_left):
            self.rect.x += self.velocity
            self.start_animation()
        else:
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.x > zombie.x():
                    self.rect.x += self.velocity
                    self.start_animation()
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.x > zombie.x():
                    self.rect.x += self.velocity
                    self.start_animation()

    def run_left(self):
        self.throw_animation = False
        self.health_bar_position = -20
        if not self.game.check_collision(self, self.game.all_zombies_right) and not self.game.check_collision(self, self.game.all_zombies_left):
            self.rect.x -= self.velocity
            self.start_animation()
        else:
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.x < zombie.x():
                    self.rect.x -= self.velocity
                    self.start_animation()
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.x < zombie.x():
                    self.rect.x -= self.velocity
                    self.start_animation()

    def jump(self):
        self.health_bar_position = 0
        self.throw_animation = False
        if 'right' in self.image_name or 'right' in self.image_name[0]:
            self.image_name = 'assets/ninja/jump/jump_right.png'
            self.image = pygame.image.load(self.image_name)
            self.image = pygame.transform.scale(self.image, (90, 120))
        else:
            self.image_name = 'assets/ninja/jump/jump_left.png'
            self.image = pygame.image.load(self.image_name)
            self.image = pygame.transform.scale(self.image, (90, 120))

        self.rect.y -= self.jump_velocity
        self.jump_velocity -= self.jump_deceleration
        if self.jump_animation:
            self.start_animation()
            self.jump_animation = False
        if self.jump_velocity < self.jump_stop:
            self.isJump = False
            self.jump_velocity = 20
            self.jump_stop = -20
            self.rect.y = 550
            self.stop_animation()
            if 'right' in self.image_name:
                self.idle_right()
            else:
                self.idle_left()

        if self.game.check_collision(self, self.game.all_zombies_right):
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.y == 476:
                    zombie.damage(self.attack)
                    self.isJump = True
                    self.jump_velocity = 20
                    self.jump_stop = -24

        if self.game.check_collision(self, self.game.all_zombies_left):
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.y == 476:
                    zombie.damage(self.attack)
                    self.isJump = True
                    self.jump_velocity = 20
                    self.jump_stop = -24
