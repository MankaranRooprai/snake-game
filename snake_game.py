import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake game by Mankaran')

game_over = False

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
	for x in snake_list:
		pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

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

	snake_list = []
	length_of_snake = 1

	foodx = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0
	foody = round(random.randrange(0, 800 - snake_block) / 10.0) * 10.0

	while not game_over:

		#if the game is over, display a message
		while game_close == True:
			dis.fill(blue)
			message("You Lost! Press Q-Quit or C-Play Again", red)

			pygame.display.update()

			#constantly check for any key events, specifically q or c
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						game_over = True
						game_close = False
					if event.key == pygame.K_c:
						gameLoop()

		#constantly check for any key events, and send snake in the direction that a key is pressed in
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

		#if the snake gets out of bounds or touches the boundaries, the user loses
		if x1 >= 800 or x1 < 0 or y1 >= 600 or y1 < 0:
			game_close = True

		#change the coordinates of the snake
		x1 += x1_change
		y1 += y1_change

		#draw the snake and food
		dis.fill(blue)
		pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #x and y coordinates, and width and height of rectangle
		snake_head = []
		snake_head.append(x1)
		snake_head.append(y1)
		snake_list.append(snake_head)

		#if the length of snake_list is greater than the actual snake,
		if len(snake_list) > length_of_snake:
			#than delete the first item of snake_list
			#(helps to ensure that whatever amount of arrays are in snake_list are actual blocks part of the snake)
			del snake_list[0]

		for x in snake_list[:-1]:
			if x == snake_head:
				game_close = True

		our_snake(snake_block, snake_list)

		pygame.display.update()

		#if the snake is where a piece of food is, display 'Yummy!'
		if x1 == foodx and y1 == foody:
			foodx = round(random.randrange(0, 800 - snake_block))
			foody = round(random.randrange(0, 600 - snake_block))
			length_of_snake += 1
		clock.tick(snake_speed)

	pygame.quit()
	quit()

gameLoop()
