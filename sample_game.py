# Example pygame program

# Import and initialize pygame and sys libraries
# Import characters file
import pygame
import sys
import characters

# import pygame.locals or easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    MOUSEBUTTONDOWN,
)

# Icons
icon = pygame.image.load('ninja.png')
pygame.display.set_icon(icon)

# images
ninja = pygame.image.load('ninja.png')
ninja = pygame.transform.scale(ninja, (characters.MAX_SPRITE_SZ, characters.MAX_SPRITE_SZ))
flag = pygame.image.load('flag.png')
flag = pygame.transform.scale(flag, (characters.MAX_SPRITE_SZ, characters.MAX_SPRITE_SZ))

# sprites
mainChar = characters.Sprite(characters.DEFAULT_X, characters.DEFAULT_Y, 0, 0, ninja)
obstacle = characters.Sprite(characters.MAX_SCREEN_SZ / 2, 0, 0, 0, flag)

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((characters.MAX_SCREEN_SZ, characters.MAX_SCREEN_SZ))


def render(sprite):
    screen.blit(sprite.image, (sprite.x, sprite.y))


''''
----------------------------------------loops for menu screens-----------------------------
'''


def start():
    while True:
        # Fill the background with white
        screen.fill((0, 0, 0))

        click = False
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        mx, my = pygame.mouse.get_pos()

        start_button = pygame.Rect(50, 100, 200, 50)
        exit_button = pygame.Rect(50, 200, 200, 50)
        if start_button.collidepoint((mx, my)):
            if click:
                main()
        if exit_button.collidepoint((mx, my)):
            if click:
                pygame.quit()

        pygame.draw.rect(screen, (250, 250, 250), start_button)
        pygame.draw.rect(screen, (250, 250, 250), exit_button)

        pygame.display.update()


def main():
    # start of game timer
    start_ticks = pygame.time.get_ticks()

    # Run until the user asks to quit
    running = True
    while running:

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Track Key presses
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
                    total_ticks = pygame.time.get_ticks()
                    print("Total time: %2d" % (total_ticks - start_ticks))
                    running = False

            # Key lifts
            if event.type == pygame.KEYUP:
                if event.key == K_RIGHT or event.key == K_LEFT:
                    mainChar.changed_x = 0
                elif event.key == K_UP or event.key == K_DOWN:
                    mainChar.changed_y = 0

        if mainChar.collided(obstacle):
            print("Finished!")

        render(mainChar)
        render(obstacle)
        mainChar.enforce_bounds()
        mainChar.update_sprite()

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (characters.MAX_SCREEN_SZ / 2, characters.MAX_SCREEN_SZ / 2), 75)

        pygame.display.update()


# def game_over():

''''
----------------------------------------loops for menu screens-----------------------------
'''

start()
