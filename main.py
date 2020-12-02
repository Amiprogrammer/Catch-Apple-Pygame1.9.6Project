"""
author: Juliao Martins
github account: https://www.github.com/amiprogrammer/

CATCH APPLE WITH PYGAME 1.9.6

NOTE:
    i'm build this game cause, i want to improve my skill in pygame library to develop game and i want to make something new with pygame library.
"""

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

    apple_y += apple_y_change
    apple(apple_x,apple_y)

    bowl_x += bowl_x_change
    bowl(bowl_x,bowl_y)

    pygame.display.update()

pygame.quit()