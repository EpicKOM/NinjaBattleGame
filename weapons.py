import pygame
import animation


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
        if self.rect.x > 1080:
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
        if self.rect.x < 0 - self.image.get_width():
            self.remove_left()


class Fireball(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.image = pygame.image.load('assets/projectiles/fireball.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.velocity = 6
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 55
        self.rect.y = self.player.rect.y + 45
        self.attack = 20
        self.magic = 40
        self.origin_image = self.image
        self.angle = 0

    def rotate_right(self):
        self.angle -= 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def rotate_left(self):
        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove_right(self):
        self.player.all_fireball_right.remove(self)

    def remove_left(self):
        self.player.all_fireball_left.remove(self)

    def move_right(self):
        self.rect.x += self.velocity
        self.rotate_right()

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_left):
            self.remove_right()
            zombie.damage(self.attack)

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_right):
            self.remove_right()
            zombie.damage(self.attack)

        # Vérifier si la Fireball est encore sur l'écran
        if self.rect.x > 1080:
            self.remove_right()

    def move_left(self):
        self.rect.x -= self.velocity
        self.rotate_left()

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_left):
            self.remove_left()
            zombie.damage(self.attack)

        for zombie in self.player.game.check_collision(self, self.player.game.all_zombies_right):
            self.remove_left()
            zombie.damage(self.attack)

        # Vérifier si la Fireball est encore sur l'écran
        if self.rect.x < 0 -self.image.get_width():
            self.remove_left()


class Kamehameha(animation.AnimateSprite):
    def __init__(self, player):
        super().__init__('kamehameha', 'idle_right')
        self.player = player
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 40
        self.rect.y = self.player.rect.y + 58

    def remove_right(self):
        self.player.all_kamehameha_right.remove(self)

    def remove_left(self):
        self.player.all_kamehameha_left.remove(self)

