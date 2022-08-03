import pygame
import time
pygame.init()

dis = pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption('Snake game by Mankaran')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis = pygame.display.set_mode((800, 600))

game_over = False

x1 = 400
y1 = 300

snake_block = 10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [400, 300])

while not game_over:
	for event in pygame.event.get():
		print(event) #prints out all the actions that take place on the screen
		if event.type == pygame.QUIT: #if the event is the close button is pressed,
			game_over = True #then set game_over to true and close the application
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
			    x1_change = -10
			    y1_change = 0
			elif event.key == pygame.K_RIGHT:
				x1_change = 10
				y1_change = 0
			elif event.key == pygame.K_UP:
				y1_change = -10
				x1_change = 0
			elif event.key == pygame.K_DOWN:
				y1_change = 10
				x1_change = 0

	if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
		game_over = True

	x1 += x1_change
	y1 += y1_change

	dis.fill(white)
	pygame.draw.rect(dis, black, [x1, y1, 10, 10]) #x and y coordinates, and width and height of rectangle

	pygame.display.update()

	clock.tick(30)

message("You lost", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
quit()
