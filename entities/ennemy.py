# -*- coding: utf-8 -*-
import os
from entities.entity import *
import pygame
from pygame.locals import *
from constantes import *
from random import *
from entities.perso import *

class Ennemy(Perso):
	"""Classe définissant un perso
	"""
	
	step = 32

	def __init__(self, level): #constructeur de perso
		Entity.__init__(self)
		self.level = level
		self.type = ennemy
		self.x = -1
		self.y = -1

	def move(self, direction):
		if direction == "up":
			if not self.level.map[self.y-1][self.x].solid and \
			not ((self.level.perso.x == self.x) and (self.level.perso.y == self.y-1)):
				self.y -=1
		elif direction == "down":
			if not self.level.map[self.y+1][self.x].solid and \
			not ((self.level.perso.x == self.x) and (self.level.perso.y == self.y+1)):
				self.y +=1
		elif direction == "left":
			if not self.level.map[self.y][self.x -1].solid and \
			not ((self.level.perso.x == self.x -1) and (self.level.perso.y == self.y)):
				self.x -=1
		elif direction == "right":
			if not self.level.map[self.y][self.x +1].solid and \
			not ((self.level.perso.x == self.x +1) and (self.level.perso.y == self.y)):
				self.x +=1