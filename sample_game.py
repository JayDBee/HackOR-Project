# Example pygame program

# Import and initialize character classes
import pygame
import characters

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

ninja = pygame.image.load('ninja.png')
ninja = pygame.transform.scale(ninja, (50, 50))
flag = pygame.image.load('flag.png')
flag = pygame.transform.scale(flag, (50, 50))

mainChar = characters.Sprite(characters.DEFAULT_X, characters.DEFAULT_Y, 0, 0, ninja)
# (pygame.image.load('ninja.png')))
# mainChar.image = pygame.transform.scale(mainChar.image, (50, 50))

obstacle = characters.Sprite(0, 0, 0, 0, flag)
# pygame.image.load('flag.png'))
# obstacle.image = pygame.transform.scale(obstacle.image, (50, 50))


def render(sprite):
    screen.blit(sprite.image, (sprite.x, sprite.y))


# Run until the user asks to quit
running = True
while running:

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    '''
    ##still unusable feature
    
    if mainChar.collided_with(obstacle):
        print("keep going!")
    '''

    if event.type == pygame.KEYDOWN:
        if event.key == K_RIGHT:
            mainChar.changed_x = .6
        elif event.key == K_LEFT:
            mainChar.changed_x = -.6
        elif event.key == K_UP:
            mainChar.changed_y = -.6
        elif event.key == K_DOWN:
            mainChar.changed_y = .6
        elif event.key == K_ESCAPE:
            running = False

    if event.type == pygame.KEYUP:
        if event.key == K_RIGHT or event.key == K_LEFT:
            mainChar.changed_x = 0
        elif event.key == K_UP or event.key == K_DOWN:
            mainChar.changed_y = 0

    mainChar.x += mainChar.changed_x
    mainChar.y += mainChar.changed_y

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    render(mainChar)
    render(obstacle)
    pygame.display.update()

# Done! Time to quit
pygame.quit()
