import pygame
import random

pygame.init()

def create(length, width):
    pygame.display.set_mode((length, width))
class room:
    def __init__(self, length, width, r, g, b):
        self.length = length
        self.width = width
        self.r = r
        self.g = g
        self.b = b
        screen = pygame.display.set_mode((length, width))

main_room = room(640, 640, 255, 255, 255)

create(main_room.length, main_room.width)

