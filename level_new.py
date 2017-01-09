# -*- coding: utf-8 -*-
import os
import pygame
from entities.banana import *
from entities.perso import *
from entities.start import *
from entities.cell import *
from pygame.locals import *
from random import *
from constantes import background, wall, banana, start
import time

class Level_new():
	"""Classe définissant un Labyrinthe généré automatiquement
	grâce à l'algorithme du recursive backtracking. 
	"""
	step = 32
	def __init__(self, size): #constructeur d'exercice : numéro de niveau
		self.tuple_level = []
		self.size = size
		y = 0
		while (y < self.size):
			x=0
			while (x < self.size):
				self.tuple_level.append(Cell(x,y))
				x = x + 1
			y = y + 1

	def go_in_cell_arround(self, current_cell, cells_around):
		new_cells_around = []
		for cell in cells_around:
			if cell.visited == False:
				new_cells_around.append(cell)
		if new_cells_around:
			next_cell = choice(new_cells_around)
			if (next_cell.x_pos == current_cell.x_pos + 1):
				current_cell.remove_wall('right', next_cell) #on pète les murs de gauche de la cellule + celui de droite de la prochaine
			elif (next_cell.x_pos == current_cell.x_pos -1):
				current_cell.remove_wall('left', next_cell) # idem
			elif (next_cell.y_pos == current_cell.y_pos +1):
				current_cell.remove_wall('down', next_cell) # idem bas et haut
			else:
				current_cell.remove_wall('up', next_cell) # idem haut et bas

			next_cell.visited = True # on s'assure que la prochaine cellule soit marquée visitée
			return next_cell
		return current_cell
	def visit_cells(self):
		
		starting_cell = choice(self.tuple_level)#choice(self.tuple_level) # on choisit une cell pour commencer le laby
		starting_cell.visited = True # on la rend visitée
		path_visited = [starting_cell]
		current_cell = starting_cell
		current_index = self.tuple_level.index(current_cell)
		while path_visited: # tant qu'on n'est pas revenu au point de départ
			cells_around = []
			if (current_cell.x_pos == 0 and current_cell.y_pos == 0): # pour en haut à gauche,  cases à côté = en à droite et en dessous
				cells_around = [self.tuple_level[current_index +1], self.tuple_level[current_index + self.size]]
			elif (current_cell.x_pos == self.size -1 and current_cell.y_pos == self.size -1): # pour en bas à droite, à gauche et en haut
				cells_around = [self.tuple_level[current_index - 1], self.tuple_level[current_index -self.size]]
			elif (current_cell.x_pos == 0 and current_cell.y_pos == self.size -1): # pour en bas à gauche
				cells_around = [self.tuple_level[current_index + 1], self.tuple_level[current_index - self.size]]
			elif (current_cell.y_pos == 0 and current_cell.x_pos == self.size -1): # pour en haut à droite
				cells_around = [self.tuple_level[current_index -1], self.tuple_level[current_index +self.size]]
			elif (current_cell.x_pos == 0): # pour les murs de gauche
				cells_around = [self.tuple_level[current_index +1], self.tuple_level[current_index + self.size], self.tuple_level[current_index - self.size]]
			elif (current_cell.x_pos == self.size -1): # pour les murs de droite
				cells_around = [self.tuple_level[current_index -1], self.tuple_level[current_index + self.size], self.tuple_level[current_index - self.size]]
			elif (current_cell.y_pos == 0): # pour les murs d'en haut
				cells_around = [self.tuple_level[current_index -1], self.tuple_level[current_index + 1], self.tuple_level[current_index + self.size]]
			elif (current_cell.y_pos == self.size -1): # pour les murs d'en bas
				cells_around = [self.tuple_level[current_index -1], self.tuple_level[current_index + 1], self.tuple_level[current_index - self.size]]
			else:
				cells_around = [self.tuple_level[current_index -1], self.tuple_level[current_index +1], self.tuple_level[current_index + self.size], self.tuple_level[current_index - self.size]]
			next_cell = self.go_in_cell_arround(current_cell, cells_around) # on se déplace jusqu'à la prochaine cell qui devient la cell courante
			next_index = self.tuple_level.index(next_cell)  #on modifie l'index de la cell courante
			if path_visited[-1] == next_cell: # Si on est resté sur la même cell (pas de cells autour)
				path_visited.pop() # On supprime cette cell du chemin
				if path_visited:
					current_cell = path_visited[-1] # on prend la précédente cell en tant que cell courante
					current_index = self.tuple_level.index(current_cell) #on modifie l'index
			else: #si on a bien changé de cell
				current_cell = next_cell #on prend la prochaine cell en tant que cell courante
				current_index = next_index #et on modifie l'index
				path_visited.append(current_cell)
		return self.tuple_level

	def display_room(self, fenetre):
		disp_fond = pygame.image.load(background).convert_alpha()
		fenetre.blit(disp_fond, (0,0))
		for cell in self.tuple_level:
			cell.display_walls(fenetre, cell.x_pos, cell.y_pos)
			pygame.display.flip()
	def cells_around(self, cell):
		_cells_around = [cell, cell, cell, cell]
		if not cell.wall_up:
			_cells_around[0] = (self.tuple_level[self.tuple_level.index(cell) - self.size])
		if not cell.wall_down:
			_cells_around[1] = (self.tuple_level[self.tuple_level.index(cell) + self.size])
		if not cell.wall_left:
			_cells_around[2] = (self.tuple_level[self.tuple_level.index(cell) - 1])
		if not cell.wall_right:
			_cells_around[3] = (self.tuple_level[self.tuple_level.index(cell) + 1])
		return _cells_around
