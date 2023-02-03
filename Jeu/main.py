import pygame
import pytmx
import pyscroll
import math
pygame.init()


from game import *
from player import Player
from player import *
from camera import *
from Pnj import *
from Sound import *
from Boss_final import *
import time





# générer la fenetre de jeu
pygame.display.set_caption("Peace in Python")
screen = pygame.display.set_mode((1619, 903))



# importer charger l'arrière plan
background = pygame.image.load('Assets/Cartes/map1.png')

# charger jeu
game = Game()

clock = pygame.time.Clock()

# charger notre joueur
player = Player(game)

running = True

# boucle tant que cette condition est vrai
while running:

    #appliquer arrière plan du jeu
    screen.blit(background, (0,0))

    villageois = Pnj(nom="Villageois", image=pygame.image.load('Assets\pnj\$villageois.png'))
    garde = Pnj(nom="Garde", image=pygame.image.load('Assets\pnj\$garde.png'))
    # appliquer l'image des pnj
    screen.blit(villageois.image, (475, 500))
    screen.blit(garde.image, (950, 240))

    # appliquer image du joueur
    screen.blit(game.player.image, game.player.rect)

    # actualiser la barre de vie du joueur
    game.player.update_health_bar(screen)

    #récupérer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    # appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    # récupérer les monstres du jeu
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # appliquer l'ensemble des images de mon groupe de monstre
    game.all_monsters.draw(screen)

    # récupérer le boss du jeu
    #for Boss_final in game.all_Boss:
     #   Boss_final.forward()
      #  Boss_final.update_health_bar(screen)



    # vérifier si le joueur souhaite aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
        game.player.anime()
        game.sounds_manager.play('marche')
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()
        game.player.animeg()
        game.sounds_manager.play('marche')
    elif game.pressed.get(pygame.K_UP) and game.player.rect.y > 0:
        game.player.move_up()
        game.player.anime()
        game.sounds_manager.play('marche')
    elif game.pressed.get(pygame.K_DOWN) and game.player.rect.y + game.player.rect.height < background.get_height():
        game.player.move_down()
        game.player.anime()
        game.sounds_manager.play('marche')

        if game.pressed.get(pygame.K_LEFT) and (game.pressed.get(pygame.K_UP) or game.pressed.get(pygame.K_DOWN)):
            game.player.animeg()

        if game.pressed.get(pygame.K_d):
            game.player.degat(15)

        if game.player.rect.y >= 240 and game.player.rect.y <= 330 and game.player.rect.x:  # carre pont bas
            game.player.move_stop()

    # mettre à jour l'écran
    pygame.display.flip()

    #game.canvas.blit(background, (0 - game.camera.offset.x, 0 - game.camera.offset.y))
    #game.canvas.blit(game.player.image,(game.player.rect.x - game.camera.offset.x, game.player.rect.y - game.camera.offset.y))
    #game.window.blit(game.canvas, (0, 0))

    pygame.display.update()

    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # vérifier l'évènement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        # détecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est enclanchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    if game.player.rect.y > 195 and game.player.rect.y < 235 and game.player.rect.x >= 1160:
        print("Vous quittez : Village")
        time.sleep(2)
        print("Vous être dans : Cimetière")
        background = pygame.image.load('Assets/Cartes/map2.png')
        screen = pygame.display.set_mode((1619, 903))
        game.player.rect.x = 470
        game.player.rect.y = 595

    if game.player.rect.y > 120 and game.player.rect.y < 170 and game.player.rect.y <= 500:
        print("Vous quittez : Cimetière")
        time.sleep(2)
        print("Vous êtes dans : Sanctuaire")
        background = pygame.image.load('Assets/Cartes/map3.png')
        screen = pygame.display.set_mode((1619, 903))
        game.player.rect.x = 600
        game.player.rect.y = 300
        # appliquer l'ensemble des images de mon groupe de Boss
        #game.all_Boss.draw(screen)