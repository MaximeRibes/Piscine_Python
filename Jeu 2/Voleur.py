import pygame
import DPS
 
class Voleur(DPS):
    def __init__(self):
        self.image = pygame.image.load('')
        self.rect = self.image.get_rect()
    
    def barre_energie(self):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_pv, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.max_pv, 5])
