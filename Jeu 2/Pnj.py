import pygame

class Pnj(pygame.sprite.Sprite):
    def __init__(self, nom="", image=""):
        self.nom = nom
        self.image = image


    def parole(self):
        print(f"Bonjour je m'appelle {self.nom}")

villageois = Pnj(nom="Villageois", image=pygame.image.load('Assets\pnj\$villageois.png'))
garde = Pnj(nom="Garde", image=pygame.image.load('Assets\pnj\$garde.png'))