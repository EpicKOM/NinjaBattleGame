# Coding : UTF-8

# ------Importation des bibliothèques ----------------------------------------------------------------------------------
import pygame
from player import Ninja
from enemies import Zombie


# Classe qui représente le jeu
class Game:
    def __init__(self):
        # Status du jeu
        self.status = False
        #Création d'un nouveau joueur
        self.all_players = pygame.sprite.Group()
        self.player = Ninja(self)
        self.all_players.add(self.player)
        # Groupe de sprite de type zombie mâle
        self.all_zombie = pygame.sprite.Group()
        # Sauvegarde de la touche préssée par le joueur
        self.pressed = {}
        self.start_song = pygame.mixer.Sound('assets/Kalimba.mp3')

    def start(self):
        self.start_song.play()
        self.status = True
        self.spawn_monsters()
        self.spawn_monsters()

    def game_over(self):
        self.status = False
        self.player.rect.x = 505
        self.player.rect.y = 550
        self.all_zombie = pygame.sprite.Group()
        self.player.health = self.player.max_health

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Appliquer la barre de vie du joueur
        self.player.update_health_bar(screen)

        for zombie in self.all_zombie:
            zombie.forward()
            zombie.update_health_bar(screen)

        # Appliquer les images des monstres de type zombie male
        self.all_zombie.draw(screen)

        for kunai in self.player.all_projectiles:
            kunai.move()
        # Appliquer l'image du kunai
        self.player.all_projectiles.draw(screen)

        # Contrôle de la direction du joueur.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monsters(self):
        self.all_zombie.add(Zombie(self))
