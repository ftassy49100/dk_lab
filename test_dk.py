from constantes import *
import pygame
from level_new import *
from menu import *
from entities import *
from pygame.locals import *
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
level = Level_new(16)
perso = Perso(level, choice(level.tuple_level))
fenetre = pygame.display.set_mode(((level.size) * 32, (level.size)*32))

pygame.display.flip()
pygame.display.set_caption(titre_fenetre)

icone = pygame.image.load(image_icone).convert_alpha()
goal = 0
continuer = 1
win = 0
disp_menu=0
menu = Menu()
level.visit_cells()
level.display_room(fenetre)
perso.display(fenetre)
print ('perso en {}, {}'.format(perso.cell.x_pos, perso.cell.y_pos))
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
			level.display_room(fenetre)
			perso.display(fenetre)
			pygame.display.flip()		
		if win:
			win_img = pygame.image.load(dk_win).convert_alpha()
			fenetre.blit(win_img, (79, 79))
			pygame.display.flip()
