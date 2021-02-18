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
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (700, 465))
banner_width = banner.get_width()
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = (screen.get_width() - play_button.get_width())/2
play_button_rect.y = 450

game = Game()

running = True

# Boucle du jeu
while running:

    # Appliquer l'arrière plan du jeu
    screen.blit(background, (-1300, -200))

    # Vérifier si le jeu a commencé.
    if game.status:
        game.update(screen)
    else:
        # Ecran de bienvenue
        screen.blit(banner, ((screen.get_width()-banner_width)/2, 50))
        screen.blit(play_button, play_button_rect)

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
            # elif event.key == pygame.K_SPACE:
            #     game.player.isJump = True

            elif event.key == pygame.K_d:
                game.player.launch_kunai()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


    # Contrôle du saut du joueur
    # if game.player.isJump:
    #     game.player.jump()


