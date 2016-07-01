# -*- coding: utf-8 -*-
import os
from entities import *
import pygame
from pygame.locals import *
from constantes import *
import string

class Menu():
	"""Classe définissant le menu
	"""


	def __init__(self): #constructeur de perso
		self.level_tuple = []
		for fichier in os.listdir('resources/level/'):
			name = fichier.split('.')
			self.level_tuple.append(name[0])
		self.font = pygame.font.SysFont('Arial', 25)


	def display(self, fenetre):
		for x, level in enumerate(self.level_tuple):
			fenetre.blit(self.font.render(level, True, (255,0,0)), (200, 50*x))
			pygame.display.update()