import pygame
import random
import math

pygame.init()  # Initialize the pygame

# create the screen
screen = pygame.display.set_mode((800, 800))

# background
background = pygame.image.load('bg.png')

# title and icon
pygame.display.set_caption("Save The Farm")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 680
playerX_change = 0

# enemy
enemyImg = pygame.image.load('fox.png')
enemyX = random.randint(0, 735)
enemyY = random.randint(100, 150)
enemyX_change = 5
enemyY_change = 60

# balloon

# ready - you cant see the bullet on the screen
# fire - bullet is currently moving

balloonImg = pygame.image.load('balloon.png')
balloonX = 0
balloonY = 680
balloonX_change = 0
balloonY_change = 10
balloon_state = "ready"

score = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_balloon(x, y):
    global balloon_state
    balloon_state = "fire"
    screen.blit(balloonImg, (x + 16, y + 10))  # to make sure that balloon appears centre of the player
    # if we dont keep x+16, the balloon is going to appear at the left side of the player screen
    # y+16 - balloon apperas little bit above player


def isCollision(enemyX, enemyY, balloonX, balloonY):
    distance = math.sqrt((math.pow(enemyX - balloonX, 2)) + (
        math.pow(enemyY - balloonY, 2)))  # square root of x2-x1 wholesquare + y2-y2 whole square
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
                    balloonX = playerX  # when we fire balloon we have saved current player x cordinate inside the balloonX variable
                    fire_balloon(balloonX, balloonY)  # then we have used that everywhere instead of using playerX.
                    # This makes tha balloon not to move along with player x when it is fired and move along its Y cordinate

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # checking for boundaries of farm so it doesn't go out of bounds

        # player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        # enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 6
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -6
        enemyY += enemyY_change



    # balloon movement
    if balloonY <= 0:
        balloonY = 680
        balloon_state = "ready"

    if balloon_state == "fire":  # when we press space bar this all code will be runned .i.e baloon comes in fire state
        fire_balloon(balloonX, balloonY)
        balloonY -= balloonY_change

        # collision
    collision = isCollision(enemyX, enemyY, balloonX, balloonY)
    if collision:
        balloonY = 680
        balloon_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(100, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
