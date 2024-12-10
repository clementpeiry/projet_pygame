print("Projet Pygame")

import pygame
from pygame.locals import *
from random import *

class Dinosaure(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Diplodocus_personnage.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vitesse = 5
    def update(self):
        if self.vitesse < 5:
            self.vitesse += 0.1
        if self.rect.y == 400:
            self.vitesse = 0
    def sauter(self):
        self.vitesse = -10

class Obstacle:
    def __init__(self, vitesse_obstacle):
        self.vitesse_obstacle = vitesse_obstacle

class Obstacle_sol(Obstacle):
    pass

perso = Dinosaure()

pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
continuer = True
bouger = True

fond1 = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(fond1)
fond1.image = pygame.image.load("Blue_rectangle.png").convert_alpha()
fond1.rect = fond1.image.get_rect()
fond1.rect.x = 50
fond1.rect.y = 50

liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(fond1)
liste_des_sprites.add(perso)

direction = "droite"

while continuer:
    liste_des_sprites.draw(fenetre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
    fond1.rect.x -=5
    if fond1.rect.x == 0:
        fond1.rect.x = 50
    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()