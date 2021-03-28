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

DEFAULT_HEALTH = 100
BASE_ATTACK = 20
BASE_HEAL = 25


class Sprite:

    def __init__(self, x, y, name):
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


class Character(Sprite):
    def __init__(self, x, y, name):
        Sprite.__init__(self, x, y, name)

        self.killed = 0
        self.health = DEFAULT_HEALTH
        self.attack = BASE_ATTACK

    def attack(self, sprite):
        sprite.health -= self.attack

    # def movement(self):


class Monster(Character):
    def __init__(self, x, y, name):
        Character.__init__(self, x, y, name)

    # heavy attack
    def attack_2(self, sprite):
        sprite.health -= self.attack * 1.5


class Player(Character):
    def __init__(self, x, y, name):
        Character.__init__(self, x, y, name)

        self.heal = BASE_HEAL

    def heal(self):
        self.health += self.heal
