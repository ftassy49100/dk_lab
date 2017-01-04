# -*- coding: utf-8 -*-
import os
import pygame
from entities.entity import *
from pygame.locals import *
from constantes import *

class Cell(Entity):
	"""Classe définissant une banane
	"""

	step = 32

	def __init__(self, x_pos, y_pos): #constructeur de wall
		Entity.__init__(self)
		self.solid = False
		self.wall_up = True
		self.wall_down = True
		self.wall_left = True
		self.wall_right = True
		self.visited = False
		self.x_pos = x_pos
		self.y_pos = y_pos


	def remove_wall(self, direction, opposite_cell):
		if direction == 'up':
			self.wall_up = False
			opposite_cell.wall_down = False
		elif direction == 'down':
			self.wall_down = False
			opposite_cell.wall_up = False
		elif direction == 'left':
			self.wall_left = False
			opposite_cell.wall_right = False
		elif direction == 'right':
			self.wall_right = False
			opposite_cell.wall_left = False
		return self


