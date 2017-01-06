# -*- coding: utf-8 -*-
import os
import pygame
from entities.entity import *
from pygame.locals import *
from constantes import *

class Banana(Entity):
	"""Classe définissant une banane
	"""

	step = 32

	def __init__(self, level, cell): #constructeur de wall
		Entity.__init__(self)
		self.type = banana
		self.solid = False
		self.level = level
		self.cell = cell
		self.x = 0
		self.y = 0

	def display(self, fenetre):
		disp = pygame.image.load(self.type).convert_alpha()
		fenetre.blit(disp, (self.cell.x_pos*32, self.cell.y_pos*32))