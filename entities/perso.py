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

	def __init__(self, level): #constructeur de perso
		Entity.__init__(self)
		self.level = level
		self.type = perso
		self.x = -1
		self.y = -1

	def move(self, direction):
		if direction == "up":
			if not self.level.map[self.y-1][self.x].solid and \
			not ((self.level.ennemy.x == self.x) and (self.level.ennemy.y == self.y-1)) and \
			not ((self.level.ennemy.x == self.x) and (self.level.ennemy.y+1 == self.y-1)):
				self.y -=1
				self.type = dk_up
		elif direction == "down":
			if not self.level.map[self.y+1][self.x].solid and \
			not ((self.level.ennemy.x == self.x) and (self.level.ennemy.y == self.y+1)) and \
			not ((self.level.ennemy.x == self.x) and (self.level.ennemy.y-1 == self.y+1)):
				self.y +=1
				self.type = dk_down
		elif direction == "left":
			if not self.level.map[self.y][self.x -1].solid and \
			not ((self.level.ennemy.x == self.x-1) and (self.level.ennemy.y == self.y)) and \
			not ((self.level.ennemy.x+1 == self.x-1) and (self.level.ennemy.y == self.y)):
				self.x -=1
				self.type = dk_left
		elif direction == "right":
			if not self.level.map[self.y][self.x +1].solid and \
			not ((self.level.ennemy.x == self.x+1) and (self.level.ennemy.y == self.y)) and \
			not ((self.level.ennemy.x-1 == self.x+1) and (self.level.ennemy.y == self.y)):
				self.x +=1
				self.type = dk_right