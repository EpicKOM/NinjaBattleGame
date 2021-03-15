# Coding : UTF-8
# Author : EpicKOM

# ------Importation des bibliothèques ----------------------------------------------------------------------------------


import pygame
import random
from game import Game

# Initialisation du module
pygame.init()

#Définir une clock
clock = pygame.time.Clock()
FPS = 100

# Création et configuration de la fenêtre de jeu
pygame.display.set_caption("Ninja Battle Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/design/bg.jpg')
magic_icon = pygame.image.load('assets/design/magic.png')
magic_icon = pygame.transform.scale(magic_icon, (25, 40))

game = Game()
running = True

# Boucle du jeu
while running:

    # Appliquer l'image de l'arrière plan du jeu
    screen.blit(background, (-1300, -200))
    screen.blit(magic_icon, (20, 20))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    game.player.update_health_bar(screen)
    game.player.update_magic_bar(screen, magic_icon.get_height())

    # Appliquer l'image des armes
    game.player.all_kunai_right.draw(screen)
    game.player.all_kunai_left.draw(screen)

    # Appliquer l'image des énemies
    game.all_zombies_right.draw(screen)
    game.all_zombies_left.draw(screen)

    for kunai in game.player.all_kunai_right:
        kunai.move_right()

    for kunai in game.player.all_kunai_left:
        kunai.move_left()

    for zombie in game.all_zombies_right:
        zombie.move_left()
        zombie.animate('zombie', f'{zombie.random_zombie}walk_left')
        if zombie.zombie_attack and not zombie.attack_reverse:
            zombie.animate('zombie', f'{zombie.random_zombie}attack_left')
        elif zombie.zombie_attack and zombie.attack_reverse:
            zombie.animate('zombie', f'{zombie.random_zombie}attack_right')
        zombie.update_health_bar(screen)

    for zombie in game.all_zombies_left:
        zombie.move_right()
        zombie.animate('zombie', f'{zombie.random_zombie}walk_right')
        if zombie.zombie_attack and not zombie.attack_reverse:
            zombie.animate('zombie', f'{zombie.random_zombie}attack_right')
        elif zombie.zombie_attack and zombie.attack_reverse:
            zombie.animate('zombie', f'{zombie.random_zombie}attack_left')
        zombie.update_health_bar(screen)

    if game.key_pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0:
        game.player.run_left()
        game.player.animate('ninja', 'run_left')

    elif game.key_pressed.get(pygame.K_RIGHT) and game.player.rect.x <= screen.get_width()-game.player.image.get_width():
        game.player.run_right()
        game.player.animate('ninja', 'run_right')

    if game.player.throw_animation:
        if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
            game.player.animate('ninja', 'throw_right')
        else:
            game.player.animate('ninja', 'throw_left')

    if game.player.isJump:
        game.player.jump()

    # Mise à jour de l'écran
    pygame.time.delay(10)
    pygame.display.flip()

    # ------------------------------------------------------------------------------------------------------------------
    # Gestion des événements

    # Récupération des actions de l'utilisateur
    for event in pygame.event.get():

        # Fermeture de la fenetre de jeu.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Evenement de type touche appuyée
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()

            elif event.key == pygame.K_SPACE:
                game.player.jump_animation = True
                game.player.isJump = True

            elif event.key == pygame.K_d and not game.player.throw_animation:
                game.player.throw_animation = True
                if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                    game.player.launch_kunai_right()
                else:
                    game.player.launch_kunai_left()

        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False

            if event.key == pygame.K_RIGHT:
                game.player.idle_right()
                game.player.stop_animation()

            elif event.key == pygame.K_LEFT:
                game.player.idle_left()
                game.player.stop_animation()

    clock.tick(FPS)
