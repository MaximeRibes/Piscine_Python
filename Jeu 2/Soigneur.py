import pygame
from Personnage import Personnage
 
class Soigneur(Personnage):
    def __init__(self):
        Personnage.attack -= 10/100
        Personnage.pv -= 10/100
        Personnage.max_pv -= 10/100
