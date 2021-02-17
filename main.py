# Coding : UTF-8

# ------Importation des bibliothèques ----------------------------------------------------------------------------------
import pygame
from game import Game

# Initialisation du module
pygame.init()


# Création et configuration de la fenêtre du jeu
pygame.display.set_caption("Ninja Battle Game")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()

running = True

# Boucle du jeu
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(background, (-1300, -200))

    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)

    for zombie_male in game.all_zombie_male:
        zombie_male.forward()
    # Appliquer les images des monstres de type zombie male
    game.all_zombie_male.draw(screen)

    for kunai in game.player.all_projectiles:
        kunai.move()
    # Appliquer l'image du kunai
    game.player.all_projectiles.draw(screen)

    # Contrôle de la direction du joueur.
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < screen.get_width() - game.player.rect.width:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    # Mise à jour de l'écran
    pygame.time.delay(10)
    pygame.display.flip()

    # Récupération des actions de l'utilisateur
    for event in pygame.event.get():
        # Fermeture de la fenetre de jeu.
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Enregistrement des touches apuyées par le joueur dans le dictionnaire game.pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Fermeture de la fenetre de jeu avec la touche Echap.
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
            # Fnction sauter du joueur
            elif event.key == pygame.K_SPACE:
                game.player.isJump = True

            elif event.key == pygame.K_d:
                game.player.launch_kunai()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    # Contrôle du saut du joueur
    if game.player.isJump:
        game.player.jump()


