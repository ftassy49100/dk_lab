# -*- coding: utf-8 -*-
import os
import pygame
from entities.banana import *
from entities.wall import *
from entities.empty import *
from entities.perso import *
from entities.start import *
from entities.ennemy import *
from entities.cell import *
from pygame.locals import *
from random import *
from constantes import background, wall, banana, start

class Level():
	"""Classe définissant un niveau : on parcourt chaque ligne du fichier,
	et pour chaque caractère on pose un bloc : D pour départ, W pour wall, 
	0 pour chemin possible, B pour bananes. 
	"""
	step = 32
	def __init__(self, size, nb_ennemies): #constructeur d'exercice : numéro de niveau
		self.tuple_level = []
		x = 0
		y = 0
		while (y < self.size):
			while (x < self.size):
				tuple_level.append(cell(x,y))
				x = x + 1
			y = y + 1

		for cell in tuple_level:

			if (cell.x == 0):
				cell.wall_left = True
			elif (cell_x == size):
				cell.wall_right = True
			if (cell.y == 0):
				cell.wall_up = True
			elif (cell.y == size):
				cell.wall_down = True


	def visit_cells():
		cells_around = []
		starting_cell = choice(self.tuple_level)
		index_start = self.tuple_level.index(starting_cell)
		path_visited = [starting_cell] # on choisit une cellule pour commencer le laby


		if (cell.x == 0 and cell.y == 0): # pour en haut à gauche,  cases à côté = en à droite et en dessous
			cells_around = [self.tuple_level[index_start +1], self.tuple_level[index_start + size]]
		elif (cell_x == size and cell.y == size): # pour en bas à droite, à gauche et en haut
			cells_around = [self.tuple_level[index_start - 1], self.tuple_level[index_start -size]]
		elif (cell.x == 0 and cell.y == size):
			cells_around == [self.tuple_level[index_start + 1], self.tuple_level[index_start -size]]
		elif (cell.y == 0 and cell.x == size):
			cells_around = [self.tuple_level[index_start -1], self.tuple_level[index_start +size]]
		elif (cell.x == 0):
			cells_around = [self.tuple_level[index_start +1], self.tuple_level[index_start + size], self.tuple_level[index_start - size]]
		elif (cell.x == size):
			cells_around = [self.tuple_level[index_start -1], self.tuple_level[index_start + size], self.tuple_level[index_start - size]]
		elif (cell.y == 0):
			cells_around = [self.tuple_level[index_start -1], self.tuple_level[index_start + 1], self.tuple_level[index_start + size]]
		elif (cell.y == size):
			cells_around = [self.tuple_level[index_start -1], self.tuple_level[index_start + 1], self.tuple_level[index_start - size]]
		else:
			cells_around = [self.tuple_level[index_start -1], self.tuple_level[index_start +1], self.tuple_level[index_start + size], self.tuple_level[index_start - size]]
	def display_room(self, fenetre, perso, ennemy):
		
