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
            'running_left': pygame.mixer.Sound("assets/sounds/running.mp3"),
            'running_right': pygame.mixer.Sound("assets/sounds/running.mp3"),
            'fatality': pygame.mixer.Sound("assets/sounds/fatality.mp3"),
        }

    def play(self, name, volume, loop):
        self.sounds[name].set_volume(volume)
        self.sounds[name].play(loops=loop)

    def stop(self, name):
        self.sounds[name].stop()