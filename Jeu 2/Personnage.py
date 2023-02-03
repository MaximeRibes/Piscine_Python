import pygame
pygame.init()
 
class Personnage(): # pygame.sprite.Sprite
    def __init__(self):
        super().__init__()
        self.pv = 100
        self.max_pv = 100
        self.ressource = 100
        self.max_ressource = 100
        self.armure = 5
        self.attack = 20

    #def barre_ressource(self):
        #pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 30, self.rect.y - 40, self.ressource, 5])
        #pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 30, self.rect.y - 40, self.max_ressource, 5])
