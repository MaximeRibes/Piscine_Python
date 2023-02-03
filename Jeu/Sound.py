import pygame

class SoundManager:
    def __init__(self):
        #self.sounds = pygame.mixer.Set_volume(0.25)
        self.sounds = {
            'marche': pygame.mixer.Sound('Assets/sounds/marche_feuille.wav'),
            'épée_vide': pygame.mixer.Sound('Assets/sounds/épée_vide.wav'),
            'épée_épée': pygame.mixer.Sound('Assets/sounds/épée_épée.wav'),
            'coup_fort': pygame.mixer.Sound('Assets/sounds/coup_fort.wav'),
        }


    def play(self, name):
        self.sounds[name].play()