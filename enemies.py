import pygame
import random
import animation


class Zombie(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('zombie', 'male_idle_right')
        self.game = game
        self.random_zombie = random.choice(['male_', 'female_'])
        self.image = pygame.transform.scale(self.image, (99, 120))
        self.rect = self.image.get_rect()
        self.rect.y = 552
        self.velocity = random.randint(1, 3)
        self.velocity_memory = []
        self.max_health = 50
        self.health = 50
        self.angle = 0
        self.points = 10
        self.magic = 20
        self.attack = 0.4

    def remove(self):
        self.game.all_zombies_right.remove(self)
        self.game.all_zombies_left.remove(self)

    def kamehameha_damage(self, amount=1000):
        self.health -= amount

        # Si le zombie est K.O
        if self.health <= 0:
            self.game.kill += 1
            self.game.monster_counter += 1
            self.game.total_points += self.points
            self.health = self.max_health
            if self in self.game.all_zombies_right:
                self.random_zombie = random.choice(['male_', 'female_'])
                self.velocity = random.randint(1, 3)
                self.rect.x = 2450

            elif self in self.game.all_zombies_left:
                self.random_zombie = random.choice(['male_', 'female_'])
                self.velocity = random.randint(1, 3)
                self.rect.x = -1370

    def damage(self, amount):
        self.health -= amount

        # Si le zombie est K.O
        if self.health <= 0:
            self.game.kill += 1
            self.game.monster_counter += 1
            self.game.total_points += self.points
            self.game.player.magic_power += self.magic
            self.health = self.max_health
            if self in self.game.all_zombies_right:
                self.random_zombie = random.choice(['male_', 'female_'])
                self.velocity = random.randint(1, 3)
                self.rect.x = 1080 + random.randint(0, 300)
                self.velocity_memory = []

            elif self in self.game.all_zombies_left:
                self.random_zombie = random.choice(['male_', 'female_'])
                self.velocity = random.randint(1, 3)
                self.rect.x = 0 - self.image.get_width() - random.randint(0, 300)
                self.velocity_memory = []

    def update_health_bar(self, surface):
        if self.health >= self.max_health * 0.5:
            bar_color = (0, 183, 74)
        elif self.max_health * 0.2 < self.health < self.max_health * 0.5:
            bar_color = (255, 169, 0)
        else:
            bar_color = (249, 49, 84)

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (46, 46, 46), [self.rect.x, self.rect.y, self.max_health * 2, 5])
        pygame.draw.rect(surface, bar_color, [self.rect.x, self.rect.y, self.health*2, 5])

    def move_right(self):
        if not self.game.check_collision(self, self.game.player_group):
            self.rect.x += self.velocity
            self.animation_speed = 0.2
            self.start_animation()
            # Vérifier si le Zombie est encore sur l'écran
            if self.rect.x > 1080:
                self.health = self.max_health
                self.velocity = random.randint(1, 3)
                self.random_zombie = random.choice(['male_', 'female_'])
                self.rect.x = 0 - self.image.get_width() - random.randint(0, 300)
                self.velocity_memory = []

        else:
            if self.rect.x <= self.game.player.rect.x:
                self.start_animation()
                self.zombie_attack = True
                self.game.player.damage(self.attack)
                self.animation_speed = 0.08
            else:
                self.start_animation()
                self.attack_reverse = True
                self.zombie_attack = True
                self.game.player.damage(self.attack)
                self.animation_speed = 0.08

    def move_left(self):
        if not self.game.check_collision(self, self.game.player_group) or self.game.kamehameha_mode:
            self.rect.x -= self.velocity
            self.animation_speed = 0.2
            self.start_animation()
            # Vérifier si le Zombie est encore sur l'écran
            if self.rect.x < 0 - self.image.get_width():
                self.velocity = random.randint(1, 3)
                self.health = self.max_health
                self.random_zombie = random.choice(['male_', 'female_'])
                self.rect.x = 1080 + random.randint(0, 300)
                self.velocity_memory = []

        else:
            if self.rect.x >= self.game.player.rect.x:
                self.start_animation()
                self.zombie_attack = True
                self.animation_speed = 0.08
                if self.game.player.rect.y > 476:
                    self.game.player.damage(self.attack)
                if self.game.kamehameha_mode:
                    self.game.player.damage(0)

            else:
                self.start_animation()
                self.attack_reverse = True
                self.zombie_attack = True
                self.animation_speed = 0.08
                if self.game.player.rect.y > 476:
                    self.game.player.damage(self.attack)
                if self.game.kamehameha_mode:
                    self.game.player.damage(0)

    def stop_move(self):
        self.velocity_memory.append(self.velocity)
        self.velocity = 0

    def start_move(self):
        self.velocity = self.velocity_memory[0]

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y