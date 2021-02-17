# Coding : UTF-8

# ------Importation des bibliothèques ----------------------------------------------------------------------------------
import pygame
from player import Ninja
from enemies import ZombieMale


# Classe qui représente le jeu
class Game:
    def __init__(self):
        #Création d'un nouveau joueur
        self.all_players = pygame.sprite.Group()
        self.player = Ninja(self)
        self.all_players.add(self.player)
        # Groupe de sprite de type zombie mâle
        self.all_zombie_male = pygame.sprite.Group()
        # Sauvegarde de la touche préssée par le joueur
        self.pressed = {}
        self.spawn_monsters()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monsters(self):
        self.all_zombie_male.add(ZombieMale(self))
