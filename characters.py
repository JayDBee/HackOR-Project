# file for characters and their attributes
import math

# assuming squares
MAX_SCREEN_SZ = 640
MAX_SPRITE_SZ = 50

# Position of the goal
DEFAULT_FINISH_X = MAX_SCREEN_SZ / 2
DEFAULT_FINISH_Y = MAX_SPRITE_SZ
# Position of the player
DEFAULT_X = MAX_SCREEN_SZ / 2
DEFAULT_Y = MAX_SCREEN_SZ - MAX_SPRITE_SZ


class Sprite:

    def __init__(self, x, y, changed_x, changed_y, name):
        self.x = x
        self.y = y

        self.changed_x = 0
        self.changed_y = 0

        self.image = name
        self.rect = self.image.get_rect()

    def collided(self, sprite):
        distance = math.sqrt(math.pow(sprite.x - self.x, 2) + math.pow(sprite.y - self.y, 2))
        if distance >= MAX_SPRITE_SZ:
            return False
        else:
            return True

    def enforce_bounds(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= MAX_SCREEN_SZ - MAX_SPRITE_SZ:
            self.x = MAX_SCREEN_SZ - MAX_SPRITE_SZ

        if self.y <= 0:
            self.y = 0
        elif self.y >= MAX_SCREEN_SZ - MAX_SPRITE_SZ:
            self.y = MAX_SCREEN_SZ - MAX_SPRITE_SZ

    def update_sprite(self):
        self.x += self.changed_x
        self.y += self.changed_y
