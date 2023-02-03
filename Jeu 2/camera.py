import pygame
from abc import ABC, abstractmethod
vec = pygame.math.Vector2


class Camera():
    def __init__(self, joueur):
        self.joueur = joueur
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)
        self.display_w, self.display_h = 500, 270
        self.const = vec(-self.display_w / 2 + joueur.rect.w / 2) #, -self.joueur.ground_y + 20)

    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

class CamScroll(ABC):
    def __init__(self, camera, joueur):
        self.camera = camera
        self.joueur = joueur

    @abstractmethod
    def scroll(self):
        pass

class Follow(CamScroll):
    def __init__(self, camera, joueur):
        CamScroll.__init__(self, camera, joueur)

    def scroll(self):
        self.camera.offset_float.x += (self.joueur.rect.x - self.camera.offset_float.x + self.camera.const.x)
        self.camera.offset_float.y += (self.joueur.rect.y - self.camera.offset_float.y + self.camera.const.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)

class Border(CamScroll):
    def __init__(self, camera, joueur):
        CamScroll.__init__(self, camera, joueur)

    def scroll(self):
        self.camera.offset_float.x += (self.joueur.rect.x - self.camera.offset_float.x + self.camera.const.x)
        self.camera.offset_float.y += (self.joueur.rect.y - self.camera.offset_float.y + self.camera.const.y)
        self.camera.offset.x, self.camera.offset.y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(self.joueur.left_border, self.camera.offset.x)
        self.camera.offset.x = min(self.camera.offset.x, self.joueur.right_border - self.camera.display_w)

class Auto(CamScroll):
    def __init__(self, camera, joueur):
        CamScroll.__init__(self, camera, joueur)

    def scroll(self):
        self.camera.offset.x += 1
