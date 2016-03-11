import pygame
import os
import sys
import inputbox
from Button import Button
from animation import animation
from errorScreen import errorScreen
from pygame.locals import *

def startGame1(DISPLAYSURF):
	btn = Button('Final Vel,v')
	btn2 = Button('Time, t')
	btn3 = Button('In. Vel, u')
	btn4 = Button('Accn., a')
	btn5 = Button('Displacement, s')
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1.jpg')
	run = True
	while run:
		DISPLAYSURF.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					countInputs=1;
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					v1 = u2 + a2 * t2
					v2 = str (v1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+v2+"metre/sec", 1, (10, 10, 10))
					animation(DISPLAYSURF,'right',text)
				elif btn2.obj.collidepoint(mouse):
					countInputs=1;
					u1 = inputbox.ask(DISPLAYSURF, "Initial Velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					v1 = inputbox.ask(DISPLAYSURF, "Final Velocity, t",countInputs)
					v2 = float (v1)
					t1 = (v2-u2)/a2
					t2 = str (t1)
					if(t1<0):
						errorScreen(DISPLAYSURF,"Invalid datas entered")
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+t2+"seconds", 1, (10, 10, 10))
					animation(DISPLAYSURF,'right',text)
				elif btn3.obj.collidepoint(mouse):
					countInputs=1;
					v1 = inputbox.ask(DISPLAYSURF, "Final velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					u1 = v2 - (a2 * t2)
					u2 = str (u1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Initial Velocity hence calculated is "+u2+"metre/sec", 1, (10, 10, 10))
					animation(DISPLAYSURF,'right',text)
				elif btn4.obj.collidepoint(mouse):
					countInputs=1;
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					v1 = inputbox.ask(DISPLAYSURF, "Final velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					a1 = (v2 - u2)/t2
					a2 = str (v1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Acceleration hence calculated is "+a2+"metre/sec^2", 1, (10, 10, 10))
					animation(DISPLAYSURF,'right',text)
		btn.draw(DISPLAYSURF, mouse, (100,100,100,20), (125,103))
		btn2.draw(DISPLAYSURF, mouse, (100,130,100,20), (125,133))
		btn3.draw(DISPLAYSURF, mouse, (100,160,100,20), (125,163))
		btn4.draw(DISPLAYSURF, mouse, (100,190,100,20), (125,193))
		pygame.display.update()
		clock.tick(60)
