import pygame
import random


# Classe qui va gérer l'énemie de type Zombie male
class Zombie(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 0.3
        self.magic = 25
        self.random_zombie = random.choice(['zombie_male', 'zombie_female'])
        self.image = pygame.image.load('assets/{}.png'.format(self.random_zombie))
        self.image = pygame.transform.scale(self.image, (99, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 552
        self.velocity = random.randint(1, 7)

    def damage(self, amount, ultime):
        self.health -= amount
        if ultime:
            self.game.kill += 1
            self.game.player.magic_power(self.magic)
            self.rect.x = 4000
            self.velocity = random.randint(1, 5)
            self.health = self.max_health

        else:
            if self.health <= 0:
                self.game.kill += 1
                self.game.player.magic_power(self.magic)
                self.rect.x = 1000 + random.randint(0, 500)
                self.velocity = random.randint(1, 5)
                self.health = self.max_health
                self.random_zombie = random.choice(['zombie_male', 'zombie_female'])
                self.image = pygame.image.load('assets/{}.png'.format(self.random_zombie))
                self.image = pygame.transform.scale(self.image, (99, 120))

    def update_health_bar(self, surface):
        if self.health >= self.max_health*0.5:
            bar_color = (0, 183, 74)
        elif self.max_health * 0.2 < self.health < self.max_health * 0.5:
            bar_color = (255, 169, 0)
        else:
            bar_color = (249, 49, 84)

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (46, 46, 46), [self.rect.x, self.rect.y, self.max_health * 2, 5])
        pygame.draw.rect(surface, bar_color, [self.rect.x, self.rect.y, self.health*2, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self. rect.x -= self.velocity
            if self.rect.x < 0:
                for i in self.game.all_zombie:
                    self.game.player.magic_power(self.magic)
                    self.rect.x = 1000 + random.randint(0, 500)
                    self.velocity = random.randint(1, 5)
                    self.health = self.max_health
                    self.random_zombie = random.choice(['zombie_male', 'zombie_female'])
                    self.image = pygame.image.load('assets/{}.png'.format(self.random_zombie))
                    self.image = pygame.transform.scale(self.image, (99, 120))
        else:
            self.game.player.damage(self.attack)

