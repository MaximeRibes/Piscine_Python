import pygame

from projectile import Projectile
# Création classe joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('Assets\Hero\Pretre\marcher/Hobbit - run1.png')
        self.image = pygame.transform.scale(self.image, (125, 125))
        self.image_g = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 600
        self.current_image = 0
        self.animation = True
        self.images = animations.get('Hobbit - run')
        self.imagesg = animationsg.get('Hobbit - run')

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

    def update_health_bar(self, surface):
        # dessiner barre de vie
        pygame.draw.rect(surface, (60, 60, 60), [self.rect.x + 10, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (0,0,255), [self.rect.x + 10, self.rect.y +20, self.health, 5])

    def launch_projectile(self):
        # créer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

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
    'Hobbit - run': marcher()
}

animationsg = {
    'Hobbit - run': marcherg()
}