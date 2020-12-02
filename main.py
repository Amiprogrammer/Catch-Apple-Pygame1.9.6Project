"""
author: Juliao Martins
github account: https://www.github.com/amiprogrammer/

CATCH APPLE WITH PYGAME 1.9.6

NOTE:
    i'm build this game cause, i want to improve my skill in pygame library to develop game and i want to make something new with pygame library.
"""

import math
import random
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(size=(840,680), flags=HWSURFACE)

icon = pygame.image.load("img/apple-icon.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Catch Apple")

# background color
darkgray = pygame.Color("darkgray")

# bowl here
bowl_img = pygame.image.load("img/fruit-bowl.png")
bowl_x = 390
bowl_y = 570
bowl_x_change = 0
def bowl(x,y):
    global screen,bowl_img
    screen.blit(bowl_img,(x,y))

# apple here
apple_img = pygame.image.load("img/apple.png")
apple_x = random.randint(10,756)
apple_y = random.randint(60,180)
apple_y_change = 1
def apple(x,y):
    global screen,apple_img
    screen.blit(apple_img,(x,y))


# collision here
def iscollision(bowl_x,bowl_y,apple_x,apple_y):
    distance = math.sqrt((math.pow(bowl_x-apple_x,2)) + (math.pow(bowl_y-apple_y,2)))
    if distance < 27:
        return True
    else:
        return False

p_score = 0

score_font = pygame.font.Font("font/ComicNeue.ttf", 40)
def show_score():
    global screen, score_font
    score_font.set_bold(True)
    score = score_font.render("Score: " + str(p_score), True, pygame.Color("white"))
    screen.blit(score, (20,20))

running = True  
while running:

    screen.fill(darkgray)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                bowl_x_change = -1
            elif event.key == K_RIGHT:
                bowl_x_change = 1
        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_RIGHT:
                bowl_x_change = 0

    # boundaries of bowl
    if bowl_x <= 10:
        bowl_x = 10
    elif bowl_x >= 756:
        bowl_x = 756

    # boundaries of apple
    if apple_y >= 690:
        apple_x = random.randint(10,756)
        apple_y = random.randint(60,180)

    collision = iscollision(bowl_x,bowl_y,apple_x,apple_y)

    if collision:
        apple_x = random.randint(10,756)
        apple_y = random.randint(60,180)
        p_score += 1

    apple_y += apple_y_change
    apple(apple_x,apple_y)

    bowl_x += bowl_x_change
    bowl(bowl_x,bowl_y)

    show_score()

    pygame.display.update()

pygame.quit()