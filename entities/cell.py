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
		self.type = banana
		self.solid = False
		self.wall_up = True
		self.wall_down = True
		self.wall_left = True
		self.wall_right = True
		sself.visited = False