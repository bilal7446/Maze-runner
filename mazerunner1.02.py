 # Imports

import pygame
import random
import json
from pygame import *
import socket
from _thread import *
import _pickle as pickle
from copy import copy
from pprint import pprint
from tkinter import *

import struct
import sys
from _thread import *
from tkinter import *

# Screen Dimensions

WIN_WIDTH = int(786 * 1.5)
WIN_HEIGHT = int(600 * 1.1)
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

# Screen Defaults

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

# Init, Create Screen

pygame.init()
screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)

##############Drawing Code##############

# sprites of gunner

spritesheet = pygame.image.load('Media/Graphics/gunner.png')

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-1, -3889))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
character = pygame.transform.flip(character, True, False)
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
standleft = stage

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-167, -3887))
character = pygame.transform.flip(character, True, False)
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (0, 0))
blinkleft = stage

standloopleft2 = [standleft, blinkleft]

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-1, -3889))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
standright = stage

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-167, -3887))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
blinkright = stage

standloopright2 = [standright, blinkright]
standloopleft2 = [pygame.transform.flip(standright, True, False),
				  pygame.transform.flip(blinkright, True, False)]

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-20, -4123))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
stepright = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-2, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright1 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 200, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright2 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 390, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright3 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 587, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright4 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 782, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright5 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 979, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright6 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 1173, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright7 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 1367, -4125))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright8 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-2, -4328))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright9 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 200, -4328))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright10 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 390, -4328))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright11 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 587, -4328))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright12 = stage

walkloopright2 = [
	stepright,
	runright1,
	runright2,
	runright3,
	runright4,
	runright5,
	runright6,
	runright7,
	runright8,
	runright9,
	runright10,
	runright11,
	runright12,
	]

walkloopleft2 = [
	pygame.transform.flip(walkloopright2[0], True, False),
	pygame.transform.flip(walkloopright2[1], True, False),
	pygame.transform.flip(walkloopright2[2], True, False),
	pygame.transform.flip(walkloopright2[3], True, False),
	pygame.transform.flip(walkloopright2[4], True, False),
	pygame.transform.flip(walkloopright2[5], True, False),
	pygame.transform.flip(walkloopright2[6], True, False),
	pygame.transform.flip(walkloopright2[7], True, False),
	pygame.transform.flip(walkloopright2[8], True, False),
	pygame.transform.flip(walkloopright2[9], True, False),
	pygame.transform.flip(walkloopright2[10], True, False),
	pygame.transform.flip(walkloopright2[11], True, False),
	pygame.transform.flip(walkloopright2[12], True, False),
	]

character = Surface((167, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-20, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
stepright = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-2, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright1 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 200, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright2 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 390, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright3 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 587, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright4 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 782, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright5 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 979, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright6 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 1173, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright7 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 1367, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright8 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-2, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright9 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 200, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright10 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 390, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright11 = stage

character = Surface((190, 204), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 587, -4555))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright12 = stage

character = Surface((149, 195), pygame.SRCALPHA)
character.blit(spritesheet, (-79, -639))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (108, 0))
shootrightstand2 = stage

shootrightstandloop2 = [srunright3]

character = Surface((29, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-206, -96))
character = pygame.transform.scale(character, (31 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
shootrightrun1 = stage

character = Surface((26, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-239, -96))
character = pygame.transform.scale(character, (31 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
shootrightrun2 = stage

character = Surface((30, 24), pygame.SRCALPHA)
character.blit(spritesheet, (-268, -96))
character = pygame.transform.scale(character, (31 * 2, 35 * 24))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
shootrightrun3 = stage

shootrightrunloop2 = [
	srunright1,
	srunright1,
	srunright2,
	srunright3,
	srunright4,
	srunright5,
	srunright6,
	srunright7,
	srunright8,
	srunright9,
	srunright10,
	srunright11,
	srunright12,
	]

shootleftstandloop2 = [pygame.transform.flip(srunright1, True, False)]
shootleftrunloop2 = [
	pygame.transform.flip(shootrightrunloop2[0], True, False),
	pygame.transform.flip(shootrightrunloop2[1], True, False),
	pygame.transform.flip(shootrightrunloop2[2], True, False),
	pygame.transform.flip(shootrightrunloop2[3], True, False),
	pygame.transform.flip(shootrightrunloop2[4], True, False),
	pygame.transform.flip(shootrightrunloop2[5], True, False),
	pygame.transform.flip(shootrightrunloop2[6], True, False),
	pygame.transform.flip(shootrightrunloop2[7], True, False),
	pygame.transform.flip(shootrightrunloop2[8], True, False),
	pygame.transform.flip(shootrightrunloop2[9], True, False),
	pygame.transform.flip(shootrightrunloop2[10], True, False),
	pygame.transform.flip(shootrightrunloop2[11], True, False),
	pygame.transform.flip(shootrightrunloop2[12], True, False),
	]

shootleftstand2 = pygame.transform.flip(shootrightstand2, True, False)
character = Surface((128, 215), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 208, -2984))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunupright1 = stage

character = Surface((131, 201), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 467, -2984))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunupright2 = stage

character = Surface((122, 202), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 590, -2984))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunupright3 = stage

character = Surface((122, 202), pygame.SRCALPHA)
character.blit(spritesheet, (-1 - 785, -2984))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunupright4 = stage

shootuprightrunloop2 = [
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunupright1,
	srunright2,
	srunupright3,
	srunupright4,
	]

shootupleftrunloop2 = [
	pygame.transform.flip(shootuprightrunloop2[0], True, False),
	pygame.transform.flip(shootuprightrunloop2[1], True, False),
	pygame.transform.flip(shootuprightrunloop2[2], True, False),
	pygame.transform.flip(shootuprightrunloop2[3], True, False),
	pygame.transform.flip(shootuprightrunloop2[4], True, False),
	pygame.transform.flip(shootuprightrunloop2[5], True, False),
	pygame.transform.flip(shootuprightrunloop2[6], True, False),
	pygame.transform.flip(shootuprightrunloop2[7], True, False),
	pygame.transform.flip(shootuprightrunloop2[8], True, False),
	pygame.transform.flip(shootuprightrunloop2[9], True, False),
	pygame.transform.flip(shootuprightrunloop2[10], True, False),
	pygame.transform.flip(shootuprightrunloop2[11], True, False),
	pygame.transform.flip(shootuprightrunloop2[12], True, False),
	]

character = Surface((119, 215), pygame.SRCALPHA)
character.blit(spritesheet, (-33, -9116))
character = pygame.transform.scale(character, (18 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
takedamageright2 = stage

takedamagerightair = takedamageright2

takedamageleft2 = pygame.transform.flip(takedamageright2, True, False)
takedamageleftair = pygame.transform.flip(takedamagerightair, True,
		False)

#heart to show health
heartpic = pygame.image.load('Media/Graphics/heart.png')
heartpic = pygame.transform.scale(heartpic, (50, 50))

# Load Sprite Oof gladiator Sheet

spritesheet = pygame.image.load('Media/Graphics/hero.png')

character = Surface((28, 52), pygame.SRCALPHA)
character.blit(spritesheet, (-68, -44))
character = pygame.transform.scale(character, (19 * 2, 35 * 2))
character = pygame.transform.flip(character, True, False)
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
standleft = stage

character = Surface((28, 52), pygame.SRCALPHA)
character.blit(spritesheet, (-68, -34))
character = pygame.transform.flip(character, True, False)
character = pygame.transform.scale(character, (19 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
blinkleft = stage

standloopleft = [standleft, blinkleft, standleft, blinkleft]

character = Surface((28, 52), pygame.SRCALPHA)
character.blit(spritesheet, (-68, -44))
character = pygame.transform.scale(character, (19 * 2, 35 * 2))

stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
standright = stage

character = Surface((28, 52), pygame.SRCALPHA)
character.blit(spritesheet, (-68, -34))

character = pygame.transform.scale(character, (19 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
blinkright = stage

standloopright = [standright, blinkright, standright, blinkleft]

character = Surface((28, 50), pygame.SRCALPHA)
character.blit(spritesheet, (-242, -271))
character = pygame.transform.scale(character, (19 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright2 = stage

character = Surface((28, 50), pygame.SRCALPHA)
character.blit(spritesheet, (-316, -271))
character = pygame.transform.scale(character, (19 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright4 = stage

character = Surface((39, 48), pygame.SRCALPHA)
character.blit(spritesheet, (-192, -274))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright1 = stage

character = Surface((39, 48), pygame.SRCALPHA)
character.blit(spritesheet, (-273, -274))
character = pygame.transform.scale(character, (30 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
runright3 = stage

walkloopright = [runright1, runright2, runright3, runright4]
walkloopleft = [pygame.transform.flip(walkloopright[0], True, False),
				pygame.transform.flip(walkloopright[1], True, False),
				pygame.transform.flip(walkloopright[2], True, False),
				pygame.transform.flip(walkloopright[3], True, False)]

character = Surface((57, 70), pygame.SRCALPHA)
character.blit(spritesheet, (-33, -506))
character = pygame.transform.scale(character, (32 * 2, 40 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, -10))
srunright1 = stage

character = Surface((87, 82), pygame.SRCALPHA)
character.blit(spritesheet, (-104, -506))
character = pygame.transform.scale(character, (66 * 2, 52 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright2 = stage

character = Surface((88, 30), pygame.SRCALPHA)
character.blit(spritesheet, (-195, -509))
character = pygame.transform.scale(character, (84 * 2, 45 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright3 = stage

character = Surface((50, 46), pygame.SRCALPHA)
character.blit(spritesheet, (-286, -533))
character = pygame.transform.scale(character, (36 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
srunright4 = stage

character = Surface((1, 1), pygame.SRCALPHA)
character.blit(spritesheet, (-1167, -163))
character = pygame.transform.scale(character, (25 * 4, 35 * 4))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
noimage = stage

shootrightstandloop = [srunright1, srunright2, srunright3, srunright4]

character = Surface((34, 74), pygame.SRCALPHA)
character.blit(spritesheet, (-404, -249))
character = pygame.transform.scale(character, (25 * 2, 50 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (135, -20))
shieldingright1 = stage

character = Surface((38, 74), pygame.SRCALPHA)
character.blit(spritesheet, (-488, -249))
character = pygame.transform.scale(character, (26 * 2, 50 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (135, -20))
shieldingright2 = stage

shieldingloop = [shieldingright1, shieldingright2, shieldingright1,
				 shieldingright2]

shieldingloop2 = [pygame.transform.flip(shieldingright1, True, False),
				  pygame.transform.flip(shieldingright2, True, False),
				  pygame.transform.flip(shieldingright1, True, False),
				  pygame.transform.flip(shieldingright2, True, False)]

shootleftstandloop = [pygame.transform.flip(srunright1, True, False),
					  pygame.transform.flip(srunright2, True, False),
					  pygame.transform.flip(srunright4, True, False),
					  pygame.transform.flip(srunright4, True, False)]

character = Surface((33, 75), pygame.SRCALPHA)
character.blit(spritesheet, (-235, -133))
character = pygame.transform.scale(character, (25 * 2, 45 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
takedamageright = stage

character = Surface((46, 44), pygame.SRCALPHA)
character.blit(spritesheet, (-130, -390))
character = pygame.transform.scale(character, (36 * 2, 35 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
shootarrowright = stage
shootarrowleft = pygame.transform.flip(shootarrowright, True, False)

takedamagerightair = takedamageright
takedamageleft = pygame.transform.flip(takedamageright, True, False)
takedamageleftair = pygame.transform.flip(takedamagerightair, True,
		False)

# Load zombie Shots Sprite Sheet

spritesheet = pygame.image.load('Media/Graphics/guu.png')

character = pygame.transform.scale(spritesheet, (30 * 2, 20 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (40, 0))
guu = stage

# load awwors of gladiator

spritesheet = pygame.image.load('Media/Graphics/arrow.png')

character = pygame.transform.scale(spritesheet, (40 * 2, 10 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (40, 0))
arrow1 = stage

spritesheet = pygame.image.load('Media/Graphics/arrow2.png')

character = pygame.transform.scale(spritesheet, (40 * 2, 10 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (40, 0))
arrow2 = stage

explodex = 68
explodey = -6

# loading zombies

s = pygame.image.load('Media/Graphics/Walk (1).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk1 = s

character = Surface((43, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-1565, -516))
character = pygame.transform.scale(character, (50 * 2, 22 * 2))
stage = Surface((300, 450), pygame.SRCALPHA)
stage.blit(character, (explodex, explodey))

s = pygame.image.load('Media/Graphics/Walk (2).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk2 = s
s = pygame.image.load('Media/Graphics/Walk (3).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk3 = s
s = pygame.image.load('Media/Graphics/Walk (4).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk4 = s
s = pygame.image.load('Media/Graphics/Walk (5).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk5 = s
s = pygame.image.load('Media/Graphics/Walk (6).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk6 = s
s = pygame.image.load('Media/Graphics/Walk (7).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk7 = s
s = pygame.image.load('Media/Graphics/Walk (8).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk8 = s
s = pygame.image.load('Media/Graphics/Walk (9).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk9 = s
s = pygame.image.load('Media/Graphics/Walk (10).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombiewalk10 = s

zombiewalkloop = [
	zombiewalk1,
	zombiewalk2,
	zombiewalk3,
	zombiewalk4,
	zombiewalk5,
	zombiewalk6,
	zombiewalk7,
	zombiewalk8,
	zombiewalk9,
	zombiewalk10,
	]

s = pygame.image.load('Media/Graphics/Gwalk (1).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk1 = s

character = Surface((43, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-1565, -516))
character = pygame.transform.scale(character, (50 * 2, 22 * 2))
stage = Surface((300, 450), pygame.SRCALPHA)
stage.blit(character, (explodex, explodey))

s = pygame.image.load('Media/Graphics/Gwalk (2).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk2 = s
s = pygame.image.load('Media/Graphics/Gwalk (3).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk3 = s
s = pygame.image.load('Media/Graphics/Gwalk (4).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk4 = s
s = pygame.image.load('Media/Graphics/Gwalk (5).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk5 = s
s = pygame.image.load('Media/Graphics/Gwalk (6).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk6 = s
s = pygame.image.load('Media/Graphics/Gwalk (7).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk7 = s
s = pygame.image.load('Media/Graphics/Gwalk (8).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk8 = s
s = pygame.image.load('Media/Graphics/Gwalk (9).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk9 = s
s = pygame.image.load('Media/Graphics/Gwalk (10).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieGirlwalk10 = s

zombieGirlwalkloop = [
	zombieGirlwalk1,
	zombieGirlwalk2,
	zombieGirlwalk3,
	zombieGirlwalk4,
	zombieGirlwalk5,
	zombieGirlwalk6,
	zombieGirlwalk7,
	zombieGirlwalk8,
	zombieGirlwalk9,
	zombieGirlwalk10,
	]

s = pygame.image.load('Media/Graphics/bwalk (1).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk1 = s

character = Surface((43, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-1565, -516))
character = pygame.transform.scale(character, (50 * 2, 22 * 2))
stage = Surface((300, 450), pygame.SRCALPHA)
stage.blit(character, (explodex, explodey))

s = pygame.image.load('Media/Graphics/bwalk (2).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk2 = s
s = pygame.image.load('Media/Graphics/bwalk (3).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk3 = s
s = pygame.image.load('Media/Graphics/bwalk (4).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk4 = s
s = pygame.image.load('Media/Graphics/bwalk (5).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk5 = s
s = pygame.image.load('Media/Graphics/bwalk (6).png')
s = pygame.transform.scale(s, (40 * 2, 47 * 2))
s = pygame.transform.flip(s, True, False)

zombieBosswalk6 = s

zombieBosswalkloop = [
	zombieBosswalk1,
	zombieBosswalk2,
	zombieBosswalk3,
	zombieBosswalk4,
	zombieBosswalk5,
	zombieBosswalk6,
	]

s = pygame.image.load('Media/Graphics/archer (1).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk1 = s

s = pygame.image.load('Media/Graphics/archer (2).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk2 = s
s = pygame.image.load('Media/Graphics/archer (3).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk3 = s
s = pygame.image.load('Media/Graphics/archer (4).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk4 = s
s = pygame.image.load('Media/Graphics/archer (5).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk5 = s
s = pygame.image.load('Media/Graphics/archer (6).png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArcherwalk6 = s

zombieArcherwalkloop = [
	zombieArcherwalk1,
	zombieArcherwalk2,
	zombieArcherwalk3,
	zombieArcherwalk4,
	zombieArcherwalk5,
	zombieArcherwalk6,
	]

# load zombieRunner zombie

s = pygame.image.load('Media/Graphics/rWalk (1).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk1 = s

s = pygame.image.load('Media/Graphics/rWalk (2).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk2 = s
s = pygame.image.load('Media/Graphics/rWalk (3).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk3 = s
s = pygame.image.load('Media/Graphics/rWalk (4).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk4 = s
s = pygame.image.load('Media/Graphics/rWalk (5).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk5 = s
s = pygame.image.load('Media/Graphics/rWalk (6).png')
s = pygame.transform.scale(s, (30 * 2, 35 * 2))
s = pygame.transform.flip(s, True, False)

zombieRunnerwalk6 = s

zombieRunnerwalkloop = [
	zombieRunnerwalk1,
	zombieRunnerwalk2,
	zombieRunnerwalk3,
	zombieRunnerwalk4,
	zombieRunnerwalk5,
	zombieRunnerwalk6,
	]

# load zombieArcher zombie

s = pygame.image.load('Media/Graphics/archerShoot.png')
s = pygame.transform.scale(s, (25 * 2, 30 * 2))

zombieArchershoot = s

spritesheet = pygame.image.load('Media/Graphics/bustershots2.png')

character = Surface((12, 13), pygame.SRCALPHA)
character.blit(spritesheet, (-37, -80))
character = pygame.transform.scale(character, (40 * 2, 30 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (40, 0))
bustershot1 = stage

character = Surface((36, 20), pygame.SRCALPHA)
character.blit(spritesheet, (-77, -12))
character = pygame.transform.scale(character, (21 * 6, 13 * 6))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
bustershotm24 = stage

character = Surface((44, 10), pygame.SRCALPHA)
character.blit(spritesheet, (-144, -76))
character = pygame.transform.scale(character, (50 * 6, 5 * 6))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
bustershotlaser = stage
spritesheet = pygame.image.load('Media/Graphics/bustershots3.png')

character = Surface((10, 42), pygame.SRCALPHA)
character.blit(spritesheet, (-76, -60))
character = pygame.transform.scale(character, (13 * 6, 20 * 6))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
bustershotlaserup = stage

character = Surface((17, 22), pygame.SRCALPHA)
character.blit(spritesheet, (-50, -145))
character = pygame.transform.scale(character, (40 * 2, 30 * 2))
stage = Surface((300, 150), pygame.SRCALPHA)
stage.blit(character, (130, 0))
bustershotup = stage
bustershotlaserdown = pygame.transform.flip(bustershotlaserup, True,
		False)

# global variables

musicplaying = ''
invincible = False
maincounter = 0
wave = 1
abilityShield = False
abilityShoot = False
shows = False
showa = False
enemyid = 1
renemyid = 0


# Main Function

def main():
	i = 0
	global wave, maincounter, enemyid, abilityShoot, abilityShield, \
		renemyid

	# Create clock, set caption

	timer = pygame.time.Clock()
	pygame.display.set_caption('MazezombieRunner!')

	# Create Game

	game = Game()

	# Create Player

	player = Gladiator(game)

	# create player 2 for multiplayer

	player2 = copy(player)

	# Create Display

	display = Display('')

	# Create level

	room = Rooms(game, player)

	# Main Loop

	while 1:
		timer.tick(60)
		maincounter += 1
		if maincounter >= 100000:
			maincounter = 1

		# title screen is shown

		if game.screenfocus == 'Title':
			if not musicplaying == 'title':
				changemusic('title', True)
			for e in game.titlegroup:
				screen.blit(e.image, (0, 0))
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))
			game.title.update()
			game.buttongroup['start'].draw(screen)
			game.buttongroup['exit'].draw(screen)
			game.buttongroup['multiplayer'].draw(screen)
			game.buttongroup['highscore'].draw(screen)

		# main game will run from here

		if game.screenfocus == 'Game':
			if player.name == '':
				player.name = inputtxt('Please enter userId')
				player.name = player.name.split()[0]
			game.camera.update(game.camerafocus)
			player.update()

			if maincounter >= wave * 1000 and len(game.enemygroup) == 0:
				wave += 1
				if wave >= 99:
					game.screenfocus = 'Level Complete'
					changemusic('win', False)
				else:
					changemusic('wave', False)
				maincounter = 0

			# waves of enemy appearing formula here................

			if wave <= 10:
				spawntime = 110 - wave * 10
			if maincounter % spawntime == 0 and maincounter <= wave \
				* 1000 and wave <= 99:
				if wave == 1:

					rand = random.randint(1, 5)
				elif wave == 2:

					rand = random.randint(1, 7)
				elif wave == 3:

					rand = random.randint(1, 10)
				elif wave == 4:

					rand = random.randint(2, 13)
				elif wave >= 5:

					rand = random.randint(3, 14)

				# random position for zombie to spawn

				position = random.randint(1, 4)
				if position == 1:
					x = 156
					y = 304
				elif position == 2:

					x = 960
					y = 280
				elif position == 3:

					x = 571
					y = 85
				else:

					x = 571
					y = 525

				# add random enemies

				if rand <= 4:
					if random.randint(1, 2) == 1:
						game.enemygroup.add(zombie(x, y, player,
								enemyid))
					else:
						game.enemygroup.add(zombieGirl(x, y, player,
								enemyid))
				elif rand <= 9:
					game.enemygroup.add(zombieArcher(x, y, player, enemyid))
				elif rand <= 12:
					game.enemygroup.add(zombieRunner(x, y, player, enemyid, 2
							* wave + 1))
					changemusic('zombieRunner', False)
				else:
					game.enemygroup.add(zombieBoss(x, y, player, enemyid))
					changemusic('zombieBoss', False)
				enemyid += 1


			# showing all the entities on screen

			for e in game.entities:
				screen.blit(e.image, game.camera.apply(e))
			for e in game.playerentity:
				screen.blit(e.image, game.camera.apply(e))
			for e in game.projectilegroup:
				e.update(game.platforms)
				screen.blit(e.image, game.camera.apply(e))
			for e in game.enemygroup:
				e.update(game.platforms, game.projectilegroup)
				screen.blit(e.image, game.camera.apply(e))

			# drawing menu button on screen
			game.buttongroup['menu'].draw(screen)

			# showing powerups cooldown on screen
			if shows:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('s', True, (255, 255, 0))
				screen.blit(text, (400, -10))
			if showa:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('a', True, (0, 255, 0))
				screen.blit(text, (320, -10))

			# displaying health bar in hearts
			i = 1
			while i <= player.currentlifetotal:
				screen.blit(pygame.transform.scale(pygame.image.load('Media/Graphics/heart.png'
							), (30, 30)), (i * 30, 0))
				i += 1
			font = pygame.font.Font(None, 60)
			text = font.render('wave ' + str(wave), 1, (0, 0, 255))
			screen.blit(text, (500, 0))

			# score shown here

			font = pygame.font.Font(None, 60)
			text = font.render(str(player.score), 1, (0, 255, 0))
			screen.blit(text, (1100, 5))

		# pause screen functions shown here

		if game.screenfocus == 'Pause Menu':
			for e in game.titlegroup:
				screen.blit(e.image, (0, 0))
			game.pausemenu.update()
			game.buttongroup['resume'].draw(screen)
			game.buttongroup['exit'].draw(screen)
			game.buttongroup['shop'].draw(screen)

		#multiplayer mode options for chosing to be host or client
		if game.screenfocus == 'Multiplayer':

			for e in game.titlegroup:
				screen.blit(e.image, (0, 0))
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))
			game.title.update2()

			game.buttongroup['host'].draw(screen)
			game.buttongroup['connect'].draw(screen)
			game.buttongroup['back'].draw(screen)

		#characters select screen for multiplayer
		if game.screenfocus == 'MultiplayerCharacter':

			for e in game.titlegroup:
				screen.blit(e.image, (0, 0))
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					pass

				pos = pygame.mouse.get_pos()

				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['gladiator'].isOver(pos):
						game.playerentity.empty()

						player = Gladiator(game)
						room = Rooms(game, player)
						abilityShoot = True
						abilityShield = False

						if player.name == '':
							player.name = inputtxt('enter name')
							player.name = player.name.split()[0]

						game.screenfocus = 'Multiplayer'
					elif game.buttongroup['gunner'].isOver(pos):

						game.playerentity.empty()

						player = Gunner(game)
						room = Rooms(game, player)
						abilityShoot = True
						abilityShield = True

						if player.name == '':
							player.name = inputtxt('enter name')
							player.name = player.name.split()[0]

						game.screenfocus = 'Multiplayer'

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['gladiator'].isOver(pos):
						game.buttongroup['gladiator'].color = (0, 0,
								255)
					elif not game.buttongroup['gladiator'].isOver(pos):
						game.buttongroup['gladiator'].color = (255, 0,
								0)
					if game.buttongroup['gunner'].isOver(pos):
						game.buttongroup['gunner'].color = (0, 0, 255)
					elif not game.buttongroup['gunner'].isOver(pos):
						game.buttongroup['gunner'].color = (255, 0, 0)

			game.buttongroup['gladiator'].draw(screen)
			game.buttongroup['gunner'].draw(screen)
			screen.blit(standloopright2[1], (425, 350))
			screen.blit(standloopright[0], (125, 350))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Gladiator', True, (255, 255, 255))
			screen.blit(text, (215, 440))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Gunner', True, (255, 255, 255))
			screen.blit(text, (520, 440))

		#connecting from host
		if game.screenfocus == 'host':
			server = ''
			port = 6767

			hsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			try:
				hsocket.bind((server, port))
			except socket.error as e:
				str(e)

			print('Waiting for a connection, Server Started.')
			showtxt('Host ip is :'
					+ socket.gethostbyname(socket.gethostname()))

			while True:
				 #getting other player's character type
				(data, addr) = hsocket.recvfrom(1024)
				data = data.decode('utf-8')
				if data == 'gunner':
					player2 = Gunner(game)
					game.playerentity.remove(player2)
				hsocket.sendto(player.type.encode('utf-8'), addr)

				game.screenfocus = 'Server'
				wave = 1
				break
		#running game from host end
		if game.screenfocus == 'Server':
			game.camera.update(game.camerafocus)
			player.update()

			if maincounter >= wave * 1000 and len(game.enemygroup) == 0:
				wave += 1
				if wave >= 99:
					game.screenfocus = 'Level Complete'
					changemusic('win', False)
				else:
					changemusic('wave', False)
				maincounter = 0

			# add random enemies

			if wave <= 10:
				spawntime = 110 - wave * 10

			if maincounter % spawntime == 0 and maincounter <= wave \
				* 1000 and wave <= 99:
				if wave == 1:

					rand = random.randint(1, 5)
				elif wave == 2:

					rand = random.randint(1, 7)
				elif wave == 3:

					rand = random.randint(1, 10)
				elif wave == 4:

					rand = random.randint(2, 13)
				elif wave >= 5:

					rand = random.randint(3, 14)

				position = random.randint(1, 4)
				if position == 1:
					x = 156
					y = 304
				elif position == 2:

					x = 960
					y = 280
				elif position == 3:

					x = 571
					y = 85
				else:

					x = 571
					y = 525

				if rand <= 4:
					if random.randint(1, 2) == 1:
						game.enemygroup.add(zombie(x, y, player,
								enemyid))
					else:
						game.enemygroup.add(zombieGirl(x, y, player,
								enemyid))
				elif rand <= 9:

					game.enemygroup.add(zombieArcher(x, y, player, enemyid))
				elif rand <= 12:

					game.enemygroup.add(zombieRunner(x, y, player, enemyid, 2
							* wave + 1))
					changemusic('zombieRunner', False)
				else:
					game.enemygroup.add(zombieBoss(x, y, player, enemyid))
					changemusic('zombieBoss', False)

				enemyid += 1

			for e in game.entities:
				screen.blit(e.image, game.camera.apply(e))

			#ablities cooldown indicator is shown here
			if showa:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('a', True, (0, 255, 0))
				screen.blit(text, (320, -10))
			if shows:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('s', True, (255, 255, 0))
				screen.blit(text, (400, -10))

			#sending and reciving data to/from client
			try:
				#sending host side player info to client
				player_host = player.__dict__.copy()
				player_host.pop('image')
				player_host.pop('bg')
				player_host.pop('detectable')
				player_host.pop('game')
				player_host.pop('projectile')
				player_host.pop('_Sprite__g')
				player_host['rect'] = tuple(player_host['rect'])

				enemy_host = []  
				projectile_host = []
				#sending enemy's data to client
				for e in game.enemygroup:
					etemp = e.__dict__.copy()
					etemp.pop('image')
					etemp.pop('player')
					etemp.pop('detectable')
					etemp.pop('_Sprite__g')
					etemp['rect'] = tuple(etemp['rect'])
					enemy_host.append(etemp)
				#sending projectiles info towards client end
				for q in game.projectilegroup:
					temp = q.__dict__.copy()
					temp.pop('image')
					temp.pop('game')
					temp.pop('pxl')
					temp.pop('detectable')
					temp.pop('_Sprite__g')
					temp['rect'] = tuple(temp['rect'])
					projectile_host.append(temp)
				#object to store all info to be sent
				saveobj = (player_host, enemy_host, projectile_host, wave)
			   
				hsocket.sendto(json.dumps(saveobj).encode('utf-8'),
							   addr)
			   
		
				(recv_client, addr) = hsocket.recvfrom(1024 * 8)
				recv_client = json.loads(recv_client.decode('utf-8'))
			   

				#variable to check if client's character killed which id mobs
				renemyid = recv_client[1]
				#client end player info is updated here
				player2.__dict__.update(recv_client[0])
				player2.animate()
				player2.rect = Rect(player2.rect)
				player2.detectable = pygame.sprite.Group()
				player2.detectable.rect = Rect(player2.rect)
				#projectiles info from client end is updated here
				for e in recv_client[2]:
					pro = copy(Projectile(player2, game, e['type']))
					pro.detectable.rect = Rect(e['rect'])
					pro.rect = Rect(e['rect'])
				  
					screen.blit(pro.image, game.camera.apply(pro))
				if not player2.destroyed == True:
					screen.blit(player2.image,
								game.camera.apply(player2))
			except Exception as e:
				print(e)
			if player.destroyed == True:
				#game ends when host side character dies
				game.screenfocus = 'Multiplayer Game Over'
				hsocket.close()
			for e in game.playerentity:
				screen.blit(e.image, game.camera.apply(e))
			for e in game.projectilegroup:
				e.update(game.platforms)
				screen.blit(e.image, game.camera.apply(e))
			for e in game.enemygroup:
				e.update(game.platforms, game.projectilegroup)
				screen.blit(e.image, game.camera.apply(e))
				if renemyid == e.id:
					game.enemygroup.remove(e)
			#player score is shown here
			font = pygame.font.Font(None, 60)
			text = font.render(str(player.score), 1, (0, 255, 0))
			screen.blit(text, (1100, 5))

			# displaying health bar in hearts
			i = 1
			while i <= player.currentlifetotal:
				screen.blit(pygame.transform.scale(pygame.image.load('Media/Graphics/heart.png'
							), (30, 30)), (i * 30, 0))
				i += 1
			#current wave info is shown here
			font = pygame.font.Font(None, 60)
			text = font.render('wave ' + str(wave), 1, (0, 0, 255))
			screen.blit(text, (500, 0))

		#connecting from client
		if game.screenfocus == 'Connect':
			ip = inputtxt('Please enter ip')
			ip = ip + ''
			cl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (ip, 6767)
			print('connected')
			cl.sendto(player.type.encode('utf-8'), addr)
			(data, addr) = cl.recvfrom(1024)
			data = data.decode('utf-8')
			#getting character type info of host end
			if data == 'gunner':
				player2 = Gunner(game)
				game.playerentity.remove(player2)
			if player.name == '':
				player.name = inputtxt('enter name')
			game.screenfocus = 'Client'
		   #running game from client end
		if game.screenfocus == 'Client':
			game.camera.update(game.camerafocus)
			if player.destroyed == True:
				player.invincible = True
				player.icounter = 0
			player.update()
			if maincounter >= wave * 1000 and len(game.enemygroup) == 0:
				wave += 1
				if wave >= 99:
					game.screenfocus = 'Level Complete'
					changemusic('win', False)
				else:
					changemusic('wave', False)
				maincounter = 0

			# add random enemies
			for e in game.entities:
				screen.blit(e.image, game.camera.apply(e))
			
			#sending and reciving data from/to client
			try:
				#sending client's end player info to host
				player_client = player.__dict__.copy()
				player_client.pop('image')
				player_client.pop('bg')
				player_client.pop('detectable')
				player_client.pop('game')
				player_client.pop('projectile')
				player_client.pop('_Sprite__g')
				player_client['rect'] = tuple(player_client['rect'])

				projectile_client = []
				#sending projectiles from client end info to server
				for q in copy(game.projectilegroup):
					temp = q.__dict__.copy()
					temp.pop('image')
					temp.pop('game')
					temp.pop('pxl')
					temp.pop('detectable')
					temp.pop('_Sprite__g')
					temp['rect'] = tuple(temp['rect'])
					projectile_client.append(temp)

				#object to store all info to be sent
				saveobj = (player_client, enemyid, projectile_client)
		
				(recv_host, addr) = cl.recvfrom(1024 * 20)
				recv_host = json.loads(recv_host.decode('utf-8'))
			   
			   
				cl.sendto(json.dumps(saveobj).encode('utf-8'), addr)
			   
				i = 0
				wave = recv_host[3]
				#host end character data ins updated here
				player2.__dict__.update(recv_host[0])
				player2.animate()
				player2.rect = Rect(player2.rect)
				player2.detectable = pygame.sprite.Group()
				player2.detectable.rect = Rect(player2.rect)

				#end game if host character dies
				if player2.destroyed == True:
					game.screenfocus = 'Multiplayer Game Over'
					cl.close()
				game.projectilegroupc.empty()

				#projectiles from host end are updated and shown here
				for e in recv_host[2]:
					pro = copy(Projectile(player2, game, e['type']))
					pro.detectable.rect = Rect(e['rect'])
					pro.rect = Rect(e['rect'])
					game.projectilegroupc.add(pro)
					screen.blit(pro.image, game.camera.apply(pro))
				screen.blit(player2.image, game.camera.apply(player2))

				#all enemies data is created/updated/deleted here from host
				game.enemygroup.empty()
				for e in recv_host[1]:
					if e['type'] == 'zombie':
						mob = copy(zombie(0, 0, player, enemyid))
					elif e['type'] == 'zombieRunner':

						mob = copy(zombieRunner(0, 0, player, enemyid))
					elif e['type'] == 'zombieGirl':

						mob = copy(zombieGirl(0, 0, player, enemyid))
					elif e['type'] == 'zombieArcher':

						mob = copy(zombieArcher(0, 0, player, enemyid))
					elif e['type'] == 'zombieBoss':

						mob = copy(zombieBoss(0, 0, player, enemyid))

					mob.image = copy(zombieArcherwalk1)
					mob.rect = Rect(e['rect'])
					mob.detectable.rect = Rect(e['rect'])
					mob.__dict__.update(e)
					mob.currentlifetotal = e['currentlifetotal']
					mob.animate()
					mob.rect = Rect(e['rect'])
					mob.detectable.rect = Rect(e['rect'])
					mob.player = player
					screen.blit(mob.image, game.camera.apply(mob))
					mob.collide(0, mob.yvel, game.platforms,
								game.projectilegroup, player)
					game.enemygroup.add(mob)
			except Exception as e:
				print(str(e))
			if not player.destroyed == True:
				for e in game.playerentity:
					screen.blit(e.image, game.camera.apply(e))
			for e in game.projectilegroup:
				e.update(game.platforms)
				screen.blit(e.image, game.camera.apply(e))

			# displaying health bar in hearts

			i = 1
			while i <= player.currentlifetotal:
				screen.blit(pygame.transform.scale(pygame.image.load('Media/Graphics/heart.png'
							), (30, 30)), (i * 30, 0))
				i += 1
			#wave and cooldown indicators
			font = pygame.font.Font(None, 60)
			text = font.render('wave ' + str(wave), 1, (0, 0, 255))
			screen.blit(text, (500, 0))
			font = pygame.font.Font(None, 60)
			text = font.render(str(player.score), 1, (0, 255, 0))
			screen.blit(text, (1100, 5))
			if showa:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('a', True, (0, 255, 0))
				screen.blit(text, (320, -10))
			if shows:
				font = pygame.font.SysFont('Arial', 50)
				text = font.render('s', True, (255, 255, 0))
				screen.blit(text, (400, -10))
		#single player gameover logic
		if game.screenfocus == 'Game Over':
			bg = \
				pygame.image.load('Media/Graphics/Backgrounds/game over.jpg'
								  )
			screen.blit(bg, (0, 0))
			#scores are stored here
			if player.score > 0 and not player.name == ' ':
				myfile = open('scorea.bin', 'a')
				temp = str(player.name) + ' ' + str(player.score) + '\n'
				if len(temp.split()) >= 2:
					myfile.write(temp)
				player.score = -1
				myfile.close()
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))
			game.buttongroup['exit'].draw(screen)
			game.buttongroup['restart'].draw(screen)
			game.buttongroup['highscore'].draw(screen)
			if game.pausemenu.inputhandler():
				invincible = False
				pygame.time.delay(1000)
				game = Game()
				wave = 1
				maincounter = 0
				# Create Display
				display = Display('')
				# Create level
				player = Gunner(game)
				room = Rooms(game, player)
				game.screenfocus = 'Title'
				wave = 1
				maincounter = 0

		#logic where game over happens in multiplayer
		if game.screenfocus == 'Multiplayer Game Over':
			bg = \
				pygame.image.load('Media/Graphics/Backgrounds/game over.jpg'
								  )
			screen.blit(bg, (0, 0))

			#storing multiplayer scores
			if player.score > 0 and not player.name == ' ':
				myfile = open('scoream.bin', 'a')
				temp = str(player.name) + ' and ' + str(player2.name) \
					+ ' ' + str(int(player.score) + int(player2.score)) \
					+ '\n'
				if len(temp.split()) >= 2:
					myfile.write(temp)
				player.score = -1
				myfile.close()
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))

			game.buttongroup['exit'].draw(screen)

			game.buttongroup['restart'].draw(screen)

			game.buttongroup['highscore'].draw(screen)

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					game.screenfocus = 'Game'

				pos = pygame.mouse.get_pos()
				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['exit'].isOver(pos):
						raise SystemExit('QUIT')
					elif game.buttongroup['restart'].isOver(pos):
						
						invincible = False
						pygame.time.delay(1000)
						game = Game()
						wave = 1
						maincounter = 0

							# Create Display

						display = Display('')

							# Create level

						player = Gunner(game)
						room = Rooms(game, player)

						game.screenfocus = 'Title'
					elif game.buttongroup['highscore'].isOver(pos):
						game.screenfocus = 'MultiplayerScore'

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['exit'].isOver(pos):
						game.buttongroup['exit'].color = (100, 255, 0)
					elif not game.buttongroup['exit'].isOver(pos):
						game.buttongroup['exit'].color = (255, 0, 0)

					if game.buttongroup['restart'].isOver(pos):
						game.buttongroup['restart'].color = (100, 255,
								0)
					elif not game.buttongroup['restart'].isOver(pos):
						game.buttongroup['restart'].color = (0, 255,
								100)
					if game.buttongroup['highscore'].isOver(pos):
						game.buttongroup['highscore'].color = (100,
								255, 0)
					elif not game.buttongroup['highscore'].isOver(pos):
						game.buttongroup['highscore'].color = (255,
								255, 0)

		#highscores will be stored here
		if game.screenfocus == 'Score':
			scoreImg = pygame.image.load('Media/Graphics/title.jpg')
			screen.blit(scoreImg, (0, 0))

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					pass

				pos = pygame.mouse.get_pos()

				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['back'].isOver(pos):

						game.screenfocus = 'Title'
					if game.buttongroup['mhighscore'].isOver(pos):

						game.screenfocus = 'MultiplayerScore'

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (100, 255, 0)
					elif not game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (255, 255, 0)
				if game.buttongroup['mhighscore'].isOver(pos):
					game.buttongroup['mhighscore'].color = (0, 100, 255)
				elif not game.buttongroup['mhighscore'].isOver(pos):
					game.buttongroup['mhighscore'].color = (255, 0, 255)

			game.buttongroup['back'].draw(screen)
			game.buttongroup['mhighscore'].draw(screen)
			font = pygame.font.SysFont('Arial', 50)
			text = font.render('Highscores', True, (0, 0, 255))
			screen.blit(text, (350, 230))
			x = 350 + 50

			name = []
			hscore = []
			myfile = open('scorea.bin', 'r')
			lines = myfile.readlines()
			myfile.close()

			for ln in lines:
				if len(ln.split()) >= 2:
					txt = ln.split()
					name.append(txt[0])
					hscore.append(int(txt[1]))
			length = len(hscore)
			for i in range(0, length - 1):
				for j in range(0, length - i - 1):
					if hscore[j] < hscore[j + 1]:
						temp1 = hscore[j]
						hscore[j] = hscore[j + 1]
						hscore[j + 1] = temp1
						temp2 = name[j]
						name[j] = name[j + 1]
						name[j + 1] = temp2
			font1 = pygame.font.SysFont('Arial', 22)

			
			y = 300
			if length > 5:
				for i in range(0, 5):
					txt = font1.render(name[i] + '     '
							+ str(hscore[i]), True, (0, 255, 0))
					screen.blit(txt, (x, y))
					y = y + 30
			else:
				for i in range(0, length):
					txt = font1.render(name[i] + '     '
							+ str(hscore[i]), True, (0, 255, 0))
					screen.blit(txt, (x, y))
					y = y + 30
			font = pygame.font.SysFont('Arial', 50)
			text = font.render('Game Over', True, (0, 0, 255))
			myfile.close()
		#multiplayer highscores
		if game.screenfocus == 'MultiplayerScore':
			scoreImg = pygame.image.load('Media/Graphics/title.jpg')
			screen.blit(scoreImg, (0, 0))

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					pass
				pos = pygame.mouse.get_pos()

				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['back'].isOver(pos):

						game.screenfocus = 'Title'

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (100, 255, 0)
					elif not game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (255, 255, 0)

			game.buttongroup['back'].draw(screen)
			font = pygame.font.SysFont('Arial', 50)
			text = font.render('Multiplayer Highscores', True, (0, 0,
							   255))
			screen.blit(text, (350, 230))
			x = 350 + 50

			name = []
			hscore = []
			myfile = open('scoream.bin', 'r')
			lines = myfile.readlines()
			myfile.close()

			for ln in lines:
				if len(ln.split()) >= 3:
					txt = ln.split()
					name.append(str(txt[0]) + ' ' + str(txt[1]) + ' '
								+ str(txt[2]))

					hscore.append(int(txt[3]))

			length = len(hscore)
			
			for i in range(0, length - 1):
				for j in range(0, length - i - 1):
					if hscore[j] < hscore[j + 1]:
						temp1 = hscore[j]
						hscore[j] = hscore[j + 1]
						hscore[j + 1] = temp1
						temp2 = name[j]
						name[j] = name[j + 1]
						name[j + 1] = temp2
			font1 = pygame.font.SysFont('Arial', 22)

		   
			y = 300
			if length > 5: #how much total highscore to show
				for i in range(0, 5):
					txt = font1.render(name[i] + '     '
							+ str(hscore[i]), True, (0, 255, 0))
					screen.blit(txt, (x, y))
					y = y + 30
			else:
				for i in range(0, length):
					txt = font1.render(name[i] + '     '
							+ str(hscore[i]), True, (0, 255, 0))
					screen.blit(txt, (x, y))
					y = y + 30
			font = pygame.font.SysFont('Arial', 50)
			text = font.render('Game Over', True, (0, 0, 255))
			myfile.close()

		#single player character select
		if game.screenfocus == 'Character':
			for e in game.titlegroup:
				screen.blit(e.image, (0, 0))
			for e in game.menugroup:
				screen.blit(e.image, (e.rect.x, e.rect.y))

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					pass

				pos = pygame.mouse.get_pos()

				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['gladiator'].isOver(pos):
						game.playerentity.empty()

						player = Gladiator(game)
						room = Rooms(game, player)

						game.screenfocus = 'Game'
					elif game.buttongroup['gunner'].isOver(pos):

						game.playerentity.empty()

						player = Gunner(game)
						room = Rooms(game, player)

						game.screenfocus = 'Game'

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['gladiator'].isOver(pos):
						game.buttongroup['gladiator'].color = (0, 0,
								255)
					elif not game.buttongroup['gladiator'].isOver(pos):
						game.buttongroup['gladiator'].color = (255, 0,
								0)
					if game.buttongroup['gunner'].isOver(pos):
						game.buttongroup['gunner'].color = (0, 0, 255)
					elif not game.buttongroup['gunner'].isOver(pos):
						game.buttongroup['gunner'].color = (255, 0, 0)

			game.buttongroup['gladiator'].draw(screen)
			game.buttongroup['gunner'].draw(screen)
			screen.blit(standloopright2[1], (425, 350))
			screen.blit(standloopright[0], (125, 350))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Gladiator', True, (255, 255, 255))
			screen.blit(text, (215, 440))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Gunner', True, (255, 255, 255))
			screen.blit(text, (520, 440))

		#single player shop items
		if game.screenfocus == 'Shop':
			scoreImg = \
				pygame.image.load('Media/Graphics/Backgrounds/shop.jpg')
			screen.blit(scoreImg, (0, 0))

			for e in pygame.event.get():
				if e.type == QUIT:
					raise SystemExit('QUIT')
				if e.type == KEYDOWN and e.key == K_ESCAPE:
					raise SystemExit('ESCAPE')
				if e.type == KEYDOWN and e.key == K_RETURN:
					pass
				pos = pygame.mouse.get_pos()
				if e.type == pygame.MOUSEBUTTONDOWN:
					if game.buttongroup['back'].isOver(pos):
						game.screenfocus = 'Pause Menu'
					elif game.buttongroup['ability1'].isOver(pos):
						if player.score >= 5 \
							and not game.buttongroup['ability1'].text \
							== 'Bought':
							player.score -= 100
							abilityShoot = True
							game.buttongroup['ability1'].text = 'Bought'
					elif game.buttongroup['ability2'].isOver(pos):

						if player.score >= 5 \
							and not game.buttongroup['ability2'].text \
							== 'Bought':
							player.score -= 100

							abilityShield = True
							game.buttongroup['ability2'].text = 'Bought'
					elif game.buttongroup['heart'].isOver(pos):

						if player.score >= 30 \
							and player.currentlifetotal < 9:

							player.currentlifetotal += 1
							player.score -= 30
						elif player.score < 30:
							font = pygame.font.SysFont('Arial', 30)
							text = font.render('less credit', True,
									(255, 255, 255))
							screen.blit(text, (500, 350))
						elif player.currentlifetotal >= 9:
							font = pygame.font.SysFont('Arial', 30)
							text = font.render('already full health',
									True, (255, 255, 255))
							screen.blit(text, (500, 350))

				if e.type == pygame.MOUSEMOTION:
					if game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (0, 0, 255)
					elif not game.buttongroup['back'].isOver(pos):
						game.buttongroup['back'].color = (255, 0, 0)
					if game.buttongroup['ability1'].isOver(pos):
						game.buttongroup['ability1'].color = (0, 0, 255)
					elif not game.buttongroup['ability1'].isOver(pos):
						game.buttongroup['ability1'].color = (255, 0, 0)
					if game.buttongroup['ability2'].isOver(pos):
						game.buttongroup['ability2'].color = (0, 0, 255)
					elif not game.buttongroup['ability2'].isOver(pos):
						game.buttongroup['ability2'].color = (255, 0, 0)

					if game.buttongroup['heart'].isOver(pos):
						game.buttongroup['heart'].color = (0, 0, 255)
					elif not game.buttongroup['heart'].isOver(pos):
						game.buttongroup['heart'].color = (255, 0, 0)

			game.buttongroup['back'].draw(screen)
			game.buttongroup['ability1'].draw(screen)
			game.buttongroup['ability2'].draw(screen)
			game.buttongroup['heart'].draw(screen)

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Weapons:', True, (255, 255, 0))
			screen.blit(text, (50, 230))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('health:', True, (255, 255, 0))
			screen.blit(text, (50, 360))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('Credit:', True, (0, 255, 255))
			screen.blit(text, (50, 300))
			screen.blit(text, (50, 430))
			screen.blit(text, (20, 50))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('100', True, (0, 255, 0))
			if not game.buttongroup['ability1'].text == 'Bought':

				screen.blit(text, (200, 300))
			if not game.buttongroup['ability2'].text == 'Bought':
				screen.blit(text, (500, 300))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render('30', True, (0, 255, 0))
			screen.blit(text, (200, 430))

			font = pygame.font.SysFont('Arial', 30)
			text = font.render(str(player.score), True, (0, 255, 0))
			screen.blit(text, (120, 50))

			screen.blit(heartpic, (380, 350))

			if player.type == 'gladiator':
				screen.blit(arrow2, (340, 240))
				screen.blit(shieldingright1, (540, 240))
			else:

				screen.blit(bustershotm24, (230, 210))
				screen.blit(bustershotlaser, (540, 240))

		pygame.display.update()


class Game(object):

	def __init__(self):

		# Create Sprite Groups

		self.buttongroup = {}
		self.entities = pygame.sprite.Group()
		self.bg = pygame.sprite.Group()
		self.playerentity = pygame.sprite.Group()
		self.projectilegroup = pygame.sprite.Group()
		self.projectilegroupc = pygame.sprite.Group()

		self.enemygroup = pygame.sprite.Group()
		self.menugroup = pygame.sprite.Group()
		self.titlegroup = pygame.sprite.Group()
		self.detectablegroup = pygame.sprite.Group()

		# Create Camera

		self.camera = ''
		self.camerafocus = ''

		# Create Platforms

		self.platforms = []

	   
 
	  
		# Create Screen Focus

		self.screenfocus = 'Title'

		# Create Title

		self.title = Title(self)

		# Create Gameover

		self.gameover = GameOver(self)

		# Create Level Complete

		self.levelcomplete = LevelComplete(self)

		# Create Pause Menu

		self.pausemenu = PauseMenu(self)

	  
  


class Entity(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)


class Platform(Entity):

	def __init__(
		self,
		x,
		y,
		w,
		h,
		chatid=0,
		):
		Entity.__init__(self)
		self.rect = Rect(x * 3, y * 3, w * 3, h * 3)
		self.chatid = chatid

	def update(self):
		pass


class Gladiator(Entity):

	def __init__(self, game, typee='gladiator'):
		Entity.__init__(self)
		# player type
		self.type = typee

		# Add Player to Game

		self.icounter = 0  # invincible counter
		self.name = ''
		self.game = game
		self.score = 0
		self.game.playerentity.add(self)

		# Set Player Velocities

		self.xvel = 0
		self.yvel = 0

		# Set Player Offsets

		self.xoffset = -128
		self.yoffset = 0

		# cooldown
		self.shootcooldown = 0

		# Counters

		self.walkcounter = 0
		self.standcounter = 0

		self.attackcounter = 0
		self.takedamagecounter = 0
		self.counter = 0

		# States
		# abilities

		self.isshield = False
		self.shooting = False

		self.bg = \
			pygame.image.load('Media/Graphics/Backgrounds/arena.png')
	   
		self.destroyed = False

		self.projectile = None

		self.collideright = False
		self.faceright = True
		self.takingdamage = False
		self.attacking = False

		self.moving = False

		# Create Player Sprite

		self.image = Surface((19 * 2, 35 * 2), pygame.SRCALPHA)
		self.rect = Rect(0, 0, 19 * 2, 35 * 2)

		# Create Player Detectable Area

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(0, 0, 19 * 2, 35 * 2)
		self.detectable.image = Surface((19 * 2, 35 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		game.detectablegroup.add(self.detectable)

		# Life Meter

		self.lifetotal = [
			'',
			'l',
			'll',
			'lll',
			'llll',
			'lllll',
			'llllll',
			'lllllll',
			'llllllll',
			'lllllllll',
			]
		self.currentlifetotal = 9

		# Inputs

		self.up = False
		self.down = False
		self.right = False
		self.left = False
		self.space = False
		self.canshoot = False
	   
	#pickle serilization fuctions for sending via socket
	def __getstate__(self):


		state = self.__dict__.copy()

		surface = state.pop('image')

	   

		surface = state.pop('bg')

	   
		surface = state.pop('detectable')

		surface = state.pop('game')

		return state

	def __setstate__(self, state):

	   
	   

		state['bg'] = \
			pygame.image.load('Media/Graphics/Backgrounds/arena.png')

		
		self.__dict__.update(state)

	def startingposition(self, x, y):
		self.rect = Rect(x, y, 19 * 2, 22 * 2)
		self.detectable.rect = Rect(x, y, 19 * 2, 22 * 2)

	def inputhandler(self):

		for e in pygame.event.get():

			if e.type == QUIT:
				raise SystemExit('QUIT')
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				if self.game.screenfocus == 'Game':
					self.game.screenfocus = 'Pause Menu'
			if e.type == KEYDOWN and e.key == K_UP:
				self.up = True
			if e.type == KEYDOWN and e.key == K_DOWN:
				self.down = True
			if e.type == KEYDOWN and e.key == K_LEFT:
				self.left = True
			if e.type == KEYDOWN and e.key == K_RIGHT:
				self.right = True
			if e.type == KEYDOWN and e.key == K_SPACE \
				and self.destroyed == False:
				self.space = True

			if e.type == KEYDOWN and e.key == K_a and abilityShield \
				== True and self.destroyed == False:
				self.isshield = True
			if e.type == KEYDOWN and e.key == K_s and abilityShoot \
				== True and self.destroyed == False:
				self.canshoot = True

			if e.type == KEYDOWN and e.key == K_RETURN:
				self.game.pausemenu.createpausemenu()
				self.game.screenfocus = 'Pause Menu'
			if e.type == KEYUP and e.key == K_SPACE:
				self.space = False
			if e.type == KEYUP and e.key == K_UP:
				self.up = False

			if e.type == KEYUP and e.key == K_a:
				self.isshield = False
			if e.type == KEYUP and e.key == K_s:
				self.canshoot = False

			if e.type == KEYUP and e.key == K_DOWN:
				self.down = False
				self.dancecounter = 0
			if e.type == KEYUP and e.key == K_RIGHT:
				self.right = False
				self.counter = 0
			if e.type == KEYUP and e.key == K_LEFT:
				self.left = False
				self.counter = 0

			pos = pygame.mouse.get_pos()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game.buttongroup['menu'].isOver(pos):

					self.game.screenfocus = 'Pause Menu'
			if e.type == pygame.MOUSEMOTION:
				if self.game.buttongroup['menu'].isOver(pos):

					self.game.buttongroup['menu'].color = (100, 255, 0)
				else:
					self.game.buttongroup['menu'].color = (0, 0, 255)

	def update(self):

		# cooldown counter

		global showa, shows
		iscolor = False

		#cooldown
		if abilityShoot:
			self.shootcooldown += 1
			if self.shootcooldown >= 10:
				self.shootcooldown = 10
				shows = True
		if abilityShield:
			#cooldown indicator
			showa = True

		self.inputhandler()

		# Apply Inputs

		# Move if not taking damage

		if self.up:
			if self.takingdamage == False:
				self.yvel = -12
				self.moving = True

		  
		# Move if not taking damage
		if self.down:
			if self.takingdamage == False:
				self.yvel = 12
				self.moving = True

			
		# Move if not taking damage
		if self.left:
			self.faceright = False
			if self.takingdamage == False:
				self.xvel = -12
				self.moving = True

			
		# Move if not taking damage
		if self.right:
			self.faceright = True
			if self.takingdamage == False:
				self.xvel = 12
				self.moving = True

			
		#basic attack
		if self.space and not self.isshield:

			projectile = Projectile(self, self.game, 'sword')
			self.game.projectilegroup.add(projectile)
			changemusic('slash', False)
			self.space = False
			self.attacking = True
		#when shielding
		if self.isshield:

			self.game.projectilegroup.remove(self.projectile)  # removes previous shield projectile from list so multiple dont add
			self.projectile = Projectile(self, self.game, 'shield')
			self.game.projectilegroup.add(self.projectile)
		# create projectiles
		if self.canshoot and self.shootcooldown >= 10:

			
			projectile = Projectile(self, self.game, 'arrow')
			self.game.projectilegroup.add(projectile)

			self.shootcooldown = 0
			self.shooting = True
			self.attacking = True

			

		# setting a boundary

		try:
			color = self.bg.get_at((int(self.detectable.rect.x / 3
								   + self.xvel * 2),
								   int(self.detectable.rect.y / 3
								   + self.yvel * 2)))  # cant move in certain colors
			if color == (185, 122, 87, 255) or color == (136, 0, 21,
					255):

				self.xvel = 0
				self.yvel = 0
		except:

			pass
		# Stop player if not taking damage
		if not (self.left or self.right):
			if not self.takingdamage:

				self.xvel = 0
		if not (self.up or self.down):
			if not self.takingdamage:

				self.yvel = 0

		if not (self.up or self.down or self.right or self.left):
			if not self.takingdamage:
				self.moving = False

		   
		 # Move player if took damage
		if self.takingdamage:
			if self.collideright:
				self.xvel = -5
			else:
				self.xvel = 5

		   
		# Stop attacking after 9 updates
		if self.attackcounter > 6:
			self.attacking = False
			self.attackcounter = 0
			self.standcounter = 0
			self.shooting = False

			
		# Player stops taking damage after 14 updates

		if self.takedamagecounter > 13:
			self.takingdamage = False
			self.takedamagecounter = 0

			
		# Increase or Reset Counters

		if self.attacking:
			self.attackcounter = self.attackcounter + 1
		if self.takingdamage:
			self.takedamagecounter = self.takedamagecounter + 1
		if not self.moving:
			self.standcounter = 0

		# Collisions

		self.detectable.rect.left += self.xvel
		self.collide(self.xvel, 0)
		self.detectable.rect.top += self.yvel
		self.onGround = False
		self.collide(0, self.yvel)

		# Offsets

		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(self, xvel, yvel):
		global invincible

		if invincible:
			self.icounter += 1
		if self.icounter >= 100:

			self.icounter = 0
			invincible = False

		

		# Collide Platforms

		for p in self.game.platforms:
			if pygame.sprite.collide_rect(self.detectable, p):
				if xvel > 0:
					self.detectable.rect.right = p.rect.left
				if xvel < 0:
					self.detectable.rect.left = p.rect.right
				if yvel > 0:
					self.detectable.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0
				if yvel < 0:
					self.detectable.rect.top = p.rect.bottom

		# Collide Enemies

		for e in self.game.enemygroup:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable):

				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False

				if not invincible:
					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal - 1

					invincible = True
				elif self.currentlifetotal <= 0:

					if self.game.screenfocus == 'Game':

						self.game.screenfocus = 'Game Over'
					elif self.game.screenfocus == 'Client':
						self.destroyed = True
					elif self.game.screenfocus == 'Server':

						self.destroyed = True

		# collide projectile

		for e in self.game.projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable) and e.type == 'guu':
				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False
				if not invincible:

					self.game.projectilegroup.remove(e)
					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal \
						- e.damage
					invincible = True

				if self.currentlifetotal <= 0:
					if self.game.screenfocus == 'game':

						self.game.screenfocus = 'Game Over'
					elif self.game.screenfocus == 'Client':
						self.destroyed = True
					elif self.game.screenfocus == 'Server':
						self.destroyed = True
		for e in self.game.projectilegroupc:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable) and e.type == 'guu':
				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False
				if not invincible:

					self.game.projectilegroupc.remove(e)

					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal \
						- e.damage
					invincible = True


	def animate(self):

		state = []
		state.append(False)
		state.append(self.moving)
		state.append(self.faceright)
		state.append(self.takingdamage)
		state.append(self.attacking)

		# Moving

		if state[1]:
			if state[0]:
				pass
			else:
				if not self.isshield:

					if state[2]:
						self.walkloop(walkloopright)
					else:
						self.walkloop(walkloopleft)
		else:
			if state[0]:
				pass
			else:

				if state[2]:
					self.standloop(standloopright)
				else:
					self.standloop(standloopleft)

		# Attacking

		if state[4] and not self.isshield:
			if state[0]:
				pass
			else:

				if state[1]:
					if state[2]:
						if self.shooting:
							self.updatecharacter(shootarrowright)
						else:

							self.attackloop(shootrightstandloop)
					else:
						if self.shooting:
							self.updatecharacter(shootarrowleft)
						else:

							self.attackloop(shootleftstandloop)
				else:
					if state[2]:
						if self.shooting:
							self.updatecharacter(shootarrowright)
						else:

							self.attackloop(shootrightstandloop)
					else:
						if self.shooting:
							self.updatecharacter(shootarrowleft)
						else:

							self.attackloop(shootleftstandloop)
		if self.isshield:

			if state[1]:
				if state[2]:
					self.walkloop(shieldingloop)
				else:
					self.walkloop(shieldingloop2)
			else:
				if state[2]:
					self.updatecharacter(shieldingloop[0])
				else:
					self.updatecharacter(pygame.transform.flip(shieldingloop[0],
							True, False))

		# Hurt

		if state[3]:
			if state[2]:
				self.updatecharacter(takedamageright)
			else:
				self.updatecharacter(takedamageleft)

	# Standing Animation Loop

	def standloop(self, loop):

		if self.standcounter == 0 or self.standcounter == 1:
			self.walkcounter = 0
			self.updatecharacter(loop[0])
		elif self.standcounter == 5:
			self.updatecharacter(loop[1])
		elif self.standcounter == 10:
			self.updatecharacter(loop[2])
		elif self.standcounter == 15:
			self.updatecharacter(loop[3])
		elif self.standcounter == 20:
			self.updatecharacter(loop[0])
			self.standcounter = 0
		self.standcounter = self.standcounter + 1

	def attackloop(self, loop):

	   

		if self.attackcounter <= 0 or self.attackcounter == 1:
			self.walkcounter = 0
			self.updatecharacter(loop[0])
		elif self.attackcounter <= 4:
			self.updatecharacter(loop[1])
		elif self.attackcounter <= 5:
			self.updatecharacter(loop[3])
		elif self.attackcounter <= 6:
			self.updatecharacter(loop[3])

	# Walking Animation Loop

	def walkloop(self, loop):
		if self.walkcounter == 0 or self.walkcounter == 1:
			self.standcounter = 0

			self.updatecharacter(loop[0])
		elif self.walkcounter == 6:
			self.updatecharacter(loop[0])
		elif self.walkcounter == 12:
			self.updatecharacter(loop[1])
		elif self.walkcounter == 18:
			self.updatecharacter(loop[2])
		elif self.walkcounter == 24:
			self.updatecharacter(loop[3])
		elif self.walkcounter >= 30:
			self.updatecharacter(loop[0])
			self.walkcounter = 3
		self.walkcounter = self.walkcounter + 1

		# Update Current Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class Gunner(Entity):

	def __init__(self, game, typee='gunner'):
		Entity.__init__(self)
		#player type
		self.type = typee
		self.destroyed = False

		# Add Player to Game

		self.icounter = 0  # invincible counter
		self.name = ''
		self.game = game
		self.score = 0
		self.game.playerentity.add(self)

		# Set Player Velocities

		self.xvel = 0
		self.yvel = 0

		# Set Player Offsets

		self.xoffset = -128
		self.yoffset = 0

		

		# Counters

		self.walkcounter = 0
		self.standcounter = 0

		self.attackcounter = 0
		self.takedamagecounter = 0
		self.counter = 0

		# States
		# abilities

		self.shooting = False
		#background
		self.bg = \
			pygame.image.load('Media/Graphics/Backgrounds/arena.png')
		

		self.projectile = None

		self.collideright = False
		self.faceright = True
		self.takingdamage = False
		self.attacking = False

		self.moving = False

		# Create Player Sprite

		self.image = Surface((19 * 2, 35 * 2), pygame.SRCALPHA)
		self.rect = Rect(0, 0, 19 * 2, 35 * 2)

		# Create Player Detectable Area

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(0, 0, 19 * 2, 35 * 2)
		self.detectable.image = Surface((19 * 2, 35 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		game.detectablegroup.add(self.detectable)

		# Life Meter

		self.lifetotal = [
			'',
			'l',
			'll',
			'lll',
			'llll',
			'lllll',
			'llllll',
			'lllllll',
			'llllllll',
			'lllllllll',
			]
		self.currentlifetotal = 9

		# Inputs

		self.up = False
		self.down = False
		self.right = False
		self.left = False
		self.space = False
		self.cansniper = False
		self.canlaser = False
		self.shootup = False
		self.shootcooldown = 0
		self.shootcooldown2 = 0

	#stats before serilizing and sending/recving via socket

	def __getstate__(self):

		state = self.__dict__.copy()

		surface = state.pop('image')

	   
		surface = state.pop('bg')

		
		surface = state.pop('detectable')

		surface = state.pop('game')

		return state

	def __setstate__(self, state):

	   
		state['bg'] = \
			pygame.image.load('Media/Graphics/Backgrounds/arena.png')

	   
		self.__dict__.update(state)

	def startingposition(self, x, y):
		self.rect = Rect(x, y, 19 * 2, 22 * 2)
		self.detectable.rect = Rect(x, y, 19 * 2, 22 * 2)

	def inputhandler(self):

		for e in pygame.event.get():

			if e.type == QUIT:
				raise SystemExit('QUIT')
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				if self.game.screenfocus == 'Game':
					self.game.screenfocus = 'Pause Menu'
			if e.type == KEYDOWN and e.key == K_UP:
				self.up = True
			if e.type == KEYDOWN and e.key == K_DOWN:
				self.down = True
			if e.type == KEYDOWN and e.key == K_LEFT:
				self.left = True
			if e.type == KEYDOWN and e.key == K_RIGHT:
				self.right = True
			if e.type == KEYDOWN and e.key == K_SPACE \
				and self.destroyed == False:
				self.space = True

			if e.type == KEYDOWN and e.key == K_a and abilityShield \
				== True and self.destroyed == False:
				self.canlaser = True
			if e.type == KEYDOWN and e.key == K_s and abilityShoot \
				== True and self.destroyed == False:
				self.cansniper = True

			if e.type == KEYDOWN and e.key == K_RETURN:
				self.game.pausemenu.createpausemenu()
				self.game.screenfocus = 'Pause Menu'
			if e.type == KEYUP and e.key == K_SPACE:
				self.space = False
			if e.type == KEYUP and e.key == K_UP:
				self.up = False

			if e.type == KEYUP and e.key == K_a:
				self.canlaser = False
			if e.type == KEYUP and e.key == K_s:
				self.cansniper = False

			if e.type == KEYUP and e.key == K_DOWN:
				self.down = False
				self.dancecounter = 0
			if e.type == KEYUP and e.key == K_RIGHT:
				self.right = False
				self.counter = 0
			if e.type == KEYUP and e.key == K_LEFT:
				self.left = False
				self.counter = 0

			pos = pygame.mouse.get_pos()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game.buttongroup['menu'].isOver(pos):

					self.game.screenfocus = 'Pause Menu'
			if e.type == pygame.MOUSEMOTION:
				if self.game.buttongroup['menu'].isOver(pos):

					self.game.buttongroup['menu'].color = (100, 255, 0)
				else:
					self.game.buttongroup['menu'].color = (0, 0, 255)

	def update(self):

		

		global shows, showa
		iscolor = False

		# cooldown counter

		if abilityShoot:
			self.shootcooldown += 1

			if self.shootcooldown >= 30:
				self.shootcooldown = 30
				shows = True
		if abilityShield:
			self.shootcooldown2 += 1

			if self.shootcooldown2 >= 20:
				self.shootcooldown2 = 20
				showa = True

		self.inputhandler()

		# Apply Inputs
		# Move if not taking damage
		if self.up:
			if self.takingdamage == False:
				self.yvel = -13
				self.moving = True

			
		# Move if not taking damage
		if self.down:
			if self.takingdamage == False:
				self.yvel = 13
				self.moving = True

		# Move if not taking damage
		if self.left:
			self.faceright = False
			if self.takingdamage == False:
				self.xvel = -13
				self.moving = True

			# Move if not taking damage

		if self.right:
			self.faceright = True
			if self.takingdamage == False:
				self.xvel = 13
				self.moving = True

		#basic attack
		if self.space:
			if self.up and not (self.right or self.left):
				projectile = Projectile(self, self.game, 'gunup')
				self.shootup = True
			else:

				projectile = Projectile(self, self.game, 'gun')
			self.game.projectilegroup.add(projectile)
			changemusic('gun', False)
			self.space = False
			self.attacking = True
		# special projectile
		if self.canlaser and self.shootcooldown2 >= 20:

			projectile = Projectile(self, self.game, 'laser')
			self.game.projectilegroup.add(projectile)
			projectile = Projectile(self, self.game, 'laserup')
			self.game.projectilegroup.add(projectile)
			projectile = Projectile(self, self.game, 'laserdown')
			self.game.projectilegroup.add(projectile)
			changemusic('laser', False)
			self.canlaser = False
			self.attacking = True
			self.shootcooldown2 = 0
			showa = False
		if self.cansniper and self.shootcooldown >= 30:

		  
			projectile = Projectile(self, self.game, 'sniper')
			self.game.projectilegroup.add(projectile)
			changemusic('m24', False)
			self.shootcooldown = 0

		   
			self.attacking = True
			shows = False

			
	
		#boundries for character
		try:
			color = self.bg.get_at((int(self.detectable.rect.x / 3
								   + self.xvel * 2),
								   int(self.detectable.rect.y / 3
								   + self.yvel * 2)))  # cant move in certain colors
			if color == (185, 122, 87, 255) or color == (136, 0, 21,
					255):

				self.xvel = 0
				self.yvel = 0
		except:

			pass
			# Apply States
		if not (self.left or self.right):
			if not self.takingdamage:

				self.xvel = 0
		if not (self.up or self.down):
			if not self.takingdamage:

				self.yvel = 0
		# Stop player if not taking damage
		if not (self.up or self.down or self.right or self.left):
			if not self.takingdamage:
				self.moving = False

			
		# Move player if taking damage
		if self.takingdamage:
			if self.collideright:
				self.xvel = -5
			else:
				self.xvel = 5

			
		# Stop attacking after 6 updates
		if self.attackcounter > 6:
			self.attacking = False
			self.attackcounter = 0
			self.standcounter = 0
			self.shooting = False
			self.shootup = False

			
		# Player stops taking damage after 14 updates
		if self.takedamagecounter > 14:
			self.takingdamage = False
			self.takedamagecounter = 0

			

		# Increase or Reset Counters

		if self.attacking:
			self.attackcounter = self.attackcounter + 1
		if self.takingdamage:
			self.takedamagecounter = self.takedamagecounter + 1
		if not self.moving:
			self.standcounter = 0

		# Collisions

		self.detectable.rect.left += self.xvel
		self.collide(self.xvel, 0)
		self.detectable.rect.top += self.yvel
		self.onGround = False
		self.collide(0, self.yvel)

		# Offsets

		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(self, xvel, yvel):
		global invincible

		if invincible:
			self.icounter += 1
		if self.icounter >= 100:

			self.icounter = 0
			invincible = False

	

		# Collide Platforms

		for p in self.game.platforms:
			if pygame.sprite.collide_rect(self.detectable, p):
				if xvel > 0:
					self.detectable.rect.right = p.rect.left
				if xvel < 0:
					self.detectable.rect.left = p.rect.right
				if yvel > 0:
					self.detectable.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0
				if yvel < 0:
					self.detectable.rect.top = p.rect.bottom

		# Collide Enemies

		for e in self.game.enemygroup:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable):

				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False

				if not invincible:
					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal - 1

					invincible = True
				elif self.currentlifetotal <= 0:

					if self.game.screenfocus == 'Game':
						self.destroyed = True

						self.game.screenfocus = 'Game Over'
					elif self.game.screenfocus == 'Client':
						self.destroyed = True
					elif self.game.screenfocus == 'Server':

						self.destroyed = True

		# collide projectile

		for e in self.game.projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable) and e.type == 'guu':
				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False
				if not invincible:

					self.game.projectilegroup.remove(e)
					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal \
						- e.damage
					invincible = True

				if self.currentlifetotal <= 0:
					if self.game.screenfocus == 'game':

						self.game.screenfocus = 'Game Over'
					else:
						self.destroyed = True
		for e in self.game.projectilegroupc:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable) and e.type == 'guu':
				leftdifference = self.detectable.rect.right \
					- e.detectable.rect.left
				rightdifference = self.detectable.rect.left \
					- e.detectable.rect.right
				if self.xvel == 0:
					if abs(leftdifference) < 10:
						self.collideright = True
					if abs(rightdifference) < 10:
						self.collideright = False
				if not invincible:

					self.game.projectilegroupc.remove(e)

					self.takingdamage = True
					self.currentlifetotal = self.currentlifetotal \
						- e.damage
					invincible = True

				if self.currentlifetotal <= 0:
					if self.game.screenfocus == 'game':

						self.game.screenfocus = 'Game Over'
					else:
						self.destroyed = True

	def animate(self):

		state = []
		state.append(False)
		state.append(self.moving)
		state.append(self.faceright)
		state.append(self.takingdamage)
		state.append(self.attacking)

		# Moving

		if state[1]:
			if state[0]:
				pass
			else:
				if not self.canlaser:

					if state[2]:
						self.walkloop(walkloopright2)
					else:
						self.walkloop(walkloopleft2)
		else:
			if state[0]:
				pass
			else:

				if state[2]:
					self.standloop(standloopright2)
				else:
					self.standloop(standloopleft2)

		# Attacking

		if state[4] and not self.canlaser:
			if state[0]:
				pass
			else:

				if state[1]:
					if state[2]:
						if self.shootup:
							self.updatecharacter(srunupright1)
						else:

							self.walkloop(shootrightrunloop2)
					else:
						if self.shootup:
							self.updatecharacter(shootupleftrunloop2[0])
						else:

							self.walkloop(shootleftrunloop2)
				else:
					if state[2]:
						if self.shootup:
							self.updatecharacter(srunupright1)
						else:

							self.updatecharacter(shootrightstand2)
					else:
						if self.shootup:
							self.updatecharacter(shootupleftrunloop2[0])
						else:

							self.updatecharacter(shootleftstand2)

		# Hurt

		if state[3]:
			if state[2]:
				self.updatecharacter(takedamageright2)
			else:
				self.updatecharacter(takedamageleft2)

	# Standing Animation Loop

	def standloop(self, loop):
		if self.standcounter == 0 or self.standcounter == 1:
			self.walkcounter = 0
			self.updatecharacter(loop[0])
		elif self.standcounter == 200:
			self.updatecharacter(loop[1])
		elif self.standcounter == 210:
			self.updatecharacter(loop[0])
			self.standcounter = 0
		self.standcounter = self.standcounter + 1

	# Walking Animation Loop

	
	def walkloop(self, loop):
		if self.walkcounter == 0 or self.walkcounter == 1:
			self.standcounter = 0
			self.updatecharacter(loop[1])
		elif self.walkcounter == 5:
			self.updatecharacter(loop[1])
		elif self.walkcounter == 10:
			self.updatecharacter(loop[2])
		elif self.walkcounter == 15:
			self.updatecharacter(loop[3])
		elif self.walkcounter == 20:
			self.updatecharacter(loop[4])
		elif self.walkcounter == 25:
			self.updatecharacter(loop[5])
		elif self.walkcounter == 30:
			self.updatecharacter(loop[6])
		elif self.walkcounter == 35:
			self.updatecharacter(loop[7])
		elif self.walkcounter == 40:
			self.updatecharacter(loop[8])
		elif self.walkcounter == 45:
			self.updatecharacter(loop[9])
		elif self.walkcounter == 50:
			self.updatecharacter(loop[10])
		elif self.walkcounter == 55:
			self.updatecharacter(loop[11])
		elif self.walkcounter == 60:
			self.updatecharacter(loop[12])
		elif self.walkcounter == 65:
			self.updatecharacter(loop[1])
			self.walkcounter = 5

		self.walkcounter = self.walkcounter + 5

	# Update Current Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class Projectile(Entity):

	def __init__(
		self,
		player,
		game,
		typee='guu',
		):

		Entity.__init__(self)

		self.xvel = 15
		self.type = typee
		self.prange = 500
		self.game = game

		for p in self.game.playerentity:
			self.pxl = p
		#player position 
		self.px = self.pxl.detectable.rect.x
		self.py = self.pxl.detectable.rect.y

		self.damage = 1
		self.xoffset = 0

		#setting stats according to type
		if typee == 'sword':
			self.xvel = 0
			self.prange = 2
			self.damage = 9
			self.killcounter = 0
		if typee == 'gun':
			self.xvel = 30
			self.prange = 500
			self.damage = 1
			self.xoffset = 0
		if typee == 'laser':
			self.xvel = 25
			self.prange = 500
			self.damage = 1
			self.xoffset = 0
		if typee == 'laserup':
			self.yvel = 25
			self.prange = 500
			self.damage = 1
			self.xoffset = 0
		if typee == 'gunup':
			self.yvel = 25
			self.prange = 500
			self.damage = 1
			self.xoffset = 0

		if typee == 'laserdown':
			self.yvel = 25
			self.prange = 500
			self.damage = 1
			self.xoffset = 0

		if typee == 'sniper':
			self.xvel = 55
			self.prange = 1000
			self.damage = 9

		if typee == 'arrow':
			self.xvel = 40
			self.type = typee
			self.prange = 500

			self.damage = 1
		if typee == 'shield':
			self.xvel = 0
			self.prange = 2
			self.damage = 4
			self.killcounter = 0
		if typee == 'guu':
			self.xvel = 20
			self.prange = 400
			self.damage = 1
			self.xoffset = 0
			self.image = noimage

		self.detectable = pygame.sprite.Sprite()

		# Place Projectile Facing Right5 and according to type

		if player.faceright == True:

		

			self.xvel = self.xvel

			if typee == 'gun':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 100
				y = player.detectable.rect.top + 18

				if player.moving:
					x += 60

				self.image = bustershot1

				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x + 50, y, 10 * 2, 10 * 2)
				self.detectable.rect.x = self.rect.x + 15
				self.detectable.rect.y = self.rect.y + 5
			if typee == 'laser':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 100
				y = player.detectable.rect.top + 18

				self.image = bustershotlaser
				if player.moving:
					x += 60

				self.detectable.rect = Rect(x, y, 30 * 2, 10 * 2)
				self.detectable.image = Surface((30 * 2, 10 * 2))
				self.rect = Rect(x + 50, y, 30 * 2, 10 * 2)
				self.detectable.rect.x = self.rect.x + 35
				self.detectable.rect.y = self.rect.y + 0

			if typee == 'laserup' or typee == 'laserdown':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 100
				y = player.detectable.rect.top + 18
				self.image = bustershotlaserup
				if player.moving:
					x += 60

				self.detectable.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.image = Surface((10 * 2, 35 * 2))
				self.rect = Rect(x + 50, y, 10 * 2, 35 * 2)
				self.detectable.rect.x = self.rect.x + 45
				self.detectable.rect.y = self.rect.y + 0

			if typee == 'gunup':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 140
				y = player.detectable.rect.top + 18
				self.image = bustershotup
				if player.moving:
					x += 60

				self.detectable.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.image = Surface((10 * 2, 35 * 2))
				self.rect = Rect(x + 50, y, 10 * 2, 35 * 2)
				self.detectable.rect.x = self.rect.x + 45
				self.detectable.rect.y = self.rect.y + 0

			if typee == 'sniper':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 100
				y = player.detectable.rect.top + 18

				if player.moving:
					x += 60

				self.image = bustershotm24

				self.detectable.rect = Rect(x, y, 30 * 2, 25 * 2)
				self.detectable.image = Surface((30 * 2, 25 * 2))
				self.rect = Rect(x + 50, y, 30 * 2, 25 * 2)

				self.detectable.rect.x = self.rect.x + 20
				self.detectable.rect.y = self.rect.y + 5

			if typee == 'sword':

				x = player.detectable.rect.left + 10
				y = player.detectable.rect.top - 10

				self.detectable.image = Surface((110, 70))
				if player.walkcounter > 0:
					self.detectable.image = Surface((130, 70))
				self.image = noimage

				self.rect = self.detectable.rect = Rect(x, y, 110, 70)

			if typee == 'arrow':

				x = player.detectable.rect.right - 50
				y = player.detectable.rect.top + 18

				if player.moving:
					x += 60
					player.moving = False

				self.image = pygame.transform.flip(arrow2, True, False)
				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x, y, 10 * 2, 10 * 2)

				# offset

				self.detectable.rect.x = self.detectable.rect.x + 65

			if typee == 'shield':
				x = player.detectable.rect.right - 2
				y = player.detectable.rect.top - 5
				self.detectable.image = Surface((20, 50))
				self.rect = Rect(x, y, 20, 50)
				self.detectable.rect = Rect(x, y, 20, 50)
				self.image = noimage  # no image

				self.detectable.image = Surface((20, 50))

			if self.type == 'guu':
				self.xvel = self.xvel * -1

				x = player.detectable.rect.left - 0
				y = player.detectable.rect.top + 18
				self.image = guu
				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x, y, 10 * 2, 10 * 2)
		else:

		# Place Projectile Facing Left

			self.xvel = self.xvel * -1

			if typee == 'gun':
				x = player.detectable.rect.left - 70
				y = player.detectable.rect.top + 18

				if player.moving:
					x -= 60

				self.image = pygame.transform.flip(bustershot1, True,
						False)

				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x + 50, y, 10 * 2, 10 * 2)

				self.detectable.rect.x = self.rect.x + 60
				self.detectable.rect.y = self.rect.y + 5
			if typee == 'laser':
				x = player.detectable.rect.left - 70
				y = player.detectable.rect.top + 18
				if player.moving:
					x -= 60

				self.image = bustershotlaser

				self.detectable.rect = Rect(x, y, 30 * 2, 10 * 2)
				self.detectable.image = Surface((30 * 2, 10 * 2))
				self.rect = Rect(x, y, 30 * 2, 10 * 2)

				self.detectable.rect.x = self.rect.x + 40
				self.detectable.rect.y = self.rect.y + 0
			if typee == 'laserup' or typee == 'laserdown':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 100
				y = player.detectable.rect.top + 18
				if player.moving:
					x -= 60

				self.image = bustershotlaserup

				self.detectable.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.image = Surface((10 * 2, 35 * 2))
				self.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.rect.x = self.rect.x + 45
				self.detectable.rect.y = self.rect.y + 0

			if typee == 'gunup':
				self.xvel = self.xvel

				x = player.detectable.rect.right - 40
				y = player.detectable.rect.top + 18
				if player.moving:
					x -= 60

				self.image = bustershotup

				self.detectable.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.image = Surface((10 * 2, 35 * 2))
				self.rect = Rect(x, y, 10 * 2, 35 * 2)
				self.detectable.rect.x = self.rect.x + 45
				self.detectable.rect.y = self.rect.y + 0

			if typee == 'sniper':
				x = player.detectable.rect.left - 70
				y = player.detectable.rect.top + 18
				if player.moving:
					x -= 60

				self.image = pygame.transform.flip(bustershotm24, True,
						False)

				self.detectable.rect = Rect(x, y, 30 * 2, 25 * 2)
				self.detectable.image = Surface((30 * 2, 25 * 2))
				self.rect = Rect(x + 50, y, 30 * 2, 25 * 2)

				self.detectable.rect.x = self.rect.x + 20
				self.detectable.rect.y = self.rect.y + 5

			if typee == 'sword':
				x = player.detectable.rect.left - 90

				y = player.detectable.rect.top - 10
				self.detectable.image = Surface((110, 70))
				if player.walkcounter > 0:
					self.detectable.image = Surface((130, 70))
				self.image = noimage

				self.rect = self.detectable.rect = Rect(x, y, 110, 70)

			if typee == 'shield':
				x = player.detectable.rect.left - 7
				y = player.detectable.rect.top - 5
				self.detectable.image = Surface((20, 50))
				self.rect = Rect(x, y, 20, 50)
				self.detectable.rect = Rect(x, y, 20, 50)
				self.image = noimage  # no image
				self.detectable.image = Surface((20, 50))

			if typee == 'arrow':
				x = player.detectable.rect.left - 50
				y = player.detectable.rect.top + 18
				if player.moving:
					x -= 60
					player.moving = False

				self.image = pygame.transform.flip(arrow1, True, False)
				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x, y, 10 * 2, 10 * 2)

				# offset

				self.detectable.rect.x = self.detectable.rect.x + 60
			if self.type == 'guu':

				x = player.detectable.rect.left - 0
				y = player.detectable.rect.top + 18
				self.image = guu

				self.detectable.rect = Rect(x, y, 10 * 2, 10 * 2)
				self.detectable.image = Surface((10 * 2, 10 * 2))
				self.rect = Rect(x, y, 10 * 2, 10 * 2)

				# offset

				self.detectable.rect.x = self.detectable.rect.x + 60

		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		game.detectablegroup.add(self.detectable)
		self.image = pygame.transform.scale(self.image, (96, 96))
		self.image.convert()

	def update(self, platforms):

	  
		#moving projectiles up
		if self.type == 'laserup' or self.type == 'gunup':
			self.rect.y -= self.yvel
			self.detectable.rect.y -= self.yvel
			self.prange -= self.yvel
			if self.prange <= 0:
				self.kill()
		#moving projectiles down
		elif self.type == 'laserdown':
			self.rect.y += self.yvel
			self.detectable.rect.y += self.yvel
			self.prange -= self.yvel
			if self.prange <= 0:
				self.kill()
		#moving projectiles
		elif not self.type == 'guu':

			self.rect.left += self.xvel
			self.detectable.rect.left += self.xvel

			# removing projectile once range is gone

			if self.xvel > 0:
				self.prange -= self.xvel
				if self.prange <= 0:
					self.kill()
			elif self.xvel <= 0:
				self.prange += self.xvel  # self.xvel already in negative
				if self.prange <= 0:
					self.kill()
		else:
			if self.xvel > 0:
				self.prange -= self.xvel
				if self.prange <= 0:
					self.kill()
			elif self.xvel <= 0:
				self.prange += self.xvel  # self.xvel already in negative
				if self.prange <= 0:
					self.kill()

			#homing projectiles following player
			if self.detectable.rect.x < self.px:
				self.detectable.rect.x -= self.xvel
				if self.detectable.rect.x > self.px:
					self.detectable.rect.x = self.px
			elif self.detectable.rect.x > self.px:
				self.detectable.rect.x += self.xvel
				if self.detectable.rect.x < self.px:
					self.detectable.rect.x = self.px
			if self.detectable.rect.y < self.py:
				self.detectable.rect.y -= self.xvel
				if self.detectable.rect.y > self.py:
					self.detectable.rect.y = self.py
			elif self.detectable.rect.y > self.py:
				self.detectable.rect.y += self.xvel
				if self.detectable.rect.y < self.py:
					self.detectable.rect.y = self.py
			if self.detectable.rect.x == self.px \
				and self.detectable.rect.y == self.py:
				self.kill()

			self.rect.x = self.detectable.rect.x + self.xoffset
			self.rect.y = self.detectable.rect.y
		if self.type == 'sword' or self.type == 'shield':
			if self.killcounter > 10:

				self.kill()
			else:

				self.killcounter += 1

		#collision
		self.collide(platforms)

	def collide(self, platforms):
		for p in platforms:
			if pygame.sprite.collide_rect(self.detectable, p):
				self.kill()
		for e in self.game.projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					e.detectable) and self.type == 'guu' and e.type \
				== 'shield':
				self.kill()


class Rooms(object):

	def __init__(self, game, player):
		self.width = 0
		self.height = 0
		self.game = game
		self.player = player

		self.createroom1('a')

	def dumpsprites(self):

		self.game.enemygroup.empty()
		self.game.entities.empty()

		self.game.platforms = []

	def resetcamera(self):
		total_level_width = self.width * 3
		total_level_height = self.height * 3
		self.game.camera = Camera(complex_camera, total_level_width,
								  total_level_height)
		self.game.camerafocus = self.player.detectable

	def setbackground(self, backgroundpath):
		self.dumpsprites()
		bg = Entity()

		bg.image = pygame.image.load(backgroundpath)
		self.width = bg.image.get_width()
		self.height = bg.image.get_height()

		bg.rect = Rect(0, 0, self.width * 3, self.height * 3)
		bg.image = pygame.transform.scale(bg.image, (self.width * 3,
				self.height * 3))

	   
		self.game.entities.add(bg)

		self.resetcamera()

	def createroom1(self, entrance):

	   
		if not musicplaying == 'lavender':
			changemusic('lavender', True)

	  

		# creating buttons

		self.game.buttongroup['menu'] = button(
			(0, 0, 255),
			820,
			5,
			120,
			50,
			'Menu',
			)
		self.game.buttongroup['resume'] = button(
			(0, 0, 255),
			400,
			300,
			150,
			50,
			'resume',
			)
		self.game.buttongroup['exit'] = button(
			(255, 0, 0),
			400,
			600,
			150,
			50,
			'exit',
			)
		self.game.buttongroup['restart'] = button(
			(255, 0, 0),
			400,
			300,
			180,
			50,
			'restart',
			)
		self.game.buttongroup['highscore'] = button(
			(0, 255, 0),
			400,
			500,
			200,
			50,
			'highscore',
			)
		self.game.buttongroup['mhighscore'] = button(
			(0, 255, 0),
			400,
			600,
			350,
			50,
			'Multiplayer score',
			)
		self.game.buttongroup['back'] = button(
			(0, 255, 0),
			400,
			500,
			180,
			50,
			'back',
			)

		self.game.buttongroup['start'] = button(
			(0, 200, 0),
			400,
			300,
			200,
			50,
			'start',
			)
		self.game.buttongroup['multiplayer'] = button(
			(200, 200, 0),
			400,
			400,
			250,
			50,
			'multiplayer',
			)
		self.game.buttongroup['host'] = button(
			(0, 255, 0),
			400,
			300,
			200,
			50,
			'host',
			)
		self.game.buttongroup['connect'] = button(
			(255, 0, 0),
			400,
			400,
			200,
			50,
			'connect',
			)

		self.game.buttongroup['shop'] = button(
			(255, 0, 0),
			400,
			400,
			200,
			50,
			'shop',
			)
		self.game.buttongroup['ability1'] = button(
			(255, 0, 0),
			200,
			230,
			150,
			50,
			'ability1',
			)
		self.game.buttongroup['ability2'] = button(
			(255, 0, 0),
			500,
			230,
			150,
			50,
			'ability2',
			)
		self.game.buttongroup['heart'] = button(
			(255, 0, 0),
			200,
			350,
			150,
			50,
			'heart',
			)

		self.game.buttongroup['gladiator'] = button(
			(255, 0, 0),
			200,
			350,
			150,
			150,
			' ',
			)
		self.game.buttongroup['gunner'] = button(
			(255, 0, 0),
			500,
			350,
			150,
			150,
			' ',
			)
		#setting background
		self.setbackground('Media/Graphics/Backgrounds/arena.png')

	

		bg = pygame.image.load('Media/Graphics/Backgrounds/arena.png')

		#setting boundary where player move or cannot move
		i = 1
		j = 1
		while i < bg.get_width():
			j = 1
			while j < bg.get_height():
				color = bg.get_at((i, j))

				if color == (185, 122, 87, 255):
					self.game.platforms.append(Platform(i, j, 10, 10))

				j += 10

			i += 10

		# Set Up Player

		if entrance == 'a':
			self.player.startingposition(520 * 3, 258 * 3)

		# Set Up Enemies

		# Set Up Platforms

		self.game.platforms.append(Platform(506, 24, 158, 39))
		self.game.platforms.append(Platform(506, 577, 158, 39))
		self.game.platforms.append(Platform(1000, 255, 30, 67))
		self.game.platforms.append(Platform(118, 274, 33, 61))



class Camera(object):

	def __init__(
		self,
		camera_func,
		width,
		height,
		):
		self.camera_func = camera_func
		self.state = Rect(0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)


def simple_camera(camera, target_rect):
	(l, t, _, _) = target_rect
	(_, _, w, h) = camera
	return Rect(-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)


def complex_camera(camera, target_rect):
	(l, t, _, _) = target_rect
	(_, _, w, h) = camera
	(l, t, _, _) = (-l + HALF_WIDTH, -t + HALF_HEIGHT, w, h)

	l = min(0, l)  # stop scrolling at the left edge
	l = max(-(camera.width - WIN_WIDTH), l)  # stop scrolling at the right edge
	t = max(-(camera.height - WIN_HEIGHT), t)  # stop scrolling at the bottom
	t = min(0, t)  # stop scrolling at the top
	return Rect(l, t, w, h)


class zombie(Entity):

	def __init__(
		self,
		x,
		y,
		player,
		id,
		xvel=2,
		typee='zombie',
		):
		Entity.__init__(self)
		self.collideright = True

		

		x = x * 3
		y = y * 3

		self.type = typee

		self.player = player
		# Set id
		self.id = id
		self.currentlifetotal = 1

		# Set Velocities
		self.xvel = xvel
		self.temp = xvel
		self.yvel = xvel

		# States

		self.destroyed = False
		self.faceright = False
		self.onGround = False

		# Offests

		self.xoffset = 0
		self.yoffset = 0

		# Counter

		self.counter = 0

		# Create Sprite Image
	   
		self.image = zombiewalk1
		self.rect = Rect(x, y, 27 * 2, 35 * 2)

		# Create Dectectable

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(x, y, 27 * 2, 35 * 2)
		self.detectable.image = Surface((27 * 2, 35 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		player.game.detectablegroup.add(self.detectable)

	def __getstate__(self):

		state = self.__dict__.copy()

		surface = state.pop('image')

	  
		surface = state.pop('player')

		return state

	def __setstate__(self, state):

		# surface_string, size = state.pop("surface_stringa")

		state['image'] = zombiewalk1

		self.__dict__.update(state)

	def update(self, platforms, projectilegroup):

		# Move according to player position

		if self.xvel > 0:
			self.faceright = True
		if self.xvel < 0:
			self.faceright = False

	   
		if self.detectable.rect.x < self.player.detectable.rect.x:
			self.xvel = self.temp

			self.faceright = False
		if self.detectable.rect.y < self.player.detectable.rect.y:
			self.yvel = self.temp

		if self.detectable.rect.x > self.player.detectable.rect.x:
			self.xvel = self.temp * -1

			self.faceright = True
		if self.detectable.rect.y > self.player.detectable.rect.y:
			self.yvel = self.temp * -1

		if self.detectable.rect.x == self.player.detectable.rect.x:
			self.xvel = 0
		if self.detectable.rect.y == self.player.detectable.rect.y:
			self.yvel = 0

		# Collisions

		self.collide(self.xvel, self.yvel, platforms, projectilegroup)
		self.detectable.rect.x += self.xvel
		self.detectable.rect.y += self.yvel
		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(
		self,
		xvel,
		yvel,
		platforms,
		projectilegroup,
		player=None,
		):
		global enemyid, renemyid

	   
		# Collide Projectiles

		for j in projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					j.detectable) and not self.destroyed \
				and not (j.type == 'shield' or j.type == 'guu'):

				self.currentlifetotal -= j.damage
				projectilegroup.remove(j)
				changemusic('hit', False)
				if self.currentlifetotal <= 0:

					self.destroyed = True
					if not enemyid == self.id:
						self.player.score += 5
					self.counter = 0
					self.xvel = 0

					if player == None:
						self.player.game.enemygroup.remove(self)
					else:
						if player.game.screenfocus == 'Client':
							enemyid = self.id

			if pygame.sprite.collide_rect(self.detectable, j) \
				and not self.destroyed and j.type == 'shield':
				self.xvel = 0

		for p in self.player.game.enemygroup:

			if pygame.sprite.collide_rect(self.detectable,
					p.detectable) and not p.id == self.id:
				if xvel > 0:
					if self.rect.right >= p.rect.left \
						and self.rect.right < p.rect.right:
						self.xvel = 0

				if xvel < 0:
					if self.rect.left <= p.rect.right \
						and self.rect.left > p.rect.left:
						self.xvel = 0

				if yvel > 0:
					if self.rect.bottom >= p.rect.top \
						and self.rect.bottom < p.rect.bottom:
						self.yvel = 0

	# Animate

	def animate(self):
		pass
		if self.destroyed == True:
			pass
		else:

			self.walkloop(zombiewalkloop)

	# Walk Loop Animation

	def walkloop(self, loop):
		if self.counter <= 10:
			self.updatecharacter(loop[0])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[0],
						True, False))
		elif self.counter <= 20:
			self.updatecharacter(loop[1])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[1],
						True, False))
		elif self.counter <= 30:

			self.updatecharacter(loop[2])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[2],
						True, False))
		elif self.counter <= 40:

			self.updatecharacter(loop[3])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[3],
						True, False))
		elif self.counter <= 50:

			self.updatecharacter(loop[4])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[4],
						True, False))
		elif self.counter <= 60:

			self.updatecharacter(loop[5])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[5],
						True, False))
		elif self.counter <= 70:

			self.updatecharacter(loop[6])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[6],
						True, False))
		elif self.counter <= 80:

			self.updatecharacter(loop[7])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[7],
						True, False))
		elif self.counter <= 90:

			self.updatecharacter(loop[8])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[8],
						True, False))
		elif self.counter <= 100:

			self.updatecharacter(loop[9])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[9],
						True, False))
			self.counter = 0

		self.counter = self.counter + 5

	# Destroy Loop Animation

	def destroyloop(self, loop):
		if self.counter == 0:
			self.yoffset = -30
			self.updatecharacter(loop[0])
		elif self.counter == 5:
			self.updatecharacter(loop[1])
		elif self.counter == 10:
			self.updatecharacter(loop[2])
		elif self.counter == 15:
			self.updatecharacter(loop[3])
		elif self.counter == 20:
			self.updatecharacter(loop[4])
		elif self.counter == 25:
			self.updatecharacter(loop[5])
		elif self.counter == 30:
			self.updatecharacter(loop[6])
		elif self.counter == 35:
			self.updatecharacter(loop[7])
		elif self.counter == 40:
			self.updatecharacter(loop[8])
		elif self.counter == 45:
			self.updatecharacter(loop[9])
		elif self.counter == 50:
			self.updatecharacter(loop[10])
		elif self.counter == 55:
			self.updatecharacter(loop[11])
		elif self.counter == 60:
			self.kill()
			self.counter = 0
		self.counter = self.counter + 20

	# Update Animation Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class zombieBoss(Entity):

	def __init__(
		self,
		x,
		y,
		player,
		id,
		xvel=2,
		typee='zombieBoss',
		):
		Entity.__init__(self)
		self.collideright = True

		

		x = x * 3
		y = y * 3

		self.type = typee
		self.currentlifetotal = 9

		self.l = 0

		self.player = player
		self.id = id

		# Set Velocities
		self.xvel = xvel
		self.temp = xvel
		self.yvel = xvel

		# States

		self.destroyed = False
		self.faceright = False
		self.onGround = False

		# Offests

		self.xoffset = 0
		self.yoffset = 0

		# Counter

		self.counter = 0

		# Create Sprite Image
	   
		self.image = zombieBosswalk1
		self.rect = Rect(x, y, 39 * 2, 47 * 2)

		# Create Dectectable

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(x, y, 39 * 2, 47 * 2)
		self.detectable.image = Surface((39 * 2, 47 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		player.game.detectablegroup.add(self.detectable)

	def __getstate__(self):

		state = self.__dict__.copy()

		surface = state.pop('image')

	  

		surface = state.pop('player')

		return state

	def __setstate__(self, state):

		self.__dict__.update(state)

	def update(self, platforms, projectilegroup):

		# gets faster randomly

		rand = random.randint(1, 10)

		# Move according to player position

		if self.xvel > 0:
			self.faceright = True
		if self.xvel < 0:
			self.faceright = False

		
		if self.detectable.rect.x < self.player.detectable.rect.x:
			self.xvel = self.temp

			self.faceright = False
		if self.detectable.rect.y < self.player.detectable.rect.y:
			self.yvel = self.temp

		if self.detectable.rect.x > self.player.detectable.rect.x:
			self.xvel = self.temp * -1

			self.faceright = True
		if self.detectable.rect.y > self.player.detectable.rect.y:
			self.yvel = self.temp * -1

		if self.detectable.rect.x == self.player.detectable.rect.x:
			self.xvel = 0
		if self.detectable.rect.y == self.player.detectable.rect.y:
			self.yvel = 0

		if rand == 5:

			self.xvel = self.xvel * 20
			self.yvel = self.yvel * 20

	  
		# Collisions

		self.collide(self.xvel, self.yvel, platforms, projectilegroup)
		self.detectable.rect.x += self.xvel
		self.detectable.rect.y += self.yvel
		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(
		self,
		xvel,
		yvel,
		platforms,
		projectilegroup,
		player=None,
		):
		global enemyid

	 

		# Collide Projectiles

		for j in projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					j.detectable) and not self.destroyed \
				and not (j.type == 'shield' or j.type == 'guu'):

				projectilegroup.remove(j)
				self.currentlifetotal -= j.damage

				changemusic('hit', False)
				if self.currentlifetotal <= 0:
					self.destroyed = True

					if not enemyid == self.id:
						self.player.score += 20
					self.xvel = 0
					self.counter = 0

					if player == None:
						self.player.game.enemygroup.remove(self)
					else:
						if player.game.screenfocus == 'Client':
							enemyid = self.id

			if pygame.sprite.collide_rect(self.detectable, j) \
				and not self.destroyed and j.type == 'shield':
				self.xvel = 0
		for p in self.player.game.enemygroup:

			if pygame.sprite.collide_rect(self.detectable,
					p.detectable) and not p.id == self.id:
				if xvel > 0:
					if self.rect.right >= p.rect.left \
						and self.rect.right < p.rect.right:
						self.xvel = 0

				if xvel < 0:
					if self.rect.left <= p.rect.right \
						and self.rect.left > p.rect.left:
						self.xvel = 0

				if yvel > 0:
					if self.rect.bottom >= p.rect.top \
						and self.rect.bottom < p.rect.bottom:
						self.yvel = 0

	# Animate

	def animate(self):
		pass
		if self.destroyed == True:
			pass
		else:
			self.walkloop(zombieBosswalkloop)

	# Walk Loop Animation

	def walkloop(self, loop):
		if self.counter <= 10:
			self.l = 0
			self.updatecharacter(loop[0])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[0],
						True, False))
		elif self.counter <= 20:
			self.l = 1
			self.updatecharacter(loop[1])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[1],
						True, False))
		elif self.counter <= 30:

			self.l = 2
			self.updatecharacter(loop[2])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[2],
						True, False))
		elif self.counter <= 40:

			self.l = 3
			self.updatecharacter(loop[3])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[3],
						True, False))
		elif self.counter <= 50:

			self.l = 4
			self.updatecharacter(loop[4])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[4],
						True, False))
		elif self.counter <= 60 or self.counter >= 60:

			self.l = 0
			self.updatecharacter(loop[5])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[5],
						True, False))
			self.counter = 0

		self.counter = self.counter + 5

	# Destroy Loop Animation

	def destroyloop(self, loop):
		if self.counter == 0:
			self.yoffset = -30
			self.updatecharacter(loop[0])
		elif self.counter == 5:
			self.updatecharacter(loop[1])
		elif self.counter == 10:
			self.updatecharacter(loop[2])
		elif self.counter == 15:
			self.updatecharacter(loop[3])
		elif self.counter == 20:
			self.updatecharacter(loop[4])
		elif self.counter == 25:
			self.updatecharacter(loop[5])
		elif self.counter == 30:
			self.updatecharacter(loop[6])
		elif self.counter == 35:
			self.updatecharacter(loop[7])
		elif self.counter == 40:
			self.updatecharacter(loop[8])
		elif self.counter == 45:
			self.updatecharacter(loop[9])
		elif self.counter == 50:
			self.updatecharacter(loop[10])
		elif self.counter == 55:
			self.updatecharacter(loop[11])
		elif self.counter == 60:
			self.kill()
			self.counter = 0
		self.counter = self.counter + 20

	# Update Animation Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class zombieGirl(Entity):

	def __init__(
		self,
		x,
		y,
		player,
		id,
		xvel=2,
		typee='zombieGirl',
		):
		Entity.__init__(self)
		self.collideright = True

		

		x = x * 3
		y = y * 3

		self.currentlifetotal = 1

		self.type = typee

		self.player = player
		self.id = id

		self.xvel = xvel
		self.temp = xvel
		self.yvel = 0

		# States

		self.destroyed = False
		self.faceright = False
		self.onGround = False

		# Offests

		self.xoffset = 0
		self.yoffset = 0

		# Counter

		self.counter = 0

		# Create Sprite Image
	  
		self.image = zombieGirlwalk1
		self.rect = Rect(x, y, 27 * 2, 35 * 2)

		# Create Dectectable

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(x, y, 27 * 2, 35 * 2)
		self.detectable.image = Surface((27 * 2, 35 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		player.game.detectablegroup.add(self.detectable)

	def __getstate__(self):

		state = self.__dict__.copy()

		surface = state.pop('image')

	   

		surface = state.pop('player')

		return state

	def __setstate__(self, state):

		
		state['image'] = zombieGirlwalk1

	   
		self.__dict__.update(state)

	def update(self, platforms, projectilegroup):

		# Move # Move according to player position

		if self.xvel > 0:
			self.faceright = True
		if self.xvel < 0:
			self.faceright = False


		if self.detectable.rect.x < self.player.detectable.rect.x:
			self.xvel = self.temp

			self.faceright = False
		if self.detectable.rect.y < self.player.detectable.rect.y:
			self.yvel = self.temp

		if self.detectable.rect.x > self.player.detectable.rect.x:
			self.xvel = self.temp * -1

			self.faceright = True
		if self.detectable.rect.y > self.player.detectable.rect.y:
			self.yvel = self.temp * -1

		if self.detectable.rect.x == self.player.detectable.rect.x:
			self.xvel = 0
		if self.detectable.rect.y == self.player.detectable.rect.y:
			self.yvel = 0

	
		# Collisions

		self.collide(self.xvel, self.yvel, platforms, projectilegroup)
		self.detectable.rect.x += self.xvel
		self.detectable.rect.y += self.yvel
		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(
		self,
		xvel,
		yvel,
		platforms,
		projectilegroup,
		player=None,
		):
		global enemyid

	  
		# Collide Projectiles

		for j in projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					j.detectable) and not self.destroyed \
				and not (j.type == 'shield' or j.type == 'guu'):

				self.currentlifetotal -= j.damage

				projectilegroup.remove(j)
				changemusic('hit', False)
				if self.currentlifetotal <= 0:

					self.destroyed = True
					if not enemyid == self.id:
						self.player.score += 5
					self.counter = 0
					self.xvel = 0

					if player == None:
						self.player.game.enemygroup.remove(self)
					else:
						if player.game.screenfocus == 'Client':
							enemyid = self.id

			if pygame.sprite.collide_rect(self.detectable, j) \
				and not self.destroyed and j.type == 'shield':
				self.xvel = 0
		for p in self.player.game.enemygroup:

			if pygame.sprite.collide_rect(self.detectable,
					p.detectable) and not p.id == self.id:
				if xvel > 0:
					if self.rect.right >= p.rect.left \
						and self.rect.right < p.rect.right:
						self.xvel = 0

				if xvel < 0:
					if self.rect.left <= p.rect.right \
						and self.rect.left > p.rect.left:
						self.xvel = 0

				if yvel > 0:
					if self.rect.bottom >= p.rect.top \
						and self.rect.bottom < p.rect.bottom:
						self.yvel = 0

	# Animate

	def animate(self):
		pass
		if self.destroyed == True:
			pass
		else:
			self.walkloop(zombieGirlwalkloop)

	# Walk Loop Animation

	def walkloop(self, loop):
		if self.counter <= 10:
			self.updatecharacter(loop[0])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[0],
						True, False))
		elif self.counter <= 20:
			self.updatecharacter(loop[1])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[1],
						True, False))
		elif self.counter <= 30:

			self.updatecharacter(loop[2])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[2],
						True, False))
		elif self.counter <= 40:

			self.updatecharacter(loop[3])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[3],
						True, False))
		elif self.counter <= 50:

			self.updatecharacter(loop[4])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[4],
						True, False))
		elif self.counter <= 60:

			self.updatecharacter(loop[5])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[5],
						True, False))
		elif self.counter <= 70:

			self.updatecharacter(loop[6])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[6],
						True, False))
		elif self.counter <= 80:

			self.updatecharacter(loop[7])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[7],
						True, False))
		elif self.counter <= 90:

			self.updatecharacter(loop[8])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[8],
						True, False))
		elif self.counter <= 100:

			self.updatecharacter(loop[9])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[9],
						True, False))
			self.counter = 0

		self.counter = self.counter + 5

	# Destroy Loop Animation

	def destroyloop(self, loop):
		if self.counter == 0:
			self.yoffset = -30
			self.updatecharacter(loop[0])
		elif self.counter == 5:
			self.updatecharacter(loop[1])
		elif self.counter == 10:
			self.updatecharacter(loop[2])
		elif self.counter == 15:
			self.updatecharacter(loop[3])
		elif self.counter == 20:
			self.updatecharacter(loop[4])
		elif self.counter == 25:
			self.updatecharacter(loop[5])
		elif self.counter == 30:
			self.updatecharacter(loop[6])
		elif self.counter == 35:
			self.updatecharacter(loop[7])
		elif self.counter == 40:
			self.updatecharacter(loop[8])
		elif self.counter == 45:
			self.updatecharacter(loop[9])
		elif self.counter == 50:
			self.updatecharacter(loop[10])
		elif self.counter == 55:
			self.updatecharacter(loop[11])
		elif self.counter == 60:
			self.kill()
			self.counter = 0
		self.counter = self.counter + 20

	# Update Animation Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class zombieRunner(Entity):

	def __init__(
		self,
		x,
		y,
		player,
		id,
		xvel=4,
		typee='zombieRunner',
		):
		Entity.__init__(self)
		self.collideright = True

		# Set Velocities

		x = x * 3
		y = y * 3
		if xvel <= 2:
			xvel = 3
		elif xvel >= 10:
			xvel = 9

		self.type = typee

		self.player = player
		self.id = id
		self.currentlifetotal = 1

		self.xvel = xvel
		self.temp = xvel
		self.yvel = 0

		# States

		self.destroyed = False
		self.faceright = False
		self.onGround = False

		# Offests

		self.xoffset = 0
		self.yoffset = 0

		# Counter

		self.counter = 0

		# Create Sprite Image
	   
		self.image = zombieRunnerwalk1
		self.rect = Rect(x, y, 30 * 2, 35 * 2)

		# Create Dectectable

		self.detectable = pygame.sprite.Sprite()
		self.detectable.rect = Rect(x, y, 30 * 2, 35 * 2)
		self.detectable.image = Surface((30 * 2, 35 * 2))
		self.detectable.image.fill(Color('#0033FF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		player.game.detectablegroup.add(self.detectable)

	def __getstate__(self):

		state = self.__dict__.copy()

		surface = state.pop('image')

		surface = state.pop('player')

		return state

	def __setstate__(self, state):



		state['image'] = zombieRunnerwalk1

		self.__dict__.update(state)

	def update(self, platforms, projectilegroup):

		# Move # Move according to player position

		if self.xvel > 0:
			self.faceright = True
		if self.xvel < 0:
			self.faceright = False

	   
		if self.detectable.rect.x < self.player.detectable.rect.x:
			self.xvel = self.temp

			self.faceright = False
		if self.detectable.rect.y < self.player.detectable.rect.y:
			self.yvel = self.temp

		if self.detectable.rect.x > self.player.detectable.rect.x:
			self.xvel = self.temp * -1

			self.faceright = True
		if self.detectable.rect.y > self.player.detectable.rect.y:
			self.yvel = self.temp * -1

		if self.detectable.rect.x == self.player.detectable.rect.x:
			self.xvel = 0
		if self.detectable.rect.y == self.player.detectable.rect.y:
			self.yvel = 0

	
		# Collisions

		self.collide(self.xvel, self.yvel, platforms, projectilegroup)
		self.detectable.rect.x += self.xvel
		self.detectable.rect.y += self.yvel
		self.rect.x = self.detectable.rect.x + self.xoffset
		self.rect.y = self.detectable.rect.y + self.yoffset

		# Animate

		self.animate()

	def collide(
		self,
		xvel,
		yvel,
		platforms,
		projectilegroup,
		player=None,
		):
		global enemyid

	   
		# Collide Projectiles

		for j in projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					j.detectable) and not self.destroyed \
				and not (j.type == 'shield' or j.type == 'guu'):

				self.currentlifetotal -= j.damage

				projectilegroup.remove(j)
				changemusic('hit', False)
				if self.currentlifetotal <= 0:

					self.destroyed = True
					if not enemyid == self.id:
						self.player.score += 7
					self.counter = 0
					self.xvel = 0

					if player == None:
						self.player.game.enemygroup.remove(self)
					else:
						if player.game.screenfocus == 'Client':
							enemyid = self.id

			if pygame.sprite.collide_rect(self.detectable, j) \
				and not self.destroyed and j.type == 'shield':
				self.xvel = 0

		for p in self.player.game.enemygroup:

			if pygame.sprite.collide_rect(self.detectable,
					p.detectable) and not p.id == self.id:
				if xvel > 0:
					if self.rect.right >= p.rect.left \
						and self.rect.right < p.rect.right:
						self.xvel = 0

				if xvel < 0:
					if self.rect.left <= p.rect.right \
						and self.rect.left > p.rect.left:
						self.xvel = 0

				if yvel > 0:
					if self.rect.bottom >= p.rect.top \
						and self.rect.bottom < p.rect.bottom:
						self.yvel = 0

	# Animate

	def animate(self):
		pass
		if self.destroyed == True:
			pass
		else:
			self.walkloop(zombieRunnerwalkloop)

	# Walk Loop Animation

	def walkloop(self, loop):
		if self.counter <= 10:
			self.updatecharacter(loop[0])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[0],
						True, False))
		elif self.counter <= 20:
			self.updatecharacter(loop[1])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[1],
						True, False))
		elif self.counter <= 30:

			self.updatecharacter(loop[2])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[2],
						True, False))
		elif self.counter <= 40:

			self.updatecharacter(loop[3])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[3],
						True, False))
		elif self.counter <= 50:

			self.updatecharacter(loop[4])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[4],
						True, False))
		elif self.counter <= 60:

			self.updatecharacter(loop[5])
			if self.faceright <= False:
				self.updatecharacter(pygame.transform.flip(loop[5],
						True, False))
			self.counter = 0

		self.counter = self.counter + 5

	# Destroy Loop Animation

	def destroyloop(self, loop):
		if self.counter == 0:
			self.yoffset = -30
			self.updatecharacter(loop[0])
		elif self.counter == 5:
			self.updatecharacter(loop[1])
		elif self.counter == 10:
			self.updatecharacter(loop[2])
		elif self.counter == 15:
			self.updatecharacter(loop[3])
		elif self.counter == 20:
			self.updatecharacter(loop[4])
		elif self.counter == 25:
			self.updatecharacter(loop[5])
		elif self.counter == 30:
			self.updatecharacter(loop[6])
		elif self.counter == 35:
			self.updatecharacter(loop[7])
		elif self.counter == 40:
			self.updatecharacter(loop[8])
		elif self.counter == 45:
			self.updatecharacter(loop[9])
		elif self.counter == 50:
			self.updatecharacter(loop[10])
		elif self.counter == 55:
			self.updatecharacter(loop[11])
		elif self.counter == 60:
			self.kill()
			self.counter = 0
		self.counter = self.counter + 20

	# Update Animation Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class zombieArcher(Entity):

	def __init__(
		self,
		x,
		y,
		player,
		id,
		xvel=2,
		typee='zombieArcher',
		):
		Entity.__init__(self)

		x = x * 3
		y = y * 3

		self.type = typee
		self.id = id
		self.player = player
		self.isstopped = False

		self.currentlifetotal = 1

		# Set Velocities

		self.pcounter = 0
		self.xvel = xvel
		self.yvel = -2
		self.move = -0.3

		# States

		self.destroyed = False
		self.faceright = False
		self.attacking = False
		self.atcounter = 0

		# Offests

		self.xoffset = -130
		self.yoffset = 0

		# Counter

		self.counter = 0

		# Configure Track
		# Create Sprite Image

		self.image = Surface((25 * 2, 30 * 2), pygame.SRCALPHA)
		self.image = zombieArcherwalk1
		self.rect = Rect(x, y, 25 * 2, 30 * 2)

		# Create Dectectable

		self.detectable = pygame.sprite.Sprite()

		self.detectable.rect = Rect(x, y, 25 * 2, 30 * 2)
		self.detectable.image = Surface((25 * 2, 30 * 2))

		self.detectable.image.fill(Color('#003FFF'))
		self.detectable.image.set_alpha(150)
		self.detectable.image.convert_alpha()
		self.player.game.detectablegroup.add(self.detectable)

	def __getstate__(self):
		try:

			state = self.__dict__.copy()
			surface = state.pop('image')
			state['surface_stringa'] = (pygame.image.tostring(surface,
					'RGBA'), surface.get_size())
			return state
		except Exception as e:
			print(e)
			pass

	def __setstate__(self, state):
		try:

			(surface_string, size) = state.pop('surface_stringa')
			state['image'] = pygame.image.fromstring(surface_string,
					size, 'RGBA')
			self.__dict__.update(state)
		except:
			pass

	def update(self, platforms, projectilegroup):

		# Move according to player position

		self.pcounter = self.pcounter + 1
		self.isstopped = False
		xstopped = False
		ystopped = False

		if self.detectable.rect.x < self.player.detectable.rect.x:

			if self.detectable.rect.x + 400 \
				>= self.player.detectable.rect.x:
				xstopped = True

				pass
			else:

				self.detectable.rect.x += self.xvel

			self.faceright = True
		if self.detectable.rect.y < self.player.detectable.rect.y:

			if self.detectable.rect.y + 300 \
				>= self.player.detectable.rect.y:
				ystopped = True

				pass
			else:

				self.detectable.rect.y += self.xvel

		if self.detectable.rect.x > self.player.detectable.rect.x:
			if self.detectable.rect.x - 400 \
				<= self.player.detectable.rect.x:
				xstopped = True
			else:

				self.detectable.rect.x -= self.xvel

			self.faceright = False
		if self.detectable.rect.y > self.player.detectable.rect.y:
			if self.detectable.rect.y - 200 \
				<= self.player.detectable.rect.y:
				ystopped = True
			else:

				self.detectable.rect.y -= self.xvel
		if xstopped and ystopped:
			self.isstopped = True

		# Collisions

		self.collide(0, self.yvel, platforms, projectilegroup)
		self.rect.x = self.detectable.rect.x + 0
		self.rect.y = self.detectable.rect.y + 0

		# shoot projectiles

		if self.pcounter == random.randint(1, 2):

			projectile = Projectile(self, self.player.game, 'guu')

			self.player.game.projectilegroup.add(projectile)
			changemusic('bullet', False)
			self.attacking = True
			self.pcounter += 1
			self.atcounter = 0

		if self.pcounter > 100:
			self.pcounter = 0

		self.animate()

	def collide(
		self,
		xvel,
		yvel,
		platforms,
		projectilegroup,
		player=None,
		):

		# Collide Projectiles

		global vssstates, convoid, inconvo, rolstates, enemyid
		for j in projectilegroup:
			if pygame.sprite.collide_rect(self.detectable,
					j.detectable) and not self.destroyed and not j.type \
				== 'guu':
				projectilegroup.remove(j)

				self.currentlifetotal -= j.damage
				changemusic('hit', False)
				self.counter = 0
				if self.currentlifetotal <= 0:
					self.destroyed = True

					if player == None:
						self.player.game.enemygroup.remove(self)
					else:
						if player.game.screenfocus == 'Client':
							enemyid = self.id

					if not enemyid == self.id:
						self.player.score += 7
				self.xvel = 0

		# with platform

		for p in platforms:
			if pygame.sprite.collide_rect(self.detectable, p):
				if yvel > 0:
					self.detectable.rect.bottom = p.rect.top
					self.move = -0.3
				if yvel < 0:
					self.detectable.rect.top = p.rect.bottom
					self.move = 0.3

	# Animate

	def animate(self):
		if self.destroyed == True:
			pass
		elif self.attacking:

			self.attackloop(zombieArchershoot)
		elif self.isstopped:
			self.updatecharacter(zombieArcherwalk1)
			self.counter = 0
			if self.detectable.rect.x > self.player.detectable.rect.x:
				self.updatecharacter(pygame.transform.flip(zombieArcherwalk1,
						True, False))
		else:

			self.walkloop(zombieArcherwalkloop)

	# Walk Loop Animation

	def walkloop(self, loop):
		if self.counter <= 10:
			self.updatecharacter(loop[0])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[0],
						True, False))
		elif self.counter <= 20:
			self.updatecharacter(loop[1])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[1],
						True, False))
		elif self.counter <= 30:

			self.updatecharacter(loop[2])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[2],
						True, False))
		elif self.counter <= 40:

			self.updatecharacter(loop[3])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[3],
						True, False))
		elif self.counter <= 50:

			self.updatecharacter(loop[4])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[4],
						True, False))
		elif self.counter <= 60:

			self.updatecharacter(loop[5])
			if self.faceright == False:
				self.updatecharacter(pygame.transform.flip(loop[5],
						True, False))
		else:
			self.counter = 0

		self.counter = self.counter + 5

	def attackloop(self, loop):
		if self.atcounter == 10:
			self.updatecharacter(loop)
			if self.detectable.rect.x > self.player.detectable.rect.x:
				self.updatecharacter(pygame.transform.flip(loop, True,
						False))
		elif self.atcounter == 20:
			self.updatecharacter(loop)

			if self.detectable.rect.x > self.player.detectable.rect.x:
				self.updatecharacter(pygame.transform.flip(loop, True,
						False))
		elif self.atcounter == 30:

			self.updatecharacter(loop)

			if self.detectable.rect.x > self.player.detectable.rect.x:
				self.updatecharacter(pygame.transform.flip(loop, True,
						False))
		elif self.atcounter >= 40:

			self.updatecharacter(loop)
			self.attacking = False
			if self.detectable.rect.x > self.player.detectable.rect.x:
				self.updatecharacter(pygame.transform.flip(loop, True,
						False))
			self.atcounter = 0

		self.atcounter = self.atcounter + 5

	def destroyloop(self, loop):
		if self.counter == 0:
			self.yoffset = -30
			self.updatecharacter(loop[0])
		elif self.counter == 5:
			self.updatecharacter(loop[1])
		elif self.counter == 10:
			self.updatecharacter(loop[2])
		elif self.counter == 15:
			self.updatecharacter(loop[3])
		elif self.counter == 20:
			self.updatecharacter(loop[4])
		elif self.counter == 25:
			self.updatecharacter(loop[5])
		elif self.counter == 30:
			self.updatecharacter(loop[6])
		elif self.counter == 35:
			self.updatecharacter(loop[7])
		elif self.counter == 40:
			self.updatecharacter(loop[8])
		elif self.counter == 45:
			self.updatecharacter(loop[9])
		elif self.counter == 50:
			self.updatecharacter(loop[10])
		elif self.counter == 55:
			self.updatecharacter(loop[11])
		elif self.counter == 60:
			self.kill()
			self.counter = 0
		self.counter = self.counter + 5

	# Update Animation Frame

	def updatecharacter(self, ansurf):
		self.image = ansurf


class PauseMenu(object):

	def __init__(self, game):
		self.game = game

	def createpausemenu(self):

		# Empty Sprite Groups

		self.game.titlegroup.empty()
		self.game.menugroup.empty()

		# Create Background Sprite

		bg = Entity()
		bg.image = \
			pygame.image.load('Media/Graphics/Backgrounds/title.jpg')
		self.game.titlegroup.add(bg)

		# Create String Sprite

		ss = Entity()
		font = pygame.font.Font(None, 80)
		ss.image = font.render(' ', 1, (255, 255, 255))
		ss.rect = Rect(0, 0, 100, 100)
		ss.rect.x = 290
		ss.rect.y = 400
		self.game.menugroup.add(ss)

	def inputhandler(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				raise SystemExit('QUIT')
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				raise SystemExit('ESCAPE')
			if e.type == KEYDOWN and e.key == K_RETURN:
				self.game.screenfocus = 'Game'

			pos = pygame.mouse.get_pos()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game.buttongroup['resume'].isOver(pos) \
					and not self.game.screenfocus == 'Game Over':

					self.game.screenfocus = 'Game'
				elif self.game.buttongroup['exit'].isOver(pos):

					raise SystemExit('QUIT')
				elif self.game.buttongroup['restart'].isOver(pos):

					return True
				elif self.game.buttongroup['highscore'].isOver(pos):
					self.game.screenfocus = 'Score'
				elif self.game.buttongroup['shop'].isOver(pos):

					self.game.screenfocus = 'Shop'

			if e.type == pygame.MOUSEMOTION:
				if self.game.buttongroup['resume'].isOver(pos) \
					and not self.game.screenfocus == 'Game Over':

					self.game.buttongroup['resume'].color = (100, 255,
							0)
				elif not self.game.buttongroup['resume'].isOver(pos) \
					and not self.game.screenfocus == 'Game Over':

					self.game.buttongroup['resume'].color = (0, 0, 255)

				if self.game.buttongroup['exit'].isOver(pos):
					self.game.buttongroup['exit'].color = (100, 255, 0)
				elif not self.game.buttongroup['exit'].isOver(pos):
					self.game.buttongroup['exit'].color = (255, 0, 0)

				if self.game.buttongroup['highscore'].isOver(pos):
					self.game.buttongroup['highscore'].color = (100,
							255, 0)
				elif not self.game.buttongroup['highscore'].isOver(pos):
					self.game.buttongroup['highscore'].color = (255,
							255, 0)

				if self.game.buttongroup['shop'].isOver(pos):
					self.game.buttongroup['shop'].color = (100, 255, 0)
				elif not self.game.buttongroup['shop'].isOver(pos):
					self.game.buttongroup['shop'].color = (255, 255, 0)

	def update(self):
		self.inputhandler()


class LevelComplete(object):

	def __init__(self, game):
		self.game = game

	def createlevelcomplete(self):

		# Empty Sprite Groups

		self.game.titlegroup.empty()
		self.game.menugroup.empty()

		# Create Background Sprite

		bg = Entity()
		bg.image = \
			pygame.image.load('Media/Graphics/Backgrounds/title.jpg')
		self.game.titlegroup.add(bg)

		# Create String Sprite

		ss = Entity()
		font = pygame.font.Font(None, 80)
		ss.image = font.render('Level Complete', 1, (255, 255, 255))
		ss.rect = Rect(0, 0, 100, 100)
		ss.rect.x = 200
		ss.rect.y = 400
		self.game.menugroup.add(ss)


class GameOver(object):

	def __init__(self, game):
		self.game = game

	def creategameover(self):

		# Empty Sprite Groups

		self.game.titlegroup.empty()
		self.game.menugroup.empty()

		# Create Background Sprite

		bg = Entity()
		bg.image = \
			pygame.image.load('Media/Graphics/Backgrounds/title.jpg')
		self.game.titlegroup.add(bg)

		# Create String Sprite

		ss = Entity()
		font = pygame.font.Font(None, 80)
		ss.image = font.render('Game Over', 1, (255, 255, 255))
		ss.rect = Rect(0, 0, 100, 100)
		ss.rect.x = 240
		ss.rect.y = 400
		self.game.menugroup.add(ss)


class Title(object):

	def __init__(self, game, player=None):
		self.game = game
		self.counter = 0
		self.createtitle()
		self.player = player

	def createtitle(self):

		# Empty Sprite Groups

		self.game.titlegroup.empty()
		self.game.menugroup.empty()

		# Create Background Sprite

		bg = Entity()
		bg.image = \
			pygame.image.load('Media/Graphics/Backgrounds/title.jpg')
		self.game.titlegroup.add(bg)

	def inputhandler(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				raise SystemExit('QUIT')
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				raise SystemExit('ESCAPE')
			if e.type == KEYDOWN and e.key == K_SPACE:
				self.game.screenfocus = 'Character'

			pos = pygame.mouse.get_pos()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game.buttongroup['start'].isOver(pos):

					self.game.screenfocus = 'Character'
				elif self.game.buttongroup['exit'].isOver(pos):

					raise SystemExit('QUIT')
				elif self.game.buttongroup['multiplayer'].isOver(pos):
					self.game.screenfocus = 'MultiplayerCharacter'
				elif self.game.buttongroup['host'].isOver(pos):
					self.game.screenfocus = 'host'
				elif self.game.buttongroup['connect'].isOver(pos):
					self.game.screenfocus = 'Connect'
				elif self.game.buttongroup['highscore'].isOver(pos):
					self.game.screenfocus = 'Score'
				elif self.game.buttongroup['back'].isOver(pos):
					self.game.screenfocus = 'Title'

			if e.type == pygame.MOUSEMOTION:
				if self.game.buttongroup['start'].isOver(pos):

					self.game.buttongroup['start'].color = (100, 255, 0)
				else:

					self.game.buttongroup['start'].color = (0, 200, 0)

				if self.game.buttongroup['exit'].isOver(pos):
					self.game.buttongroup['exit'].color = (255, 200, 0)
				else:
					self.game.buttongroup['exit'].color = (255, 0, 0)

				if self.game.buttongroup['multiplayer'].isOver(pos):
					self.game.buttongroup['multiplayer'].color = (200,
							200, 0)
				else:
					self.game.buttongroup['multiplayer'].color = (255,
							0, 255)

				if self.game.buttongroup['host'].isOver(pos):
					self.game.buttongroup['host'].color = (0, 0, 255)
				else:
					self.game.buttongroup['host'].color = (0, 255, 0)

				if self.game.buttongroup['connect'].isOver(pos):
					self.game.buttongroup['connect'].color = (0, 0, 255)
				else:
					self.game.buttongroup['connect'].color = (255, 0, 0)
				if self.game.buttongroup['highscore'].isOver(pos):
					self.game.buttongroup['highscore'].color = (0, 0,
							255)
				else:
					self.game.buttongroup['highscore'].color = (255, 0,
							0)
				if self.game.buttongroup['back'].isOver(pos):
					self.game.buttongroup['back'].color = (0, 0, 255)
				else:
					self.game.buttongroup['back'].color = (255, 0, 0)

	def update(self):
		self.inputhandler()

		# Animate Title Screen

		self.counter = self.counter + 1

	def update2(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				raise SystemExit('QUIT')
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				raise SystemExit('ESCAPE')
			if e.type == KEYDOWN and e.key == K_SPACE:
				self.game.screenfocus = 'Game'

			pos = pygame.mouse.get_pos()

			if e.type == pygame.MOUSEBUTTONDOWN:
				if self.game.buttongroup['host'].isOver(pos):
					self.game.screenfocus = 'host'
				elif self.game.buttongroup['connect'].isOver(pos):
					self.game.screenfocus = 'Connect'
				elif self.game.buttongroup['back'].isOver(pos):
					self.game.screenfocus = 'Title'

			if e.type == pygame.MOUSEMOTION:
				if self.game.buttongroup['host'].isOver(pos):
					self.game.buttongroup['host'].color = (0, 0, 255)
				else:
					self.game.buttongroup['host'].color = (0, 255, 0)

				if self.game.buttongroup['connect'].isOver(pos):
					self.game.buttongroup['connect'].color = (0, 0, 255)
				else:
					self.game.buttongroup['connect'].color = (255, 0,
							255)
				if self.game.buttongroup['back'].isOver(pos):
					self.game.buttongroup['back'].color = (0, 0, 255)
				else:
					self.game.buttongroup['back'].color = (255, 0, 0)


def text(
	msg,
	y=0,
	color=0,
	size=30,
	):

	font = pygame.font.SysFont('comicsans', size)
	if color == 'red':
		text = font.render(msg, 1, (255, 0, 0))
	else:
		text = font.render(msg, 1, (255, 255, 255))
	screen.blit(text, (36, 38 + y * 20))
	pygame.display.update()


def changemusic(name, music):  # if music true if sound than false
	global musicplaying
	if music:

		m = pygame.mixer.music.load('Media/Music/' + name + '.mp3')
		pygame.mixer.music.set_volume(0.3)
		pygame.mixer.music.play(-1)
		musicplaying = name
	else:

		sound = pygame.mixer.Sound('Media/Music/' + name + '.ogg')

		sound.play()


class Display(Entity):

	def __init__(self, string):
		Entity.__init__(self)
		self.font = pygame.font.Font(None, 80)
		self.image = self.font.render(string, 1, (255, 0, 0))

	def update(self, string):
		self.image = self.font.render(string, 1, (255, 0, 0))


class button:

	def __init__(
		self,
		color,
		x,
		y,
		width,
		height,
		text='',
		):
		self.color = color
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.text = text

	def draw(self, win, outline=None):

		# Call this method to draw the button on the screen

		if outline:
			pygame.draw.rect(win, outline, (self.x - 2, self.y - 2,
							 self.width + 4, self.height + 4), 0)

		pygame.draw.rect(win, self.color, (self.x, self.y, self.width,
						 self.height), 0)

		if self.text != '':
			font = pygame.font.SysFont('comicsans', 60)
			text = font.render(self.text, 1, (0, 0, 0))
			win.blit(text, (self.x + self.width / 2 - text.get_width()
					 / 2, self.y + self.height / 2 - text.get_height()
					 / 2))

	def isOver(self, pos):

		# Pos is the mouse position or a tuple of (x,y) coordinates

		if pos[0] > self.x and pos[0] < self.x + self.width:
			if pos[1] > self.y and pos[1] < self.y + self.height:
				return True

		return False


def inputtxt(msg):
	window = Tk()
	window.title('window')
	window.geometry('500x500+300+100')
	txt = StringVar()

	def com():
		if txt.get() == '' or txt.get()[0] == ' ':
			pass
		else:
			window.destroy()

	labl2 = Label(text=msg, font=20).pack()
	button1 = Button(text='Enter', command=com).pack()
	text = Entry(textvariable=txt).pack()
	window.mainloop()
	while txt.get() == '' or txt.get()[0] == ' ':
		window.mainloop()

	return txt.get()


def showtxt(msg):
	window = Tk()
	window.title('window')
	window.geometry('500x500+300+100')
	txt = StringVar()

	def com():
		window.destroy()

	labl2 = Label(text=msg, font=20).pack()
	button1 = Button(text='OK', command=com).pack()
	window.mainloop()


if __name__ == '__main__':
	main()

	# main()

			