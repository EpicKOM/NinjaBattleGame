import pygame


# Classe qui va gérer l'énemie de type Zombie male
class ZombieMale(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 50
        self.attack = 5
        self.image = pygame.image.load('assets/zombie_male.png')
        self.image = pygame.transform.scale(self.image, (99, 120))
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 552
        self.velocity = 4

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self. rect.x -= self.velocity

