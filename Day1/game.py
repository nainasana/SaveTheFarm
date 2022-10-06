import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
import pygame
import random

pygame.init() #Initialize the pygame

#create the screen
screen = pygame.display.set_mode((800, 800))


#background
background_img = pygame.image.load("bg.png").convert()


#title and icon
pygame.display.set_caption("Save The Farm")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#player
playerImg = pygame.image.load('player.png')
playerX = 400
playerY = 680
playerX_change = 0


#enemy
enemyImg = pygame.image.load('fox.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(100, 150)
enemyX_change = 1.5
enemyY_change = 25

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    screen.blit(enemyImg, (x, y))


#game loop
running = True
while running:

    screen.fill((0, 0, 0))

    #background image
    screen.blit(background_img, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -6
            if event.key == pygame.K_RIGHT:
                playerX_change = 6

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


#checking for boundaries of farm so it doesn't go out of bounds

    #player movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

#enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 6
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -6
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
