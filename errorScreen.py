import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import os
import sys
import inputbox

class errorScreen:
	def __init__(self, screen,text):
		pygame.mixer.music.stop()


	        # set up music
 	        pygame.mixer.music.load('error.mid')
	        pygame.mixer.music.play(-1, 0.0)

		pygame.font.init()
		fontobject = pygame.font.Font(None,18)
		
               	bckgd = pygame.image.load('Images/error.jpg')
               	screen.blit(bckgd,(0,0))
		pygame.draw.rect(screen, (75,0,0),((screen.get_width() / 2) - 100,100,200,20), 0)
		pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 102,98,204,24), 1)
		if len(text) != 0:
			screen.blit(fontobject.render(text, 1, (255,255,255)),((screen.get_width() / 2) - 100, 100))
			pygame.display.flip()
			btnReplay = Button('Play Again ?')
			btnExit = Button('Exit')
			clock = pygame.time.Clock()
			
			run1= True;
			run2= False;
			while run1:
				mouse2 = pygame.mouse.get_pos()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if btnReplay.obj.collidepoint(mouse2):
							print "restart"
							os.execl(sys.executable, sys.executable, *sys.argv)
						elif btnExit.obj.collidepoint(mouse2):
							print "exit"
							run1= False;
							run2 = True;
				btnReplay.draw(screen, mouse2, (100,(screen.get_height()-100),100,20), (100,(screen.get_height()-100)))
				btnExit.draw(screen, mouse2, (300,(screen.get_height()-100),100,20), (300,(screen.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
			if run2 :
				sys.exit()
			else :
				print "some error"
				return
