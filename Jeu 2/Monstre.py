import pygame
pygame.init()


# classe qui gère la notion de monstre
class Monstre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_pv = 100
        self.attack = 20
        self.speed = 5
        self.armure = 0

    def barre_de_vie(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_pv, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.max_pv, 5])

    def degat(self, amount):
        subir = amount - self.armure
        if self.pv - amount > amount:
            self.pv -= subir

