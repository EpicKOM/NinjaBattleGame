import pygame

# Les projectiles du jeu


class Kunai(pygame.sprite.Sprite):
    def __init__(self, ninja):
        super().__init__()
        self.velocity = 6
        self.attack = 8
        self.ninja = ninja
        self.image = pygame.image.load('assets/projectiles/kunai.png')
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.rect = self.image.get_rect()
        self.rect.x = ninja.rect.x + 50
        self.rect.y = ninja.rect.y + 60

    def remove(self):
        self.ninja.all_kunai.remove(self)

    def move(self):
        self.rect.x += self.velocity

        for monster in self.ninja.game.check_collision(self, self.ninja.game.all_zombie):
            self.remove()
            monster.damage(self.attack, False)

        if self.rect.x > 1080:
            self.remove()


class Fireball(pygame.sprite.Sprite):
    def __init__(self, ninja):
        super().__init__()
        self.ninja = ninja
        self.velocity = 6
        self.attack = 25
        self.magic = 10
        self.image = pygame.image.load('assets/projectiles/fireball.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = ninja.rect.x + 50
        self.rect.y = ninja.rect.y + 45
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle -= 15
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.ninja.all_fireball.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.ninja.game.check_collision(self, self.ninja.game.all_zombie):
            self.remove()
            monster.damage(self.attack, False)

        if self.rect.x > 1080:
            self.remove()


class Superkunai(pygame.sprite.Sprite):
    def __init__(self, ninja):
        super().__init__()
        self.ninja = ninja
        self.velocity = 6
        self.attack = 1000
        self.magic = 200
        self.image = pygame.image.load('assets/projectiles/kunai.png')
        self.rect = self.image.get_rect()
        self.rect.x = ninja.rect.x + 50
        self.rect.y = ninja.rect.y + 45

    def remove(self):
        self.ninja.all_superkunai.remove(self)

    def move(self):
        self.rect.x += self.velocity

        for monster in self.ninja.game.check_collision(self, self.ninja.game.all_zombie):
           monster.damage(self.attack, True)

        if self.rect.x > 1080:
            self.remove()
