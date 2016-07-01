# -*- coding: utf-8 -*-
import os
import pygame
from entity import *
from pygame.locals import *
from constantes import *

class Banana(Entity):
	"""Classe définissant une banane
	"""

	step = 32

	def __init__(self): #constructeur de wall
		Entity.__init__(self)
		self.type = banana
		self.solid = False
		self.x = 0
		self.y = 0