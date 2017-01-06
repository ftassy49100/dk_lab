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
level = Level_new(9)
perso = Perso(level, choice(level.tuple_level))
fenetre = pygame.display.set_mode(((level.size) * 32, (level.size)*32))
banana = Banana(level, choice(level.tuple_level))
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
banana.display(fenetre)
perso.display(fenetre)
print ('perso en {}, {}'.format(perso.cell.x_pos, perso.cell.y_pos))
pygame.display.flip()
while continuer:
	if perso.cell.x_pos == banana.cell.x_pos and perso.cell.y_pos == banana.cell.y_pos:
		win = True
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
				banana.display(fenetre)
				pygame.display.flip()		
		if win:
			win_img = pygame.image.load(dk_win).convert_alpha()
			fenetre.blit(win_img, (79, 79))
			pygame.display.flip()
