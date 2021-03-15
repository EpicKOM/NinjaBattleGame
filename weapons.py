import pygame


class Kunai(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load('assets/projectiles/kunai_right.png')
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.velocity = 6
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 55
        self.rect.y = self.player.rect.y + 60
        self.attack = 5

    def remove_right(self):
        self.player.all_kunai_right.remove(self)

    def remove_left(self):
        self.player.all_kunai_left.remove(self)

    def move_right(self):
        self.rect.x += self.velocity

        # Si le Kunai touche un ennemi --> Détruire le Kunai
        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_left):
            self.remove_right()
            zombie.damage(self.attack)

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_right):
            self.remove_right()
            zombie.damage(self.attack)

        # Vérifier si le Kunai est encore sur l'écran
        if self.rect.x > 1080 :
            self.remove_right()

    def move_left(self):
        self.rect.x -= self.velocity

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_left):
            self.remove_left()
            zombie.damage(self.attack)

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_right):
            self.remove_left()
            zombie.damage(self.attack)

        # Vérifier si le Kunai est encore sur l'écran
        if self.rect.x < 0:
            self.remove_left()


class Fireball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/projectiles/fireball.png')
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.velocity = 6


