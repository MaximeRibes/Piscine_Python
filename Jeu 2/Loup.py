import pygame
pygame.init()

from Monstre import Monstre

# classe qui gère la notion de monstre
class Loup(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Assets/Mechants/Loup/Loup2.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 400
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.speed = 5
