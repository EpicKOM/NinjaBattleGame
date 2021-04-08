import pygame
import random


class Heart(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.h_velocity = 3
        self.v_velocity = 2
        self.v_velocity_memory = []
        self.image = pygame.image.load('assets/items/heart.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1081
        self.rect.y = 100
        self.life = 20

    def stop_move(self):
        self.v_velocity_memory.append(self.v_velocity)
        self.h_velocity = 0
        self.v_velocity = 0

    def start_move(self):
        self.h_velocity = 3
        self.v_velocity = self.v_velocity_memory[0]

    def remove(self):
        self.game.all_heart.remove(self)

    def move(self):
        if not self.game.check_collision(self, self.game.player_group):
            self.rect.x -= self.h_velocity
            self.rect.y += self.v_velocity
            if self.rect.y > 450:
                self.v_velocity = -2
            elif self.rect.y < 250:
                self.v_velocity = 2
        else:
            self.game.player.gain_life(self.life)
            self.game.sound_manager.play('heart', 0.2, 0)
            self.remove()


class Flask(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.attack = 25
        self.velocity = random.randint(1, 3)
        self.velocity_memory = []
        self.image = pygame.image.load('assets/items/flask.png')
        self.image = pygame.transform.scale(self.image, (63, 50))
        self.rect = self.image.get_rect()
        self.rect.x = 1081
        self.rect.y = 620

    def stop_move(self):
        self.velocity_memory.append(self.velocity)
        self.velocity = 0

    def start_move(self):
        self.velocity = self.velocity_memory[0]

    def remove(self):
        self.game.all_flask.remove(self)

    def move(self):
        if not self.game.check_collision(self, self.game.player_group):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)
            self.remove()
            self.game.sound_manager.play('poison', 0.4, 0)
