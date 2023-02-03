import pygame
import pytmx
import pyscroll
import math
pygame.init()

from game import *
from game2 import *
from Pnj import *
from Pretre import *
from camera import *
import time
from Monstre import Monstre
from Loup import Loup
from Menu import *


# générer la fenêtre de jeu
pygame.display.set_caption("World of Minecraft")

# Taille Map1 (1619, 903)
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

# charger le jeu
game = Game()

#arrière-plan du jeu
background = pygame.image.load('Assets/Cartes/map1.png')

clock = pygame.time.Clock()

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer ensemble images des monstres
    #game.all_Monstres.draw(screen)

    #verifier si notre jeu a commencé ou non
    if game.is_playing:
        # declencher les instructions de la partie
        game.update(screen)
    # verifier si notre jeu n'a pas commencé
    else:
        # ajouter mon ecran de bienvenue
        screen.blit(banner, banner_rect)
        screen.blit(play_button, play_button_rect)

    #print(game.joueur.rect.x, "x")
    #print(game.joueur.rect.y, "y")

    if game.pressed.get(pygame.K_RIGHT) and game.joueur.rect.x + game.joueur.rect.width < background.get_width():
        game.joueur.move_right()
        game.joueur.anime()
        game.sounds_manager.play('marche')
    elif game.pressed.get(pygame.K_LEFT) and game.joueur.rect.x > 0:
        game.joueur.move_left()
        game.joueur.animeg()
        game.sounds_manager.play('marche')

    if game.pressed.get(pygame.K_UP) and game.joueur.rect.y > 0:
        game.joueur.move_up()
        game.joueur.anime()
        game.sounds_manager.play('marche')
    elif game.pressed.get(pygame.K_DOWN) and game.joueur.rect.y + game.joueur.rect.height < background.get_height():
        game.joueur.move_down()
        game.joueur.anime()
        game.sounds_manager.play('marche')

    if game.pressed.get(pygame.K_LEFT) and (game.pressed.get(pygame.K_UP) or game.pressed.get(pygame.K_DOWN)):
        game.joueur.animeg()
        
    if game.pressed.get(pygame.K_d):
        game.joueur.degat(15)

    if game.joueur.rect.y >= 240 and game.joueur.rect.y <= 330 and game.joueur.rect.x : # carre pont bas
        game.joueur.move_stop()

    # mettre à jour l'écran
    pygame.display.flip()

    #game.joueur.barre_de_vie()
    game.joueur.update()
    game.loup.update()
    game.camera.scroll()
    clock.tick(60)

    game.canvas.blit(background, (0 - game.camera.offset.x, 0 - game.camera.offset.y))
    game.canvas.blit(game.joueur.image, (game.joueur.rect.x - game.camera.offset.x, game.joueur.rect.y - game.camera.offset.y))
    game.window.blit(game.canvas, (0, 0))
    pygame.display.update()

    # si le joueur ferme la fenêtre
    for event in pygame.event.get():
        # évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # détecte si relache une touche
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton
            if play_button_rect.collidepoint(event.pos):
                # mettre le jeu en mode "lancé"
                game.is_playing = True
                # jouer le son
                #game.sounds_manager.play('')


    if game.joueur.rect.y > 195 and game.joueur.rect.y < 235 and game.joueur.rect.x >= 1160:
        print("Vous quittez : Village")
        time.sleep(2)
        print("Vous être dans : Cimetière")
        background = pygame.image.load('Assets/Cartes/map2.png')
        game.joueur.rect.x = 470
        game.joueur.rect.y = 595

    if game.joueur.rect.y > 120 and game.joueur.rect.y < 170 and game.joueur.rect.y <= 500:
        print("Vous quittez : Cimetière")
        time.sleep(2)
        print("Vous être dans : Sanctuaire")
        background = pygame.image.load('Assets/Cartes/map3.png')
        game.joueur.rect.x = 655
        game.joueur.rect.y = 220
