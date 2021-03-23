import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.mp3"),
            'jump': pygame.mixer.Sound("assets/sounds/jump.mp3"),
            'kunai_throw': pygame.mixer.Sound("assets/sounds/kunai_throw.ogg"),
            'duck': pygame.mixer.Sound("assets/sounds/duck.ogg"),
            'fireball': pygame.mixer.Sound("assets/sounds/fireball.mp3"),
            'poof': pygame.mixer.Sound("assets/sounds/poof.mp3"),
            'punch': pygame.mixer.Sound("assets/sounds/punch.mp3"),
        }

    def play(self, name, volume):
        self.sounds[name].set_volume(volume)
        self.sounds[name].play()