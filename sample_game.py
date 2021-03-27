# Example pygame program

# Import and initialize the pygame lib
import pygame

# import pygame.locas or easier access to key coordinates
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
screen = pygame.display.set_mode((500, 500))

# Icons
icon = pygame.image.load('ninja.png')
pygame.display.set_icon(icon)

# player
playerIMG = pygame.image.load('ninja.png')
playerX = 20
playerY = 20
player_change_X = 0
player_change_Y = 0


def player(x, y):
    screen.blit(playerIMG, (x, y))


# Run until the user asks to quit
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ''''# Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
    '''
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
    pygame.display.update()

# Done! Time to quit
pygame.quit()
