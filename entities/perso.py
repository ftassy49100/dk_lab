# -*- coding: utf-8 -*-
import os
from entity import *
import pygame
from pygame.locals import *
from constantes import *

class Perso(Entity):
	"""Classe définissant un perso
	"""

	step = 32

	def __init__(self, level): #constructeur de perso
		Entity.__init__(self)
		self.level = level
		self.type = perso
		self.x = 1
		self.y = 1

	def move(self, direction):
		if direction == "up":
			if not self.level.map[self.y-1][self.x].solid:
				self.y -=1
				self.type = dk_up
		elif direction == "down":
			if not self.level.map[self.y+1][self.x].solid:
				self.y +=1
				self.type = dk_down
		elif direction == "left":
			if not self.level.map[self.y][self.x -1].solid:
				self.x -=1
				self.type = dk_left
		elif direction == "right":
			if not self.level.map[self.y][self.x +1].solid:
				self.x +=1
				self.type = dk_right