# Example pygame program
#I was here
# Import and initialize the pygame lib
import pygame

# import pygame.locals or easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
)

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((640, 640))

# Icons
icon = pygame.image.load('ninja.png')
pygame.display.set_icon(icon)

# player
playerIMG = pygame.image.load('ninja.png')
playerX = 0
playerY = 400
player_change_X = 0
player_change_Y = 0


# Obstacle
obstacleIMG = pygame.image.load('flag.png')
obstacle_pos_x = 0
obstacle_pos_y = -400


def player(x, y):
    screen.blit(playerIMG, (x, y))


def obstacle(x, y):
    screen.blit(obstacleIMG, (x, y))


# Run until the user asks to quit
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    if event.type == pygame.KEYDOWN:
        if event.key == K_RIGHT:
            player_change_X = .3
        elif event.key == K_LEFT:
            player_change_X = -.3
        elif event.key == K_UP:
            player_change_Y = -.3
        elif event.key == K_DOWN:
            player_change_Y = .3
        elif event.key == K_ESCAPE:
            running = False

    if event.type == pygame.KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            player_change_X = 0
        elif event.key == K_UP or event.key == K_DOWN:
            player_change_Y = 0

    playerX += player_change_X
    playerY += player_change_Y
    player(playerX, playerY)
    obstacle(obstacle_pos_x, obstacle_pos_y)
    pygame.display.update()

# Done! Time to quit
pygame.quit()
