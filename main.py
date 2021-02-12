import math
import sys
import random
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode(flags=HWSURFACE, size=(640,480))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    pygame.display.update()

pygame.quit()
