from constantes import cote_fenetre, titre_fenetre, image_icone
import pygame
from level_new import *
from menu import *
from entities import *
from pygame.locals import *

labyrinthe = Level_new(4);

for cell in labyrinthe.visit_cells():
	print ('cellule en X : {}, Y :{} ; mur du haut : {}, mur du bas : {}, mur de gauche : {} mur de droite : {}'.format(cell.x_pos, cell.y_pos, cell.wall_up, cell.wall_down, cell.wall_left, cell.wall_right))



