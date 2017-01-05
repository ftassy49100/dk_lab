from constantes import *
import pygame
from level_new import *
from menu import *
from entities import *
from pygame.locals import *
pygame.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
level = Level_new(10)

fenetre = pygame.display.set_mode(((level.size) * 32, (level.size)*32))

pygame.display.flip()
pygame.display.set_caption(titre_fenetre)

icone = pygame.image.load(image_icone).convert_alpha()
goal = 0
continuer = 1
win = 0
disp_menu=0
menu = Menu()
level.visit_cells()
level.display_room(fenetre)
pygame.display.flip()

input('quit')