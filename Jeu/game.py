import pygame


from camera import *
from player import Player
from monster import Monster
from Sound import SoundManager
from Boss_final import *

# jeu
class Game:

    def __init__(self):
        # générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.all_Boss = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()
        self.spawn_monster()
        self.spawn_Boss()
        self.camera = Camera(self.player)
        self.follow = Follow(self.camera, self.player)
        self.border = Border(self.camera, self.player)
        self.auto = Auto(self.camera, self.player)
        self.camera.setmethod(self.follow)

        #display_w, display_h = 550, 350
        #self.canvas = pygame.Surface((display_w, display_h))
        #self.window = pygame.display.set_mode(((display_w, display_h)))

        self.camera = Camera(self.player)
        self.follow = Follow(self.camera, self.player)
        self.border = Border(self.camera, self.player)
        self.auto = Auto(self.camera, self.player)
        self.camera.setmethod(self.follow)

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

        # gérer le son
        self.sounds_manager = SoundManager()

    def spawn_Boss(self):
        Boss_final = Boss(self)
        self.all_Boss.add(Boss_final)

