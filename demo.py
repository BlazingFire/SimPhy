import pygame
import os
import sys
import inputbox
from Button import Button
from animation import animation
from animation2 import animation2
from errorScreen import errorScreen
from pygame.locals import *
import game1
import game2
pygame.init()

if __name__ == '__main__':
	#now Displaying first DISPLAYSURF, what need to be calculated
	background=pygame.image.load('Images/home.jpg')
	DISPLAYSURF = pygame.display.set_mode((600,400))
	DISPLAYSURF.blit(background,(0,0))

	# set up music
 	pygame.mixer.music.load('bill1.mid')
	pygame.mixer.music.play(-1, 0.0)
	musicPlaying = True
	
	try:
		btngame1=Button('Linear Motion')
		btngame2=Button('Vertical Motion')	
		clock = pygame.time.Clock()
		run1= True;
		while run1:
			mouse2 = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if btngame1.obj.collidepoint(mouse2):
						game1.startGame1(DISPLAYSURF)
					elif btngame2.obj.collidepoint(mouse2):
						game2.startGame2(DISPLAYSURF)
			btngame1.draw(DISPLAYSURF, mouse2, (100,210,150,20), (100,210))
			btngame2.draw(DISPLAYSURF, mouse2, (300,210,150,20), (300,210))
			pygame.display.update()
			clock.tick(60)


	except :
		if musicPlaying:
			pygame.mixer.music.stop()
		else:
			pygame.mixer.music.play(-1, 0.0)
		errorScreen(DISPLAYSURF,"Something went wrong")
