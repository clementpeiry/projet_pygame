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
    def sauter(self):
        if perso.rect.y = sol.rect.y:
            vitesse == 0
        else:
            vitesse -= 9.81
    def se_baisser(self):

class Objet:
    def __init__(self):

class Obstacle:
    def __init__(self, vitesse_obstacle):
        self.vitesse_obstacle = vitesse_obstacle

class Obstacle_sol(Obstacle):


pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
continuer = True

perso = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(perso)
perso.image = pygame.image.load("Diplodocus_personnage.png").convert_alpha()
perso.rect = perso.image.get_rect()
perso.rect.x = 50
perso.rect.y = 50

liste_des_sprites = pygame.sprite.LayeredUpdates()
liste_des_sprites.add(perso)

direction = "droite"

while continuer:
    liste_des_sprites.draw(fenetre)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    fenetre.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()