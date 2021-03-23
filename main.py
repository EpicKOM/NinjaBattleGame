# Coding : UTF-8
# Author : EpicKOM

# ------Importation des bibliothèques ----------------------------------------------------------------------------------


import pygame
import sys
from game import Game

# Initialisation du module
pygame.init()

#Définir une clock et gestion des FPS
clock = pygame.time.Clock()
FPS = 80

# Création et configuration de la fenêtre de jeu
pygame.display.set_caption("Ninja Battle Game")
screen = pygame.display.set_mode((1080, 720))
gameIcon = pygame.image.load('assets/design/icon.png')
gameIcon = pygame.transform.scale(gameIcon, (30, 30))
pygame.display.set_icon(gameIcon)


background = pygame.image.load('assets/design/bg.jpg')
magic_icon = pygame.image.load('assets/design/magic.png')
magic_icon = pygame.transform.scale(magic_icon, (19, 30))
point_icon = pygame.image.load('assets/design/coins.png')
point_icon = pygame.transform.scale(point_icon, (30, 30))

font_game = pygame.font.SysFont('arial', 20, True)

game = Game()
running = True

# Boucle du jeu
while running:

    # Appliquer l'image de l'arrière plan du jeu
    screen.blit(background, (-1300, -200))
    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    # Appliquer le nombre de FPS
    fps_text = font_game.render(f"FPS: {clock.get_fps():.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (screen.get_width() - fps_text.get_width() - 20, 20))

    if game.game_finish:
        # Partie terminée, GAME OVER

        game.player.animation_speed = 0.1
        if game.finish_scene:
            game.player.animation = True
            game.sound_manager.play('game_over', 0.06)
            game.finish_scene = False

        if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
            game.player.animate('ninja', 'gover_right')
        else:
            game.player.animate('ninja', 'gover_left')

        game.game_over(screen)

    else:
        point_text = font_game.render(str(game.total_points), True, (255, 182, 40))

        screen.blit(magic_icon, (20, 20))
        # screen.blit(point_icon, (15, 80))
        # screen.blit(point_text, (60, 85))

        game.player.update_health_bar(screen)
        game.player.update_magic_bar(screen, magic_icon.get_height())

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

        if game.dismiss_monsters:
            for zombie in game.all_zombies_right:
                zombie.animation_speed = 0.2
                zombie.animate('zombie', 'disappear')
                if zombie.end_animation:
                    zombie.remove()

            for zombie in game.all_zombies_left:
                zombie.animation_speed = 0.2
                zombie.animate('zombie', 'disappear')
                if zombie.end_animation:
                    zombie.remove()

            if len(game.all_zombies_right) <= 0 and len(game.all_zombies_left) <= 0:
                game.game_finish = True

        else:
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
                if game.player.rect.y == 550:
                    game.sound_manager.play('jump', 0.02)
                game.player.jump_animation = True
                game.player.isJump = True

            elif event.key == pygame.K_SPACE and game.game_finish:
                print('On rejoue !')

            elif event.key == pygame.K_d and not game.player.throw_animation and not game.game_finish:
                game.player.throw_animation = True
                game.sound_manager.play('kunai_throw', 0.3)
                if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                    game.player.launch_kunai_right()
                else:
                    game.player.launch_kunai_left()

            elif event.key == pygame.K_z and not game.player.throw_animation and not game.game_finish:
                if game.player.magic_power >= 80:
                    game.sound_manager.play('fireball', 0.08)
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
