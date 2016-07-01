# -*- coding: utf-8 -*-
import os
import pygame

class Entity():
	"""Classe définissant une entité : utile pour définir le display et la solidité ou non de l'élément. 
	"""
	step = 32
	def __init__(self): #constructeur d'exercice : numéro de niveau
		self.solid = True

	def display(self, fenetre, x, y):
		disp = pygame.image.load(self.type).convert_alpha()
		fenetre.blit(disp, (x * 32, y * 32))
