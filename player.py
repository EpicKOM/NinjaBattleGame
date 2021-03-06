import pygame
from weapons import Kunai, Fireball, Kamehameha
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
        self.jump_parameters = []
        self.isJump = False
        self.jump_animation = False
        self.all_kunai_right = pygame.sprite.Group()
        self.all_kunai_left = pygame.sprite.Group()
        self.all_fireball_right = pygame.sprite.Group()
        self.all_fireball_left = pygame.sprite.Group()
        self.all_kamehameha_right = pygame.sprite.Group()
        self.all_kamehameha_left = pygame.sprite.Group()
        self.jump_stop = -20
        self.max_health = 100
        self.ko_alert = False
        self.health = 100
        self.attack = 15
        self.health_bar_position = 10
        self.magic_power = 0
        self.max_magic_power = 200

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.vanish_all_monsters()
            self.game.game_time = pygame.time.get_ticks()

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

    def update_magic_bar(self, surface, height):
        if self.magic_power >= self.max_magic_power:
            self.magic_power = self.max_magic_power
            pygame.draw.rect(surface, (213, 49, 84), [270, 20 + (height / 2) - 14, 40, 28], 3, 3, 3, 3)
            font_ko = pygame.font.SysFont('arial', 16, True)
            ko_text = font_ko.render("KO", True, (255, 255, 255))
            surface.blit(ko_text, (
            270 + (40 - ko_text.get_width()) / 2, 20 + (height / 2) - (14 - (28 - ko_text.get_height()) / 2)))

            if self.ko_alert:
                self.game.sound_manager.play('ko', 0.4, 0)
                self.ko_alert = False

        elif self.magic_power < self.max_magic_power:
            self.ko_alert = True

        elif self.max_magic_power <= 0:
            self.magic_power = 0

        pygame.draw.rect(surface, (46, 46, 46), [60, 20 + (height / 2) - 6, 200, 10])
        pygame.draw.rect(surface, (13, 71, 161), [60, 20 + (height / 2) - 6, self.magic_power, 10])

    def update_health_bar(self, surface):

        if self.health >= self.max_health:
            bar_color = (0, 183, 74)
            self.health = self.max_health

        elif self.health >= self.max_health * 0.5:
            bar_color = (0, 183, 74)

        elif self.max_health * 0.2 < self.health < self.max_health * 0.5:
            bar_color = (255, 169, 0)
        else:
            bar_color = (249, 49, 84)

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (46, 46, 46),
                         [self.rect.x + self.health_bar_position, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, bar_color, [self.rect.x + self.health_bar_position, self.rect.y - 15, self.health, 7])

    def launch_kamehameha_right(self):
        kamehameha_right = Kamehameha(self)
        kamehameha_right.throw_kamehameha = True
        self.all_kamehameha_right.add(kamehameha_right)
        self.animation_speed = 0.2
        self.start_animation()

    def launch_kamehameha_left(self):
        kamehameha_left = Kamehameha(self)
        kamehameha_left.throw_kamehameha = True
        kamehameha_left.image = pygame.image.load('assets/kamehameha/idle/idle_left.png')
        kamehameha_left.rect.y = self.rect.y + 58
        self.all_kamehameha_left.add(kamehameha_left)
        self.animation_speed = 0.2
        self.start_animation()

    def launch_kunai_right(self):
        self.health_bar_position = 10
        kunai_right = Kunai(self)
        kunai_right.image = pygame.image.load('assets/projectiles/kunai_right.png')
        kunai_right.image = pygame.transform.scale(kunai_right.image, (50, 10))
        kunai_right.rect.x = self.rect.x + 55
        kunai_right.rect.y = self.rect.y + 60
        if not self.game.key_pressed.get(pygame.K_RIGHT):
            kunai_right.attack = 20
        self.all_kunai_right.add(kunai_right)
        self.animation_speed = 0.2
        self.start_animation()

    def launch_kunai_left(self):
        self.health_bar_position = -15
        kunai_left = Kunai(self)
        kunai_left.image = pygame.image.load('assets/projectiles/kunai_left.png')
        kunai_left.image = pygame.transform.scale(kunai_left.image, (50, 10))
        kunai_left.rect.x = self.rect.x - 3
        kunai_left.rect.y = self.rect.y + 60
        if not self.game.key_pressed.get(pygame.K_LEFT):
            kunai_left.attack = 20
        self.all_kunai_left.add(kunai_left)
        self.animation_speed = 0.2
        self.start_animation()

    def launch_fireball_right(self):
        self.health_bar_position = 10
        fireball_right = Fireball(self)
        if not self.game.key_pressed.get(pygame.K_RIGHT):
            fireball_right.attack = 50
        self.all_fireball_right.add(fireball_right)
        self.animation_speed = 0.2
        self.start_animation()
        self.magic_power -= fireball_right.magic

    def launch_fireball_left(self):
        self.health_bar_position = -15
        fireball_left = Fireball(self)
        fireball_left.rect.x = self.rect.x - 3
        if not self.game.key_pressed.get(pygame.K_RIGHT):
            fireball_left.attack = 50
        self.all_fireball_left.add(fireball_left)
        self.animation_speed = 0.2
        self.start_animation()
        self.magic_power -= fireball_left.magic

    def run_right(self):
        self.throw_animation = False
        self.health_bar_position = 13
        if not self.game.check_collision(self, self.game.all_zombies_right) and not self.game.check_collision(self,
                                                                                                              self.game.all_zombies_left):
            self.rect.x += self.velocity
            self.animation_speed = 0.3
            self.start_animation()
        else:
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.x > zombie.x():
                    self.rect.x += self.velocity
                    self.animation_speed = 0.3
                    self.start_animation()
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.x > zombie.x():
                    self.rect.x += self.velocity
                    self.animation_speed = 0.3
                    self.start_animation()

    def run_left(self):
        self.throw_animation = False
        self.health_bar_position = -20
        if not self.game.check_collision(self, self.game.all_zombies_right) and not self.game.check_collision(self,
                                                                                                              self.game.all_zombies_left):
            self.rect.x -= self.velocity
            self.animation_speed = 0.3
            self.start_animation()
        else:
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.x < zombie.x():
                    self.rect.x -= self.velocity
                    self.animation_speed = 0.3
                    self.start_animation()
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.x < zombie.x():
                    self.rect.x -= self.velocity
                    self.animation_speed = 0.3
                    self.start_animation()

    def start_move(self):
        self.velocity = 5
        self.jump_velocity = 20
        self.jump_deceleration = 1
        self.magic_power = 0
        if self.isJump:
            self.jump_velocity = self.jump_parameters[0]
            self.jump_deceleration = 1
        if self.game.key_pressed.get(pygame.K_LEFT):
            self.game.sound_manager.play('running_left', 0.04, -1)
        elif self.game.key_pressed.get(pygame.K_RIGHT):
            self.game.sound_manager.play('running_right', 0.04, -1)

    def kamehameha_enabled_right(self):
        self.velocity = 0
        self.jump_velocity = 0
        self.image = pygame.image.load('assets/ninja/throw_right/throw_right0.png')
        self.image = pygame.transform.scale(self.image, (100, 120))

    def kamehameha_enabled_left(self):
        self.velocity = 0
        self.jump_velocity = 0
        self.image = pygame.image.load('assets/ninja/throw_left/throw_left0.png')
        self.image = pygame.transform.scale(self.image, (100, 120))

    def jump(self):
        self.game.sound_manager.stop('running_left')
        self.game.sound_manager.stop('running_right')
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
        if self.throw_kamehameha:
            self.jump_parameters.append(self.jump_velocity)
        if self.jump_animation:
            self.start_animation()
            self.jump_animation = False
        if self.jump_velocity < self.jump_stop:
            if self.game.key_pressed.get(pygame.K_LEFT):
                self.game.sound_manager.play('running_left', 0.04, -1)
            elif self.game.key_pressed.get(pygame.K_RIGHT):
                self.game.sound_manager.play('running_right', 0.04, -1)
            self.isJump = False
            self.jump_velocity = 20
            self.jump_stop = -20
            self.rect.y = 550
            self.jump_parameters = []
            self.stop_animation()
            if 'right' in self.image_name:
                self.idle_right()
            else:
                self.idle_left()

        if self.game.check_collision(self, self.game.all_zombies_right):
            for zombie in self.game.check_collision(self, self.game.all_zombies_right):
                if self.rect.y >= 476 and self.jump_velocity <= 0:
                    self.game.sound_manager.play('punch', 0.08, 0)
                    zombie.damage(self.attack)
                    self.isJump = True
                    self.jump_velocity = 20
                    self.jump_stop = -24

        if self.game.check_collision(self, self.game.all_zombies_left):
            for zombie in self.game.check_collision(self, self.game.all_zombies_left):
                if self.rect.y >= 476 and self.jump_velocity <= 0:
                    self.game.sound_manager.play('punch', 0.08, 0)
                    zombie.damage(self.attack)
                    self.isJump = True
                    self.jump_velocity = 20
                    self.jump_stop = -24

    def gain_life(self, amount):
        self.health += amount
