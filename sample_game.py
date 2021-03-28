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

start_ticks = 0
total_ticks = 0

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

# Done! Time to quit
pygame.quit()
