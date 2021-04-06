import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.h_velocity = 2
        self.v_velocity = 2
        self.image = pygame.image.load('assets/items/heart.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = 100
        self.life = 20

    def move(self):
        self.rect.x -= self.h_velocity
        self.rect.y += self.v_velocity
        if self.rect.y > 450:
            self.v_velocity = -2
        elif self.rect.y < 250:
            self.v_velocity = 2


class Flask(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 20
        self.image = pygame.image.load('assets/items/flask.png')
        self.image = pygame.transform.scale(self.image, (63, 50))
        self.rect = self.image.get_rect()