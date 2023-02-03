import pygame

import Soigneur
from Soigneur import *
from Personnage import *
from game import *


class Pretre(Soigneur, pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load('Assets\Hero\Pretre\marcher/Hobbit - run1.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.image_g = pygame.transform.flip(self.image, True, False)
        #factor = 2
        #width = int(self.image.width * factor)
        #height = int(self.image.height * factor)
        #self.image_resized = self.image.resize((self.image.width * 2, self.image.height * 2))
        self.rect = self.image.get_rect()
        self.rect.x = 145
        self.rect.y = 680
        self.speed = 5
        self.dps = 15
        self.pv = 100
        self.max_pv = 100
        self.armure = 5
        self.current_image = 0
        self.animation = True
        self.images = animations.get('Hobbit - run')
        self.imagesg = animationsg.get('Hobbit - run')

    def barre_de_vie(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 5, self.rect.y + 5, self.pv, 8])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 5, self.rect.y + 5, self.max_pv, 8])

    def degat(self, amount):
        subir = amount - self.armure
        if self.pv - amount >= 0:
            self.pv -= subir
        else:
            print("Vous êtes mort")

    def move_right(self):
        self.rect.x += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_stop(self):
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y


    def anime(self, loop=True):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]

    def animeg(self, loop=True):
        if self.animation:
            self.current_image += 1
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.imagesg[self.current_image]

def marcher():
    marche = []
    path = 'Assets/Hero/Pretre/marcher/Hobbit - run'

    for num in range(1, 10):
        marche_path = path + str(num) + '.png'
        img = pygame.image.load(marche_path)
        img_scale = pygame.transform.scale(img, (125, 125))
        marche.append(img_scale)

    return marche

def marcherg():
    marcheg = []
    path = 'Assets/Hero/Pretre/marcher/Hobbit - run'

    for num in range(1, 10):
        marcheg_path = path + str(num) + '.png'
        img = pygame.image.load(marcheg_path)
        img_scale = pygame.transform.scale(img, (125, 125))
        img_gauche = pygame.transform.flip(img_scale, True, False)
        marcheg.append(img_gauche)

    return marcheg

animations = {
    'Hobbit - run' : marcher()
}

animationsg = {
    'Hobbit - run' : marcherg()
}
