import pygame
import os
import sys
import inputbox
from errorScreen import errorScreen
from pygame.locals import *

class animation:
	def __init__(self,screen,direction,text):
		FPS = 30
		fpsClock = pygame.time.Clock()
		screen = pygame.display.set_mode((600,400), 0, 32)
		pygame.display.set_caption('Animation')
		WHITE = (255, 255, 255)
		catImg = pygame.image.load('Images/block.png')
		tree = pygame.image.load('Images/tree.png')
		background = pygame.image.load('Images/background.png')
		screen.blit(background,(0,0))
		treex=370
		treey = 0
		catx = 0
		caty = 240
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		textpos.y = 350
		background.blit(text, textpos)
		while True :			#main game loop
			screen.blit(background,(0,0))
			if direction == 'right':
				catx += 5
		        	treex -= 5

			if catx>590 :
				errorScreen(screen,"Oops.. Block went to Infinity")
			screen.blit(catImg, (catx,caty))
			screen.blit(tree, (treex,treey))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)
