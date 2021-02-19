# Coding : UTF-8

# ------Importation des bibliothèques ----------------------------------------------------------------------------------
import pygame
from projectile import Kunai, Fireball, Superkunai


# Classe représentant le personnage principal (Un Ninja)
class Ninja(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = 100
        self.max_magic = 200
        self.magic = 200
        self.attack = 10
        self.velocity = 5
        self.isJump = False
        self.jump_velocity = 20
        self.jump_deceleration = 1
        self.image = pygame.image.load('assets/ninja.png')
        self.image = pygame.transform.scale(self.image, (63, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 505
        self.rect.y = 550
        self.all_kunai = pygame.sprite.Group()
        self.all_fireball = pygame.sprite.Group()
        self.all_superkunai = pygame.sprite.Group()

    def magic_power(self, magic_amount):
        if self.magic < self.max_magic:
            self.magic += magic_amount*0.2
        if self.max_magic > self.max_magic:
            self.max_magic = self.max_magic

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.game.game_over()

    def magic_progress_bar(self, surface):
        pygame.draw.rect(surface, (46, 46, 46), [80, 50, self.max_magic, 10])
        pygame.draw.rect(surface, (18, 102, 241), [80, 50, self.magic, 10])

    def update_health_bar(self, surface):
        if self.health >= self.max_health*0.5:
            bar_color = (0, 183, 74)
        elif self.max_health * 0.2 < self.health < self.max_health*0.5:
            bar_color = (255, 169, 0)
        else:
            bar_color = (249, 49, 84)

        # Dessiner la barre de vie
        pygame.draw.rect(surface, (46, 46, 46), [self.rect.x - 20, self.rect.y - 15, self.max_health, 7])
        pygame.draw.rect(surface, bar_color, [self.rect.x - 20, self.rect.y - 15, self.health, 7])

    def move_right(self):
        # Si le joueur n'est pas en collision avec un ennemi déplacement à droite autorisé'
        if not self.game.check_collision(self, self.game.all_zombie):
            self.rect.x += self.velocity

    def move_left(self):
        # Si le joueur n'est pas en collision avec un ennemi déplacement à gauche autorisé'

        self.rect.x -= self.velocity

    def jump(self):
        self.rect.y -= self.jump_velocity
        self.jump_velocity -= self.jump_deceleration
        if self.jump_velocity < -20:
            self.isJump = False
            self.jump_velocity = 20

    def launch_kunai(self):
        self.all_kunai.add(Kunai(self))

    def launch_fireball(self):
        if self.magic > 100*0.2:
            self.all_fireball.add(Fireball(self))
            self.magic -= 100*0.2

    def launch_superkunai(self):
        if self.magic == 200:
            self.all_superkunai.add(Superkunai(self))
            self.magic -= 200





