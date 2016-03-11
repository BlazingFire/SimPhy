import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from errorScreen import errorScreen

def get_key():
	while 1:
		event = pygame.event.poll()
		if event.type == KEYDOWN:
			return event.key
		else:
			pass
			
def display_box(screen,countIn, message):
	"Print a message in a box in the middle of the screen"
	fontobject = pygame.font.Font(None,18)
	pygame.draw.rect(screen, (75,0,0),(30,countIn*10,200,20), 0)
	pygame.draw.rect(screen, (255,255,255),(28,countIn*10-2,204,24), 1)
	if len(message) != 0:
		screen.blit(fontobject.render(message, 1, (255,255,255)),(30, countIn*10))
	pygame.display.flip()
	
def ask(screen, question,countIn):
	try:
		"ask(screen, question) -> answer"
		pygame.font.init()
		current_string = []
		display_box(screen,countIn, question + ": " + string.join(current_string,""))
		#print "now enter"
		while 1:
			inkey = get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				break
			elif inkey == K_MINUS:
				if len(current_string) == 0:
					current_string.append("-")
			elif inkey <= 127:
				current_string.append(chr(inkey))
			display_box(screen, countIn,question + ": " + string.join(current_string,""))
		return string.join(current_string,"")
	except :
		print "error in getting input"
		errorScreen(screen,"Error in getting "+question)
		return
