import pygame
import random

pygame.init()

class room:
    def __init__(self, length, width, r, g, b):
        self.length = length
        self.width = width
        self.r = r
        self.g = g
        self.b = b
        screen = pygame.display.set_mode((length, width))
    def create(self):
        screen.fill((self.r, self.g, self.b))
main_room = room(640, 640, 255, 255, 255)



