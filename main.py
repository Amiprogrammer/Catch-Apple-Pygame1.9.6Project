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

LIGHTGREEN = pygame.Color("lightgreen")
WHITE = pygame.Color("white")
BGCOLOR = LIGHTGREEN

score = 0
game_over = False

apple_img = []
apple_x = []
apple_y = []
apple_move_to_y = []
apple_total = 4
for i in range(apple_total):
    apple_img.append(pygame.image.load("img\\apple.png"))
    apple_x.append(random.randint(0,618))
    apple_y.append(0)
    apple_move_to_y.append(0.4)
def apple(x,y,i):
    global screen, apple_img
    screen.blit(apple_img[i], (x,y))

bomb_img = []
bomb_x = []
bomb_y = []
bomb_move_to_y = []
bomb_total = 3
for i in range(bomb_total):
    bomb_img.append(pygame.image.load("img\\bomb.png"))
    bomb_x.append(random.randint(0,618))
    bomb_y.append(0)
    bomb_move_to_y.append(0.4)
def bomb(x,y,i):
    global screen, bomb_img
    screen.blit(bomb_img[i], (x,y))

bowl_img = pygame.image.load("img\\fruit-bowl.png")
bowl_x = 340
bowl_y = 450
move_to_x = 0
def bowl(x,y):
    global screen, bowl_img
    screen.blit(bowl_img, (x,y))

def isapplecollision(bowl_x,bowl_y,apple_x,apple_y):
    distance = math.sqrt((math.pow(bowl_x-apple_x,2)) + (math.pow(bowl_y-apple_y,2)))
    if distance < 27:
        return True
    else:
        return False

def isbombcollision(bowl_x,bowl_y,bomb_x,bomb_y):
    distance = math.sqrt((math.pow(bowl_x-bomb_x,2)) + (math.pow(bowl_y-bomb_y,2)))
    if distance < 27:
        return True
    else:
        return False

blackopsone = pygame.font.Font("font\\BlackOpsOne-Regular.ttf", 32)
def show_score():
    global screen, blackopsone, score
    x = blackopsone.render(f"score: {score}", True, pygame.Color("black"))
    screen.blit(x,(20,20))

while True:

    screen.fill(BGCOLOR)

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                move_to_x = -0.4
            elif event.key == K_d or event.key == K_RIGHT:
                move_to_x = 0.4
        elif event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                move_to_x = 0
            elif event.key == K_d or event.key == K_RIGHT:
                move_to_x = 0

    if bowl_x <= 0:
        bowl_x = 0
    elif bowl_x >= 618:
        bowl_x = 618

    for i in range(apple_total):
        if apple_y[i] >= 618:
            apple_x[i] = random.randint(0,618)
            apple_y[i] = 0

        applecollision = isapplecollision(bowl_x,bowl_y,apple_x[i],apple_y[i])

        if applecollision:
            apple_x[i] = random.randint(0,618)
            apple_y[i] = 0
            score += 1
            print(score)

        apple_y[i] += apple_move_to_y[i]
        apple(apple_x[i],apple_y[i],i)

    for i in range(bomb_total):

        if bomb_y[i] >= 618:
            bomb_x[i] = random.randint(0,618)
            bomb_y[i] = 0

        bombcollision = isbombcollision(bowl_x,bowl_y,bomb_x[i],bomb_y[i])

        if bombcollision:
            game_over = True
            print("game over!")

        bomb_y[i] += bomb_move_to_y[i]
        bomb(bomb_x[i],bomb_y[i],i)

    if game_over:
        BGCOLOR = WHITE

    bowl_x += move_to_x
    bowl(bowl_x,bowl_y)

    show_score()

    pygame.display.update()

pygame.quit()
