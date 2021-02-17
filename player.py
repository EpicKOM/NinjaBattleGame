# Coding : UTF-8

# ------Importation des bibliothèques ----------------------------------------------------------------------------------
import pygame
from projectile import Kunai


# Classe représentant le personnage principal (Un Ninja)
class Ninja(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.max_health = 100
        self.health = 100
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
        self.all_projectiles = pygame.sprite.Group()
        self.velocity_damage = 20

    def move_right(self):
        # Si le joueur n'est pas en collision avec un ennemi déplacement à droite autorisé'
        if not self.game.check_collision(self, self.game.all_zombie_male):
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
        self.all_projectiles.add(Kunai(self))






