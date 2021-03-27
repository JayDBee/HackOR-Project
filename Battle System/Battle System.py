
import pygame

#set up variables
battlesystem = True
Position = 0

#Game Loop
while battlesystem == True:
    if event.type == pygame.KEYDOWN:
        if event.key == K.Right:
             Position = Position + 1