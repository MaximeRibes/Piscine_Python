import math

import pygame
import math

class Menu():
    def __init__(self):
        screen = pygame.display.set_mode((1619, 903))
        # importer charger notre bannière
        banner = pygame.image.load('Assets\$banner.jpg')
        # pour modifier la taille
        # banner = pygame.transform.scale(banner, (500,500))
        banner_rect = banner.get_rect()
        banner_rect.x = math.ceil(screen.get_width() / 2.3)

        # import charger notre bouton pour lancer la partie
        play_button = pygame.image.load('Assets\$start_2.png')
        # pour modifier la taille
        # play_button = pygame.transform.scale(play_button, (500,500))
        play_button_rect = play_button.get_rect()
        play_button_rect.x = math.ceil(screen.get_width() / 2.3)
        play_button_rect.y = math.ceil(screen.get_height() / 2)