"""Jeu DK labyrinthe, espèce de pacman like 
sans aucun fun, pas de fantôme ni de bouboules ..."""

from constantes import cote_fenetre, titre_fenetre, image_icone
import pygame
from level import *
from menu import *
from entities import *
from pygame.locals import *
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

pygame.display.flip()
pygame.display.set_caption(titre_fenetre)

icone = pygame.image.load(image_icone).convert_alpha()
goal = 0
continuer = 1
win = 0
disp_menu=0
menu = Menu()
level = Level(1)
perso = Perso(level)
level.display_room(fenetre, perso)
	
while continuer:
	if disp_menu == 0:
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					disp_menu = 1
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
	else:
		fenetre.fill(BLUE)
		menu.display(fenetre)
		stay = True
		while stay:
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer = 0
					stay = False
				elif event.type == KEYDOWN:
					if event.key == K_ESCAPE:
						disp_menu = 0
						stay = False
						win = 0
					elif event.key == K_F1:
						level = Level(1)
						perso = Perso(level)
						disp_menu = 0
						win = 0
						stay = False
					elif event.key == K_F2:
						level = Level(2)
						perso = Perso(level)
						disp_menu = 0
						stay = False
						win = 0
		level.display_room(fenetre, perso)

