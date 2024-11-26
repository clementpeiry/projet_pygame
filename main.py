print("Projet Pygame")

import pygame
from pygame.locals import *
from random import randint

pygame.init()
LARGEUR = 600
HAUTEUR = 600
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
clock = pygame.time.Clock()
continuer = True
bouger = True

perso = pygame.sprite.Sprite()
pygame.sprite.Sprite.__init__(perso)
perso.image = pygame.image.load("Blue_rectangle.png").convert_alpha()
perso.rect = perso.image.get_rect()
perso.rect.x = 50
perso.rect.y = 50
while bouger:
    perso.rect.x -=5
    if perso.rect.x == 0:
        perso.rect.x = 50

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