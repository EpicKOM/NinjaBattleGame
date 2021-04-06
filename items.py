import pygame


class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/items/heart.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.life = 20


class Flask(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.attack = 20
        self.image = pygame.image.load('assets/items/flask.png')
        self.image = pygame.transform.scale(self.image, (63, 50))
        self.rect = self.image.get_rect()