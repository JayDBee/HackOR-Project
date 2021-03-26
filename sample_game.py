#Example pygame program

#Import and initialize the pygame lib
import pygame
pygame.init()


#Set uyp th drawing window
screen = pygame.display.set_mode((500,500))

#Run uyntil th user asks to quit

running = True
while running:

    #Did the user clikc the window close button?
    for even in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill the background with white
    screen.fill((255,255,255))

    #Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0,0, 255), (250,250), 75)

    #Flip the display
    pygame.display.flip()

#Done! Time to quit
pygame.quit()