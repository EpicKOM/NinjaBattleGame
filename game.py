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
        self.kill = 0
        self.score = 0

    def start(self):
        self.status = True
        self.spawn_monsters()
        self.spawn_monsters()

    def game_over(self):
        self.status = False
        self.player.rect.x = 505
        self.player.rect.y = 550
        self.player.magic = 0
        self.all_zombie = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.score = 0
        self.kill = 0

    def update(self, screen):
        font = pygame.font.SysFont('verdana', 25, 1)
        kill_text = font.render('{}'.format(self.kill), 1, (249, 49, 84))
        screen.blit(kill_text, (80, 105))

        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Appliquer la barre de magie du joueur
        self.player.magic_progress_bar(screen)

        # Appliquer la barre de vie du joueur
        self.player.update_health_bar(screen)

        for zombie in self.all_zombie:
            zombie.forward()
            zombie.update_health_bar(screen)

        # Appliquer les images des monstres de type zombie male
        self.all_zombie.draw(screen)

        for fireball in self.player.all_fireball:
            fireball.move()

        for superkunai in self.player.all_superkunai:
            superkunai.move()

        # Appliquer l'image de la fireball
        self.player.all_fireball.draw(screen)

        # Appliquer l'image du superkunai
        self.player.all_superkunai.draw(screen)

        for kunai in self.player.all_kunai:
            kunai.move()
        # Appliquer l'image du kunai
        self.player.all_kunai.draw(screen)

        # Contrôle de la direction du joueur.
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width() - self.player.rect.width:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monsters(self):
        self.all_zombie.add(Zombie(self))


