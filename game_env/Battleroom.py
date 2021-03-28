import Objects_and_stuff
import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_z,
    K_x,
)

running = True
screen = pygame.display.set_mode((Objects_and_stuff.main_room.length, Objects_and_stuff.main_room.width))
select = 0
HP = 100
EHP = 100


while running:
    screen.fill((Objects_and_stuff.main_room.r, Objects_and_stuff.main_room.g, Objects_and_stuff.main_room.b))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if select <= 2:
                if event.key == K_LEFT:
                    select = select + 1
            elif select >= 0:
                if event.key == K_RIGHT:
                    select = select - 1
            elif event.key == K_x:
                if select == 0:
                    print("you got away")
                elif select == 1:
                    HP = HP + 10
                    HP = HP - 5
                    print("you were healed")
                elif select == 2:
                    EHP = EHP - 20
                    HP = HP - 10
                    print("Attack!")
