import math
import sys
import random
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(flags=HWSURFACE, size=(680,520))
icon = pygame.image.load("img\icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Catch Apple")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    pygame.display.update()

pygame.quit()
