# -*- coding: utf-8 -*-
import os
import pygame
from entity import *
from pygame.locals import *
from constantes import *

class Empty(Entity):
	"""Classe définissant un mur
	"""

	step = 32

	def __init__(self): #constructeur de wall
		Entity.__init__(self)
		self.type = wall
		self.solid = False

	def display(self, fenetre, x, y):
		pass