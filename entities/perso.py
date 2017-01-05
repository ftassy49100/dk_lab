# -*- coding: utf-8 -*-
import os
from entities.entity import *
import pygame
from pygame.locals import *
from constantes import *

class Perso(Entity):
	"""Classe définissant un perso
	"""

	step = 32

	def __init__(self, level, cell): #constructeur de perso
		Entity.__init__(self)
		self.level = level
		self.type = dk_down
		self.cell = cell

	def move(self, direction):
		if direction == "up":
			if not self.cell.wall_up:
				self.cell = self.level.cells_around(self.cell)[0]
				self.type = dk_up
		elif direction == "down":
			if not self.cell.wall_down:
				self.cell = self.level.cells_around(self.cell)[1]
				self.type = dk_down
		elif direction == "left":
			if not self.cell.wall_left:
				self.cell = self.level.cells_around(self.cell)[2]
				self.type = dk_left
		elif direction == "right":
			if not self.cell.wall_right:
				self.cell = self.level.cells_around(self.cell)[3]
				self.type = dk_right
		print ('perso maintenant en {}, {}'.format(self.cell.x_pos, self.cell.y_pos))

	def display(self, fenetre):
		disp = pygame.image.load(self.type).convert_alpha()
		fenetre.blit(disp, (self.cell.x_pos*32, self.cell.y_pos*32))
