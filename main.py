print("Projet Pygame")

import pygame

class Dinosaure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Diplodocus_personnage.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
    def sauter(self):
        if self.rect.y == 400:
            self.vitesse == 0
        else:
            self.vitesse -= 9.81
    def se_baisser(self):
        pass

class Objet:
    pass
    def __init__(self):
        pass

class Obstacle:
    pass
    def __init__(self, vitesse_obstacle):
        self.vitesse_obstacle = vitesse_obstacle

class Obstacle_sol(Obstacle):
    pass

fenetre = pygame.display.set_mode((640, 480))


fond1 = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(fond1)
fond1.image = pygame.image.load("Fondpygame.jpg").convert_alpha()
fond1.rect = fond1.image.get_rect()
fond1.rect.x = 0
fond1.rect.y = 0
continuer = True

fond2 = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(fond2)
fond2.image = pygame.image.load("Fondpygame.jpg").convert_alpha()
fond2.rect = fond2.image.get_rect()
fond2.rect.x = 1022
fond2.rect.y = 0

liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(fond1)
liste_des_sprites.add(fond2)
direction = "droite"
clock = pygame.time.Clock()
while continuer:
    liste_des_sprites.draw(fenetre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    fond1.rect.x -= 2
    fond2.rect.x -= 2
    if fond1.rect.x == -1022:
        fond1.rect.x = 1022
    if fond2.rect.x == -1022:
        fond2.rect.x = 1022
    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()