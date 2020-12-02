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

def catch_apple():
    try:
        global screen,bowl_img,bowl_x,bowl_y,bowl_x_change,apple_img,apple_x,apple_y,apple_y_change,num_of_apple,black_apple_img,black_apple_x,black_apple_y,black_apple_y_change,num_of_black_apple,p_score,score_font,game_status,game_over_img,restart_game

        pygame.init()

        screen = pygame.display.set_mode(size=(840,680), flags=HWSURFACE)

        icon = pygame.image.load("img/apple-icon.png")
        pygame.display.set_icon(icon)

        pygame.display.set_caption("Catch Apple")

        # background color
        darkgray = pygame.Color("darkgray")

        # background sound
        bg_sound = pygame.mixer.Sound("sound/game-tune.wav")
        bg_sound.set_volume(0.5)
        bg_sound.play(-1) # will loop!

        # bowl here
        bowl_img = pygame.image.load("img/fruit-bowl.png")
        bowl_x = 390
        bowl_y = 570
        bowl_x_change = 0
        def bowl(x,y):
            global screen,bowl_img
            screen.blit(bowl_img,(int(x),int(y)))

        # multiple apple
        apple_img = []
        apple_x = []
        apple_y = []
        apple_y_change = []
        num_of_apple = 5
        # apple here
        for i in range(num_of_apple):
            apple_img.append(pygame.image.load("img/apple.png"))
            apple_x.append(random.randint(10,756))
            apple_y.append(random.randint(60,180))
            apple_y_change.append(1)
        def apple(x,y,i):
            global screen,apple_img
            screen.blit(apple_img[i],(x,y))

        # multiple black apple
        black_apple_img = []
        black_apple_x = []
        black_apple_y = []
        black_apple_y_change = []
        num_of_black_apple = 3
        # apple here
        for i in range(num_of_black_apple):
            black_apple_img.append(pygame.image.load("img/black-apple.png"))
            black_apple_x.append(random.randint(10,756))
            black_apple_y.append(random.randint(60,180))
            black_apple_y_change.append(1.9)
        def black_apple(x,y,i):
            global screen,black_apple_img
            screen.blit(black_apple_img[i],(x,int(y)))

        # collision here
        def iscollision(bowl_x,bowl_y,apple_x,apple_y):
            distance = math.sqrt((math.pow(bowl_x - apple_x,2)) + (math.pow(bowl_y - apple_y,2)))
            if distance < 27:
                return True
            else:
                return False

        # collision here NOTE: for black apple
        def isblackcollision(bowl_x,bowl_y,black_apple_x,black_apple_y):
            distance = math.sqrt((math.pow(bowl_x - black_apple_x,2)) + (math.pow(bowl_y - black_apple_y,2)))
            if distance < 27:
                return True
            else:
                return False

        p_score = 0

        score_font = pygame.font.Font("font/ComicNeue.ttf", 40)
        def show_score():
            global screen, score_font
            score = score_font.render("Score: " + str(p_score), True, pygame.Color("white"))
            screen.blit(score, (20,20))

        game_status = False
        def game_over():
            global game_status
            game_status = True

        game_over_img = pygame.image.load("img/game-over.png")
        restart_game = pygame.font.Font("font/ComicNeue.ttf", 28)
        def show_over():
            global screen,game_over_img,restart_game
            x = restart_game.render("Press Enter to Restart the game!", True, pygame.Color("black"))
            screen.blit(game_over_img,(280,190))
            screen.blit(x,(210,420))

        running = True  
        while running:

            screen.fill(darkgray)

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        bowl_x_change = -1.6
                    elif event.key == K_RIGHT:
                        bowl_x_change = 1.6
                    elif event.key == K_RETURN:
                        if game_status == True:
                            catch_apple()
                            game_status == False
                elif event.type == KEYUP:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        bowl_x_change = 0

            # boundaries of bowl
            if bowl_x <= 10:
                bowl_x = 10
            elif bowl_x >= 756:
                bowl_x = 756

            for i in range(num_of_apple):

                if game_status == True:
                    for j in range(num_of_apple):
                        apple_x[i] = 200000
                        apple_y[i] = 200000
                    break

                # boundaries of apple
                if apple_y[i] >= 690:
                    apple_x[i] = random.randint(10,756)
                    apple_y[i] = random.randint(60,180)

                apple_y[i] += apple_y_change[i]
                apple(apple_x[i],apple_y[i], i)

                collision = iscollision(bowl_x,bowl_y,apple_x[i],apple_y[i])

                if collision:
                    catch_apple_sound = pygame.mixer.Sound("sound/game-heal.wav")
                    catch_apple_sound.set_volume(0.6)
                    catch_apple_sound.play()
                    apple_x[i] = random.randint(10,756)
                    apple_y[i] = random.randint(60,180)
                    p_score += 1

            for i in range(num_of_black_apple):

                if game_status == True:
                    for j in range(num_of_black_apple):
                        black_apple_x[i] = 200000
                        black_apple_y[i] = 200000
                    break

                # boundaries of black apple
                if black_apple_y[i] >= 690:
                    black_apple_x[i] = random.randint(10,756)
                    black_apple_y[i] = random.randint(60,180)

                black_apple_y[i] += black_apple_y_change[i]
                black_apple(black_apple_x[i],black_apple_y[i], i)

                blackcollision = isblackcollision(bowl_x,bowl_y,black_apple_x[i],black_apple_y[i])

                if blackcollision:
                    game_over_sound = pygame.mixer.Sound("sound/game-over.wav")
                    game_over_sound.set_volume(0.7)
                    game_over_sound.play()
                    game_over()
                    black_apple_x[i] = random.randint(10,756)
                    black_apple_y[i] = random.randint(60,180)

            bowl_x += bowl_x_change
            bowl(bowl_x,bowl_y)

            show_score()

            if game_status == True:
                show_over()

            pygame.display.update()

        pygame.quit()
    except pygame.error as err1:
        print(err1)
    except Exception as err2:
        print(err2)


if __name__ == "__main__":
    catch_apple()