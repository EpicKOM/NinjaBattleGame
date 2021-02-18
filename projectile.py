import pygame

# Les projectiles du jeu


class Kunai(pygame.sprite.Sprite):
    def __init__(self, ninja):
        super().__init__()
        self.velocity = 6
        self.attack = 10
        self.ninja = ninja
        self.image = pygame.image.load('assets/kunai.png')
        self.image = pygame.transform.scale(self.image, (50, 10))
        self.rect = self.image.get_rect()
        self.rect.x = ninja.rect.x + 50
        self.rect.y = ninja.rect.y + 60
        self.origin_image = self.image
        self.angle = 0

    def remove(self):
        self.ninja.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity

        for monster in self.ninja.game.check_collision(self, self.ninja.game.all_zombie):
            self.remove()
            monster.damage(self.attack)

        if self.rect.x > 1080:
            self.remove()




