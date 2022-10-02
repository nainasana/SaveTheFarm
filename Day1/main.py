import pygame

pygame.init()  #initializing pygame package


#screen
screen = pygame.display.set_mode((1167, 700))

# Background
background = pygame.image.load('background.jpg')


#caption and icon
pygame.display.set_caption("SAVE THE FARM")
icon = pygame.image.load('thumbs.png')
pygame.display.set_icon(icon)





#game loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill((255, 255, 255))

    # Background Image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



































pygame.display.update()