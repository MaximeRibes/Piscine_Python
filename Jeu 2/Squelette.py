import pygame
pygame.init()

import Monstre

# classe qui gère la notion de monstre
class Squelette(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 80
        self.max_health = 80
        self.attack = 5
        self.speed = 5
        self.image = pygame.image.load('Assets/Mechants/Squelette/Squelette.png')
        self.rect = self.image.get_rect()