"""
author: Juliao Martins
github account: https://www.github.com/amiprogrammer/

CATCH APPLE WITH PYGAME 1.9.6

NOTE:
    i'm build this game cause, i want to improve my skill in pygame library to develop game and i want to make something new with pygame library.
"""

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(size=(840,680), flags=HWSURFACE)

icon = pygame.image.load("img/apple-icon.png")
pygame.display.set_icon(icon)

pygame.display.set_caption("Catch Apple")

# background color
darkgray = pygame.Color("darkgray")

running = True  
while running:

    screen.fill(darkgray)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()