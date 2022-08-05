import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Mankaran')

game_over = False

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

x1_change = 0
y1_change = 0

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
	mesg = font_style.render(msg, True, color)
	dis.blit(mesg, [800/3, 600/3])

def gameLoop():
	game_over = False
	game_close = False

	x1 = 400
	y1 = 300

	x1_change = 0
	y1_change = 0

	foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0

	while not game_over:

		while game_close == True:
			dis.fill(white)
			message("You Lost! Press Q-Quit or C-Play Again", red)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameLoop()

		for event in pygame.event.get():
			#print(event) #prints out all the actions that take place on the screen
			if event.type == pygame.QUIT: #if the event is the close button is pressed,
				game_over = True #then set game_over to true and close the application
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
				    x1_change = -snake_block
				    y1_change = 0
				elif event.key == pygame.K_RIGHT:
					x1_change = snake_block
					y1_change = 0
				elif event.key == pygame.K_UP:
					y1_change = -snake_block
					x1_change = 0
				elif event.key == pygame.K_DOWN:
					y1_change = snake_block
					x1_change = 0

		if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
			game_close = True

		x1 += x1_change
		y1 += y1_change

		dis.fill(white)
		pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block]) #x and y coordinates, and width and height of rectangle
		pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
		pygame.display.update()

		if x1 == foodx and y1 == foody:
			print("Yummy!")
		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameLoop()
