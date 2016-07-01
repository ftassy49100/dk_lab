"""Jeu DK labyrinthe, espèce de pacman like 
sans aucun fun, pas de fantôme ni de bouboules ..."""

from constantes import cote_fenetre, titre_fenetre, image_icone
import pygame
from level import *
from perso import *
from pygame.locals import *
pygame.init()

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.flip()
pygame.display.set_caption(titre_fenetre)

icone = pygame.image.load(image_icone).convert_alpha()
menu = 1
goal = 0
continuer = 1
win = 0

level = Level(1)
perso = Perso(level)
print (level.map[1])
level.display_room(fenetre, perso)
while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0
		elif event.type == KEYDOWN:
			if event.key == K_DOWN:
				perso.move("down")
			if event.key == K_UP:
				perso.move("up")
			if event.key == K_LEFT:
				perso.move("left")
			if event.key == K_RIGHT:
				perso.move("right")
			level.display_room(fenetre, perso)
	if (perso.x == level.banane.x) and (perso.y == level.banane.y):
		win = 1

	if win:
		win_img = pygame.image.load(dk_win).convert_alpha()
		fenetre.blit(win_img, (79, 79))
		pygame.display.flip()