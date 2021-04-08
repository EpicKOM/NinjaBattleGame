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
            'test1': pygame.mixer.Sound("assets/sounds/test1.mp3"),
            'ko': pygame.mixer.Sound("assets/sounds/ko.mp3"),
            'bazooka': pygame.mixer.Sound("assets/sounds/bazooka.mp3"),
            'heart': pygame.mixer.Sound("assets/sounds/heart.mp3"),
            'poison': pygame.mixer.Sound("assets/sounds/poison.mp3"),
            'zombie_1': pygame.mixer.Sound("assets/sounds/zombie_sound_1.mp3"),
            'zombie_2': pygame.mixer.Sound("assets/sounds/zombie_sound_2.mp3"),
            'zombie_3': pygame.mixer.Sound("assets/sounds/zombie_sound_3.mp3"),
            'zombie_4': pygame.mixer.Sound("assets/sounds/zombie_sound_4.mp3"),
            'zombie_5': pygame.mixer.Sound("assets/sounds/zombie_sound_5.mp3"),
            'zombie_6': pygame.mixer.Sound("assets/sounds/zombie_sound_6.mp3"),
            'zombie_7': pygame.mixer.Sound("assets/sounds/zombie_sound_7.mp3"),
        }

    def play(self, name, volume, loop):
        self.sounds[name].set_volume(volume)
        self.sounds[name].play(loops=loop)

    def stop(self, name):
        self.sounds[name].stop()