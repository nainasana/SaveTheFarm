import pygame
import random
import math
from pygame import mixer

pygame.init()  #Initialize the pygame

# create the screen
screen = pygame.display.set_mode((800, 800))

# background
background = pygame.image.load('bg.png')

# background music
mixer.music.load('background.mp3')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("Save The Farm")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# house
houseImg = pygame.image.load('house.png')
houseX = 300
houseY = 0

# player1
player1Img = pygame.image.load('broom girl.png')
player1X = 450
player1Y = 75


# player
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 680
playerX_change = 0

# player2
player2Img = pygame.image.load('hen.png')
player2X = 250
player2Y = 735

# player3
player3Img = pygame.image.load('hen (1).png')
player3X = 620
player3Y = 700

# player4
player4Img = pygame.image.load('hen (2).png')
player4X = 120
player4Y = 600

# player5
player5Img = pygame.image.load('chicken.png')
player5X = 540
player5Y = 650

# player6
player6Img = pygame.image.load('chicks.png')
player6X = 320
player6Y = 590

# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('fox.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(200, 301))
    enemyX_change.append(4)
    enemyY_change.append(60)

# balloon

# ready - you can't see the bullet on the screen
# fire - bullet is currently moving

balloonImg = pygame.image.load('balloon.png')
balloonX = 0
balloonY = 680
balloonX_change = 0
balloonY_change = 10
balloon_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 40)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('game over text.ttf', 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (240, 330))


def house(x, y):
    screen.blit(houseImg, (x, y))

def player1(x, y):
    screen.blit(player1Img, (x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


def player2(x, y):
    screen.blit(player2Img, (x, y))


def player3(x, y):
    screen.blit(player3Img, (x, y))


def player4(x, y):
    screen.blit(player4Img, (x, y))


def player5(x, y):
    screen.blit(player5Img, (x, y))


def player6(x, y):
    screen.blit(player6Img, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_balloon(x, y):
    global balloon_state
    balloon_state = "fire"
    screen.blit(balloonImg, (x + 16, y + 10))                   # to make sure that balloon appears centre of the player
                                                                # if we dont keep x+16, the balloon is going to appear at the left side of the player screen
                                                                # y+16 - balloon appears little bit above player


def isCollision(enemyX, enemyY, balloonX, balloonY):
    distance = math.sqrt((math.pow(enemyX - balloonX, 2)) + (math.pow(enemyY - balloonY, 2)))   # square root of x2-x1 wholesquare + y2-y2 whole square
    if distance < 27:
        return True
    else:
        return False


# game loop

running = True
while running:

    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6

            if event.key == pygame.K_SPACE:
                if balloon_state == "ready":
                    balloon_Sound = mixer.Sound('balloon throw.mp3')
                    balloon_Sound.play()
                    balloonX = playerX                  # when we fire balloon we have saved current player x cordinate inside the balloonX variable
                    fire_balloon(balloonX, balloonY)    # then we have used that everywhere instead of using playerX.
                                                        # This makes tha balloon not to move along with player x when it is fired and move along its Y cordinate

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # checking for boundaries of farm, so it doesn't go out of bounds

    # player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):

        # game over
        if enemyY[i] > 555:

            for j in range(num_of_enemies):
                enemyY[j] = 2000

            game_over_text()
            pygame.mixer.music.stop()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]

        if enemyY[i] > 555:
            game_over_Sound = pygame.mixer.Sound('game over.wav')
            game_over_Sound.play(0)

        # collision
        collision = isCollision(enemyX[i], enemyY[i], balloonX, balloonY)
        if collision:
            explosion_Sound = mixer.Sound('waterballoon.mp3')
            explosion_Sound.play()
            explosion_Sound = mixer.Sound('foxcalls.mp3')
            explosion_Sound.play()
            balloonY = 680
            balloon_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(150, 150)

        enemy(enemyX[i], enemyY[i], i)

    # balloon movement
    if balloonY <= 0:
        balloonY = 680
        balloon_state = "ready"

    if balloon_state == "fire":  # when we press space bar this all code will be run .i.e balloon comes in fire state
        fire_balloon(balloonX, balloonY)
        balloonY -= balloonY_change

    house(houseX, houseY)
    player(playerX, playerY)
    player1(player1X, player1Y)
    player2(player2X, player2Y)
    player3(player3X, player3Y)
    player4(player4X, player4Y)
    player5(player5X, player5Y)
    player6(player6X, player6Y)
    show_score(textX, textY)
    pygame.display.update()
