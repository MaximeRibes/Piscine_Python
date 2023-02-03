import pygame
import pytmx
import pyscroll


from Monstre import Monstre
from Personnage import Personnage
from Pretre import Pretre
from Pnj import Pnj
from camera import *
from Sound import SoundManager
from Monstre import Monstre

# créer une seconde classe qui va représenter le jeu
class Game:
    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        # générer le joueur
        self.joueur = Pretre()

        #groupe de monstre
        self.all_Monstres = pygame.sprite.Group()
        self.personnage = Personnage()
        self.spawn_monstre()

    def spawn_monstre(self):
        monstre = Monstre()
        self.all_Monstres.add(monstre)

        #test map tmx
        # créer la fenetre de jeu
        #self.screen = pygame.display.set_mode((1619, 903))
        # charger la carte (tmx)
        #tmx_data = pytmx.util_pygame.load_pygame('Assets/Cartes/map1.tmx')
        #map_data = pyscroll.data.TiledMapData(tmx_data)
        #map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        # dessiner le groupe de calques
        #self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

        display_w, display_h = 550, 350
        self.canvas = pygame.Surface((display_w, display_h))
        self.window = pygame.display.set_mode(((display_w, display_h)))
        # gérer le son
        self.sounds_manager = SoundManager()
        self.camera = Camera(self.joueur)
        self.follow = Follow(self.camera, self.joueur)
        self.border = Border(self.camera, self.joueur)
        self.auto = Auto(self.camera, self.joueur)
        self.camera.setmethod(self.follow)



    def update(self, screen):
        # appliquer l'image du perso
        screen.blit(self.joueur.image, self.joueur.rect)

        villageois = Pnj(nom="Villageois", image=pygame.image.load('Assets\pnj\$villageois.png'))
        garde = Pnj(nom="Garde", image=pygame.image.load('Assets\pnj\$garde.png'))

        # appliquer l'image des pnj
        screen.blit(villageois.image, (475, 500))
        screen.blit(garde.image, (950, 240))

        # si le joueur appuie sur une touche
        #if self.pressed.get(pygame.K_RIGHT):
        #    self.joueur.move_right()
        #elif self.pressed.get(pygame.K_LEFT):
        #    self.joueur.move_left()
        #elif self.pressed.get(pygame.K_UP):
        #    self.joueur.move_up()
        #elif self.pressed.get(pygame.K_DOWN):
        #    self.joueur.move_down()
