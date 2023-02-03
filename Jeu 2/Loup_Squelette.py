import pygame
pygame.init()

import Monstre

# classe qui gère la notion de monstre
class Loup_Squelette(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 80
        self.max_health = 80
        self.attack = 7
        self.speed = 7
        self.image = pygame.image.load('Assets/Mechants/Loup_Squelette/Loup_Squelette.png')
        self.rect = self.image.get_rect()