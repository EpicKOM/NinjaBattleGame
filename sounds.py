import pygame


class SoundManager:
    def __init__(self):
        self.sounds = {
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'jump': pygame.mixer.Sound("assets/sounds/jump.ogg"),
            'kunai_throw': pygame.mixer.Sound("assets/sounds/kunai_throw.ogg"),
            'duck': pygame.mixer.Sound("assets/sounds/duck.ogg"),
            'fireball': pygame.mixer.Sound("assets/sounds/fireball.ogg"),
            'poof': pygame.mixer.Sound("assets/sounds/poof.ogg"),
            'punch': pygame.mixer.Sound("assets/sounds/punch.ogg"),
            'running_left': pygame.mixer.Sound("assets/sounds/running.ogg"),
            'running_right': pygame.mixer.Sound("assets/sounds/running.ogg"),
            'fatality': pygame.mixer.Sound("assets/sounds/fatality.ogg"),
            'test1': pygame.mixer.Sound("assets/sounds/kamehameha.ogg"),
            'ko': pygame.mixer.Sound("assets/sounds/ko.ogg"),
            'bazooka': pygame.mixer.Sound("assets/sounds/bazooka.ogg"),
            'heart': pygame.mixer.Sound("assets/sounds/heart.ogg"),
            'poison': pygame.mixer.Sound("assets/sounds/poison.ogg"),
            'nope': pygame.mixer.Sound("assets/sounds/nope.ogg"),
            'zombie_1': pygame.mixer.Sound("assets/sounds/zombie_sound_1.ogg"),
            'zombie_2': pygame.mixer.Sound("assets/sounds/zombie_sound_2.ogg"),
            'zombie_3': pygame.mixer.Sound("assets/sounds/zombie_sound_3.ogg"),
            'zombie_4': pygame.mixer.Sound("assets/sounds/zombie_sound_4.ogg"),
            'zombie_6': pygame.mixer.Sound("assets/sounds/zombie_sound_6.ogg"),
            'ambience': pygame.mixer.Sound("assets/sounds/soundtrack.ogg"),
        }

    def play(self, name, volume, loop):
        self.sounds[name].set_volume(volume)
        self.sounds[name].play(loops=loop)

    def stop(self, name):
        self.sounds[name].stop()