# -*- coding: utf-8 -*-
import os
import pygame
from entities.banana import *
from entities.wall import *
from entities.empty import *
from entities.perso import *
from entities.start import *
from pygame.locals import *
from constantes import background, wall, banana, start

class Level():
	"""Classe définissant un niveau : on parcourt chaque ligne du fichier,
	et pour chaque caractère on pose un bloc : D pour départ, W pour wall, 
	0 pour chemin possible, B pour bananes. 
	"""
	step = 32
	def __init__(self, niveau): #constructeur d'exercice : numéro de niveau
		self.niveau = niveau
		fichier = "resources/level/level%s.txt" % self.niveau
		self.fichier = open(fichier, "r")
		self.map = []
		self.banane = Banana()
		lignes  = self.fichier.readlines()
		for x, line in enumerate(lignes):
			self.map.append([])
			for y, char in enumerate(line):
				if char == "W":
					self.map[x].append(Wall())
				elif char == "B":
					self.banane.x = y
					self.banane.y = x
					self.map[x].append(self.banane)
				elif char == "S":
					self.map[x].append(Start())
				else:
					self.map[x].append(Empty())



	def display_room(self, fenetre, perso):
		disp_fond = pygame.image.load(background).convert_alpha()
		fenetre.blit(disp_fond, (0,0))
		tup_entity = []
		for y, line in enumerate(self.map):
			for x, entity in enumerate(line):
				entity.display(fenetre, x, y)
		perso.display(fenetre, perso.x, perso.y)

		pygame.display.flip()
