# -*- coding: utf-8 -*-
import os
import pygame
from entities.entity import *
from pygame.locals import *
from constantes import *

class Start(Entity):
	"""Classe définissant un départ
	"""

	step = 32

	def __init__(self): #constructeur de wall
		Entity.__init__(self)
		self.type = start
		self.solid = False