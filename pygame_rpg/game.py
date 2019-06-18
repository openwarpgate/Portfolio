import sqlite3, binascii, datetime
import pygame, sys, random, socket, _thread, time
from pygame.locals import *

# we will make game.
# agent can build, gather, train, and so on.
# It is kind of RPG.

# variable setting
units = []
buildings = []
items = []

# Pygame Setting
pygame.init()
DISPLAYSURF = pygame.display.set_mode((1200,900),0,32)
pygame.display.set_caption('Game')
fpsClock = pygame.time.Clock()
BASICFONTSIZE = 16
BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

# Color Setting
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKYBLUE = (128, 128, 255)
DARKGRAY = (100, 100, 100)
GRAY = (140,140,140)
WHITEGRAY = (200,200,200)

# initial variable setting
scene = 1
interface = 1
triggerlist = []
FPS = 20

# game state
state = 1 # start memu
interface = 1 # ordinary map

class unit:
	name = ''
	num = 0
	# Position
	position = [0,0,0]

	# BuildingStat
	BuildingStat = 0
	# CraftingStat
	CraftingStat = 0
	# CombatStat
	CombatStat = {'hp' : [0,0], 'atk': 0, 'atkspeed': 0, 'atkrange': 0, 'speed': 0}

	# Aura
	BuildingAura = 0
	CraftingAura = 0
	CombatAura = 0
	AuraRange = 0
	# Item
	inventory = []

	# Image
	imagePath = ''

	# Allowed Action. Based on Player`s Command.
	# Treat about action only influence to world`s state.

	def move():
		pass

	def attack():
		pass

	def equip():
		pass

	def craft():
		pass

	def build():
		pass

	def generate(self):
		self.name = 'moon' # need to modify

		# basic stat setting
		self.position = [600,400,30]
		self.BuildingStat = 5
		self.CraftingStat = 5
		self.CombatStat['hp'] = [100,100]
		self.CombatStat['atk'] = 5
		self.atkspeed = 0.5
		self.atkrange = 50
		self.speed = 150

		# aura
		self.BuildingAura = 0
		self.CraftingAura = 0
		self.CombatAura = 0
		self.AuraRange = 100

		# inventory
		self.inventory = []


class building:
	name = ''
	num = 0
	# position
	position = (0,0,0,0)

	# hp
	hp = (0,0)
	atk = 0
	atkspeed = 0
	atkrange = 0
	# Aura
	BuildingAura = 0
	CraftingAura = 0
	CombatAura = 0
	AuraRange = 0
	# unit
	presense = []
	# item
	inventory = []

	# Allowed Action. Based on Player`s Command.
	# Treat about action only influence to world`s state.

	def attack():
		pass
	def train():
		pass

class item:
	name = ''
	num = 0
	# position
	position = (0,0)
	# hp 
	hp = (0,0)
	# stat
	BuildingBonus = 0
	CraftingBonus = 0
	hpBonus = 0
	mpBonus = 0
	spBonus = 0

	# Aura Bonus
	BuildingAuraBonus = 0
	CraftingAuraBonus = 0
	CombatAuraBonus = 0




def start():
	pass

def drawmap():
	global triggerlist, scene
	triggerlist = []

	if scene == 1:
		# start scene

		DISPLAYSURF.fill(BLACK)
		# display map

		# for testing
		triggerlist.append((440, 240, 60, 20, 1, 0))
		textSurf = BASICFONT.render('New Game', True, WHITE)
		textRect = textSurf.get_rect()
		textRect.topleft = (440, 240)
		DISPLAYSURF.blit(textSurf,textRect)

		triggerlist.append((440, 340, 60, 20, 2, 0))
		textSurf = BASICFONT.render('Load Game', True, WHITE)
		textRect = textSurf.get_rect()
		textRect.topleft = (440, 340)
		DISPLAYSURF.blit(textSurf,textRect)

		triggerlist.append((440, 440, 60, 20, 3, 0))
		textSurf = BASICFONT.render('Options', True, WHITE)
		textRect = textSurf.get_rect()
		textRect.topleft = (440, 440)
		DISPLAYSURF.blit(textSurf,textRect)

		# testing end

		# draw building
		for i in buildings:
			pass
		# draw unit
		for i in units:
			pygame.draw.circle(DISPLAYSURF, SKYBLUE, (i.position[0], i.position[1]), i.position[2])

		pygame.display.update()

	elif scene == 2:
		# main game scene
		DISPLAYSURF.fill(BLACK)
		
		# draw structure
		pygame.draw.line(DISPLAYSURF, GRAY, (0, 650), (1200, 650))
		pygame.draw.line(DISPLAYSURF, GRAY, (250, 650), (250, 900))
		pygame.draw.line(DISPLAYSURF, GRAY, (950, 650), (950, 900))
		

		# draw the terrain. into (0,0) ~ (1200, 650)
		image = pygame.image.load('./data/image/terrain/water_3.jpg')
		image = pygame.transform.scale(image, (50, 50))
		
		for i in range(24):
			for j in range(13):
				DISPLAYSURF.blit(image, (i*50,j*50))

		pygame.display.update()


def processfunction(func, argument):
	global units, buildings, items, triggerlist, scene

	if func == 1:
		# start page
		# generate user character
		myCharacter = unit()
		myCharacter.generate()
		units.append(myCharacter)

		scene = 2




def processinput():
	global triggerlist

	mousex = 0
	mousey = 0
	mouseClicked = False

	for event in pygame.event.get(): # event handling loop
		if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
		elif event.type == MOUSEBUTTONUP:
			mousex, mousey = event.pos
			mouseClicked = True

	if mouseClicked == True:
		# process event if mouse cursor in event range
		for trigger in triggerlist:
			if mousex > trigger[0] and mousex < trigger[0] + trigger[2] and mousey > trigger[1] and mousey < trigger[1] + trigger[3]:
				processfunction(trigger[4], trigger[5])
		return (0,0)

def processaction():
	for i in units:
		pass
	for i in buildings:
		pass


def mainloop():
	while True:
		drawmap()
		processinput()
		processaction()

start()
mainloop()