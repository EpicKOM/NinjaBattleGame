# Coding : UTF-8
# Author : EpicKOM

# ------Importation des bibliothèques ----------------------------------------------------------------------------------


import pygame
import sys
import random
from game import Game

# Initialisation du module pygame
pygame.init()

# Définir une clock et le nombre de FPS
clock = pygame.time.Clock()
FPS = 70

# Création et configuration de la fenêtre de jeu
pygame.display.set_caption("Ninja Battle Game")
screen = pygame.display.set_mode((1080, 720))
gameIcon = pygame.image.load('assets/design/icon.png')
gameIcon = pygame.transform.scale(gameIcon, (30, 30))
pygame.display.set_icon(gameIcon)

# Chargement des images statiques
background = pygame.image.load('assets/design/bg.jpg')
background_bw = pygame.image.load('assets/design/bg_bw.jpg')
magic_icon = pygame.image.load('assets/design/magic.png')
magic_icon = pygame.transform.scale(magic_icon, (19, 30))
rounds_image = pygame.image.load('assets/design/rounds.png')
rounds_image = pygame.transform.scale(rounds_image, (80, 69))

# Chargement de la police d'écriture
font_game = pygame.font.SysFont('arial', 20, True)
font_rounds = pygame.font.SysFont('monospace', 40, True)

# ----------------------------------------------------------------------------------------------------------------------

# Déclaration des Userevent

# Evénement lors de la fin du round song
ROUND_SONG_END = pygame.USEREVENT
ZOMBIES_SCREAM = pygame.USEREVENT + 1
HEART_BONUS = pygame.USEREVENT + 2
POISON = pygame.USEREVENT + 3

pygame.time.set_timer(ZOMBIES_SCREAM, 15000)
pygame.time.set_timer(HEART_BONUS, 105000)
pygame.time.set_timer(POISON, 60000)


game = Game()
running = True

# Boucle du jeu
while running:
    # Appliquer l'image du fond en mode Kamehameha
    if game.kamehameha_mode:
        screen.blit(background_bw, (-1300, -200))

    # Appliquer l'image du fond
    else:
        screen.blit(background, (-1300, -200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    # Appliquer le nombre de FPS
    fps_text = font_game.render(f"FPS: {clock.get_fps():.0f}", True, (255, 255, 255))
    screen.blit(fps_text, (screen.get_width() - fps_text.get_width() - 20, 20))

    # Partie terminée, GAME OVER
    if game.game_finish and not game.player.isJump:
        game.player.animation_speed = 0.1
        if game.finish_scene:
            if pygame.mixer.get_busy():
                pygame.mixer.stop()
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.stop()
            game.player.animation = True
            game.sound_manager.play('game_over', 0.2, 0)
            game.finish_scene = False

        if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
            game.player.animate('ninja', 'gover_right')
            if game.player.end_animation:
                game.game_results = True

        else:
            game.player.animate('ninja', 'gover_left')
            if game.player.end_animation:
                game.game_results = True

        if game.game_results:
            # Affichage des résultats de la partie
            game.game_over(screen)

    # Partie en cours
    else:

        # Gestion du déclenchement d'un nouveau niveau
        # -------------------------------------------------------------------------------
        if game.monster_counter >= game.target_number:
            for zombie in game.all_zombies_right:
                if zombie.rect.x >= 1080:
                    zombie.kill()
                if zombie.rect.x + zombie.image.get_width() <= 0:
                    zombie.kill()

            for zombie in game.all_zombies_left:
                if zombie.rect.x >= 1080:
                    zombie.kill()
                if zombie.rect.x + zombie.image.get_width() <= 0:
                    zombie.kill()

            if len(game.all_zombies_left) <= 0 and len(game.all_zombies_right) <= 0:
                if game.round % 2 == 0:
                    pygame.mixer.music.set_endevent(ROUND_SONG_END)
                    pygame.mixer.music.load('assets/music/new_round_pair.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play()
                else:
                    pygame.mixer.music.set_endevent(ROUND_SONG_END)
                    pygame.mixer.music.load('assets/music/new_round_impair.mp3')
                    pygame.mixer.music.set_volume(0.3)
                    pygame.mixer.music.play()

                if game.round == 0:
                    game.monster_counter = -1
                else:
                    game.monster_counter = 0

        # Affichage de l'icone magie
        screen.blit(magic_icon, (20, 20))
        round_text = font_rounds.render(f'{game.round}', True, (249, 49, 84))
        screen.blit(rounds_image, ((240 - rounds_image.get_width())/2 + 20, 40 + magic_icon.get_width()))
        screen.blit(round_text, (100 + (rounds_image.get_width() - round_text.get_width()) / 2, 74))

        # Affichage des jauges de vie et de magie du joueur
        game.player.update_health_bar(screen)
        game.player.update_magic_bar(screen, magic_icon.get_height())

        # Appliquer l'image des armes
        game.player.all_kunai_right.draw(screen)
        game.player.all_kunai_left.draw(screen)
        game.player.all_fireball_right.draw(screen)
        game.player.all_fireball_left.draw(screen)
        game.player.all_kamehameha_right.draw(screen)
        game.player.all_kamehameha_left.draw(screen)

        # Appliquer l'image des énemies
        game.all_zombies_right.draw(screen)
        game.all_zombies_left.draw(screen)

        # Appliquer l'image des items
        game.all_heart.draw(screen)
        game.all_flask.draw(screen)

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
                    zombie.kill()
                    game.all_zombies_right.empty()

            for zombie in game.all_zombies_left:
                zombie.animation_speed = 0.2
                zombie.animate('zombie', 'disappear')
                if zombie.end_animation:
                    zombie.kill()
                    game.all_zombies_right.empty()

            if len(game.all_zombies_right) <= 0 and len(game.all_zombies_left) <= 0:
                game.dismiss_monsters = False
                pygame.time.wait(20)
                game.game_finish = True

        else:
            for zombie in game.all_zombies_right:
                zombie.move_left()
                zombie.animate('zombie', f'{zombie.random_zombie}walk_left')
                if zombie.rect.x == 1080:
                    zombie_sound = random.choice(['zombie_1', 'zombie_2', 'zombie_3', 'zombie_6', 'zombie_7'])
                    game.sound_manager.play(f'{zombie_sound}', 0.1, 0)

                if zombie.zombie_attack and not zombie.attack_reverse:
                    zombie.animate('zombie', f'{zombie.random_zombie}attack_left')
                elif zombie.zombie_attack and zombie.attack_reverse:
                    zombie.animate('zombie', f'{zombie.random_zombie}attack_right')
                zombie.update_health_bar(screen)

            for zombie in game.all_zombies_left:
                zombie.move_right()
                zombie.animate('zombie', f'{zombie.random_zombie}walk_right')
                if zombie.rect.x == 0:
                    zombie_sound = random.choice(['zombie_1', 'zombie_2', 'zombie_3', 'zombie_6', 'zombie_7'])
                    game.sound_manager.play(f'{zombie_sound}', 0.1, 0)
                if zombie.zombie_attack and not zombie.attack_reverse:
                    zombie.animate('zombie', f'{zombie.random_zombie}attack_right')
                elif zombie.zombie_attack and zombie.attack_reverse:
                    zombie.animate('zombie', f'{zombie.random_zombie}attack_left')
                zombie.update_health_bar(screen)

        if game.key_pressed.get(pygame.K_LEFT) and game.player.rect.x >= 0 and not game.kamehameha_mode:
            game.player.run_left()
            game.player.animate('ninja', 'run_left')

        elif game.key_pressed.get(pygame.K_RIGHT) and game.player.rect.x <= screen.get_width()-game.player.image.get_width() and not game.kamehameha_mode:
            game.player.run_right()
            game.player.animate('ninja', 'run_right')

        if game.player.throw_animation:
            if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                game.player.animate('ninja', 'throw_right')
            else:
                game.player.animate('ninja', 'throw_left')

        if game.player.isJump:
            game.player.jump()

        for kamehameha in game.player.all_kamehameha_right:
            if kamehameha.throw_kamehameha:
                game.sound_manager.stop('running_right')
                game.player.kamehameha_enabled_right()
                kamehameha.animation_speed = 0.2
                kamehameha.start_animation()
                kamehameha.animate('kamehameha', 'kame_right')
                for zombie in game.all_zombies_right:
                    zombie.stop_move()
                    if game.check_collision(zombie, game.player.all_kamehameha_right):

                        if zombie.rect.x < 1080:
                            zombie.animation_speed = 0.2
                            zombie.animate('zombie', 'disappear')

                            if zombie.end_animation:
                                game.sound_manager.play('poof', 0.2, 0)
                                zombie.kamehameha_damage()

                    else:
                        zombie.current_image = 0

                for zombie in game.all_zombies_left:
                    zombie.stop_move()
                    if game.check_collision(zombie, game.player.all_kamehameha_right):

                        if zombie.rect.x > 0 - zombie.image.get_width():
                            zombie.animation_speed = 0.2
                            zombie.animate('zombie', 'disappear')

                            if zombie.end_animation:
                                game.sound_manager.play('poof', 0.2, 0)
                                zombie.kamehameha_damage()

                    else:
                        zombie.current_image = 0

            if kamehameha.end_animation:
                for zombie in game.all_zombies_right:
                    zombie.start_move()
                for zombie in game.all_zombies_left:
                    zombie.start_move()
                game.sound_manager.play('fatality', 0.9, 0)
                game.player.idle_right()
                game.player.start_move()
                kamehameha.remove_right()
                game.kamehameha_mode = False
                game.player.throw_kamehameha = False

        for kamehameha in game.player.all_kamehameha_left:
            if kamehameha.throw_kamehameha:
                game.sound_manager.stop('running_left')
                game.player.kamehameha_enabled_left()
                kamehameha.animation_speed = 0.2
                kamehameha.start_animation()
                kamehameha.animate('kamehameha', 'kame_left')
                kamehameha.rect.x = game.player.rect.x + 55 - kamehameha.image.get_width()

                for zombie in game.all_zombies_left:
                    zombie.stop_move()
                    if game.check_collision(zombie, game.player.all_kamehameha_left):

                        if zombie.rect.x > 0 - zombie.image.get_width():
                            zombie.animation_speed = 0.2
                            zombie.animate('zombie', 'disappear')

                            if zombie.end_animation:
                                game.sound_manager.play('poof', 0.2, 0)
                                zombie.kamehameha_damage()

                    else:
                        zombie.current_image = 0

                for zombie in game.all_zombies_right:
                    zombie.stop_move()
                    if game.check_collision(zombie, game.player.all_kamehameha_left):

                        if zombie.rect.x < 1080:
                            zombie.animation_speed = 0.2
                            zombie.animate('zombie', 'disappear')

                            if zombie.end_animation:
                                game.sound_manager.play('poof', 0.2, 0)
                                zombie.kamehameha_damage()

                    else:
                        zombie.current_image = 0

            if kamehameha.end_animation:
                for zombie in game.all_zombies_right:
                    zombie.start_move()
                for zombie in game.all_zombies_left:
                    zombie.start_move()
                game.sound_manager.play('fatality', 0.9, 0)
                game.player.idle_left()
                game.player.start_move()
                kamehameha.remove_left()
                game.kamehameha_mode = False
                game.player.throw_kamehameha = False

        for heart in game.all_heart:
            heart.move()

        for poison in game.all_flask:
            poison.move()

    # Mise à jour de l'écran
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

            elif event.key == pygame.K_LEFT and not game.game_finish and not game.kamehameha_mode:
                game.sound_manager.play('running_left', 0.04, -1)

            elif event.key == pygame.K_RIGHT and not game.game_finish and not game.kamehameha_mode:
                game.sound_manager.play('running_right', 0.04, -1)

            elif event.key == pygame.K_SPACE and not game.game_finish and not game.kamehameha_mode:
                if game.player.rect.y == 550:
                    game.sound_manager.play('jump', 0.02, 0)
                game.player.jump_animation = True
                game.player.isJump = True

            elif event.key == pygame.K_SPACE and game.game_finish and game.game_replay:
                # game.game_finish = False
                print('The replay function is not yet implemented.\nTo replay, close the window and restart the '
                      'main.py program')

            elif event.key == pygame.K_d and not game.player.throw_animation and not game.game_finish and not game.kamehameha_mode:
                game.player.throw_animation = True
                game.sound_manager.play('kunai_throw', 0.3, 0)
                if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                    game.player.launch_kunai_right()
                else:
                    game.player.launch_kunai_left()

            elif event.key == pygame.K_z and not game.player.throw_animation and not game.game_finish and not game.kamehameha_mode:
                if game.player.magic_power >= 80:
                    game.sound_manager.play('fireball', 0.08, 0)
                    game.player.throw_animation = True
                    if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                        game.player.launch_fireball_right()
                    else:
                        game.player.launch_fireball_left()
                else:
                    game.sound_manager.play('duck', 0.06, 0)

            elif event.key == pygame.K_q and not game.game_finish and len(game.player.all_kamehameha_right) < 1 and len(game.player.all_kamehameha_left) < 1:
                if game.player.magic_power >= game.player.max_magic_power:
                    game.kamehameha_mode = True
                    game.sound_manager.play('bazooka', 0.5, 0)
                    game.player.throw_kamehameha = True
                    game.sound_manager.play('test1', 0.1, 0)
                    if 'right' in game.player.image_name or 'right' in game.player.image_name[0]:
                        game.player.launch_kamehameha_right()
                    else:
                        game.player.launch_kamehameha_left()

                else:
                    game.sound_manager.play('duck', 0.06, 0)

        elif event.type == pygame.KEYUP:
            game.key_pressed[event.key] = False

            if event.key == pygame.K_RIGHT and not game.game_finish and not game.kamehameha_mode:
                game.sound_manager.stop('running_right')
                game.player.idle_right()
                game.player.stop_animation()

            elif event.key == pygame.K_LEFT and not game.game_finish and not game.kamehameha_mode:
                game.sound_manager.stop('running_left')
                game.player.idle_left()
                game.player.stop_animation()

        # Déclenchement du générateur de niveau (game engine) à la fin d'un new round song
        elif event.type == ROUND_SONG_END:
            game.game_engine()

        elif event.type == ZOMBIES_SCREAM and len(game.all_zombies_left) > 0 and len(game.all_zombies_right) > 0:
            if pygame.mixer.get_busy():
                pass
            else:
                zombie_sound = random.choice(['zombie_4', 'zombie_5'])
                game.sound_manager.play(f'{zombie_sound}', 0.1, 0)

        elif event.type == HEART_BONUS and len(game.all_zombies_left) > 0 and len(game.all_zombies_right) > 0:
            game.spawn_heart()

        elif event.type == POISON and len(game.all_zombies_left) > 0 and len(game.all_zombies_right) > 0:
            game.spawn_flask()

    clock.tick(FPS)
