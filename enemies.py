import pygame
import random
import animation


class Zombie(animation.AnimateSprite):
    def __init__(self, game):
        super().__init__('zombie', 'male_idle_right')
        self.game = game
        self.image = pygame.transform.scale(self.image, (99, 120))
        self.rect = self.image.get_rect()
        self.rect.y = 552
        self.velocity = 1  # random.randint(1, 4)
        self.max_health = 50
        self.health = 50
        self.angle = 0
        self.points = 10

    def damage(self, amount):
        self.health -= amount

        # Si le zombie est K.O
        if self.health <= 0:
            self.game.kill += 1
            self.game.total_points += self.points
            self.health = self.max_health
            if self in self.game.all_zombies_right:
                self.random_zombie = random.choice(['zombie_male_right', 'zombie_female_right'])
                self.image = pygame.image.load('assets/{}.png'.format(self.random_zombie))
                self.image = pygame.transform.scale(self.image, (99, 120))
                self.rect.x = 1080 + random.randint(0, 300)

            elif self in self.game.all_zombies_left:
                self.random_zombie = random.choice(['zombie_male_left', 'zombie_female_left'])
                self.image = pygame.image.load('assets/{}.png'.format(self.random_zombie))
                self.image = pygame.transform.scale(self.image, (99, 120))
                self.rect.x = 0 - self.image.get_width() - random.randint(0, 300)

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
            self.start_animation()

    def move_left(self):
        if not self.game.check_collision(self, self.game.player_group):
            self.rect.x -= self.velocity
            self.start_animation()

    def x(self):
        return self.rect.x

    def y(self):
        return self.rect.y