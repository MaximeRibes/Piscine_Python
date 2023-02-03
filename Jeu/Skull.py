import pygame
import random


# classe monstre du jeu
class Skull(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 50
        self.max_health = 70
        self.attack = 1
        self.image = pygame.image.load("Assets/Mechants/Loup/Loup2.png")
        self.rect = self.image.get_rect()
        self.rect.x = 750 + random.randint(0, 300)
        self.rect.y = 245
        self.velocity = 1

    def damage(self, amount):
        # infliger des dégats
        self.health -= amount

        # vérifier si ses pv inférieur ou égal à 0
        if self.health <=0:
            # réapparaitre
            self.rect.x = 1000 + random.randint(0, 300)
            self.health = self.max_health

    def update_health_bar(self, surface):
        # dessiner barre de vie
        pygame.draw.rect(surface, (60,60,60), [self.rect.x, self.rect.y, self.max_health - 25, 5])
        pygame.draw.rect(surface, (255,0,0), [self.rect.x, self.rect.y, self.health - 25, 5])


    def forward(self):
        # le déplacement ne se fait que s'il n'y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else :
            # infliger des dégats au joueur
            self.game.player.damage(self.attack)


