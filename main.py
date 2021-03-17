# Coding : UTF-8
# Author : EpicKOM

# ------Importation des bibliothèques ----------------------------------------------------------------------------------


import pygame
import sys
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
magic_icon = pygame.transform.scale(magic_icon, (19, 30))
point_icon = pygame.image.load('assets/design/coins.png')
point_icon = pygame.transform.scale(point_icon, (30, 30))
font_points = pygame.font.SysFont('monospace', 20, True)
GO_font = pygame.font.SysFont("monospace", 95, True)
retry_font = pygame.font.SysFont("arial", 25, False)
GO_text = GO_font.render("Game Over !", True, (46, 46, 46))
retry_text = retry_font.render("Appuyer sur espace pour recommencer une partie.", True, (255, 255, 255))

game = Game()
running = True
# Boucle du jeu
while running:

    # Appliquer l'image de l'arrière plan du jeu
    screen.blit(background, (-1300, -200))
    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    if game.game_finish:
        # Partie terminée, GAME OVER
        if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
            game.player.animate('ninja', 'gover_right')
        else:
            game.player.animate('ninja', 'gover_left')
        screen.blit(GO_text, ((screen.get_width()-GO_text.get_width())/2, 60))

    else:
        screen.blit(magic_icon, (20, 20))
        screen.blit(point_icon, (15, 80))
        point_text = font_points.render(str(game.total_points), True, (255, 182, 40))
        game.player.update_health_bar(screen)
        game.player.update_magic_bar(screen, magic_icon.get_height())
        screen.blit(point_text, (60, 85))

        # Appliquer l'image des armes
        game.player.all_kunai_right.draw(screen)
        game.player.all_kunai_left.draw(screen)
        game.player.all_fireball_right.draw(screen)
        game.player.all_fireball_left.draw(screen)

        # Appliquer l'image des énemies
        game.all_zombies_right.draw(screen)
        game.all_zombies_left.draw(screen)

        for fireball in game.player.all_fireball_right:
            fireball.move_right()

        for fireball in game.player.all_fireball_left:
            fireball.move_left()

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
            sys.exit()

        # Evenement de type touche appuyée
        elif event.type == pygame.KEYDOWN:
            game.key_pressed[event.key] = True

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_SPACE and not game.game_finish:
                game.sound_manager.play('jump', 0.02)
                game.player.jump_animation = True
                game.player.isJump = True

            elif event.key == pygame.K_d and not game.player.throw_animation and not game.game_finish:
                game.player.throw_animation = True
                game.sound_manager.play('kunai_throw', 0.3)
                if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                    game.player.launch_kunai_right()
                else:
                    game.player.launch_kunai_left()

            elif event.key == pygame.K_z and not game.player.throw_animation and not game.game_finish:
                if game.player.magic_power >= 80:
                    game.sound_manager.play('fireball', 0.06)
                    game.player.throw_animation = True
                    if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                        game.player.launch_fireball_right()
                    else:
                        game.player.launch_fireball_left()
                else:
                    game.sound_manager.play('duck', 0.06)

        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False

            if event.key == pygame.K_RIGHT and not game.game_finish:
                game.player.idle_right()
                game.player.stop_animation()

            elif event.key == pygame.K_LEFT and not game.game_finish:
                game.player.idle_left()
                game.player.stop_animation()

    clock.tick(FPS)
