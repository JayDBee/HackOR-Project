# file for characters and their attributes

DEFAULT_FINISH_X = 0
DEFAULT_FINISH_Y = -400
DEFAULT_X = 0
DEFAULT_Y = 400


class Sprite:

    def __init__(self, x, y, changed_x, changed_y, name):
        self.x = x
        self.y = y

        self.changed_x = 0
        self.changed_y = 0

        self.image = name
        self.rect = self.image.get_rect()

    def collided_with(self, sprite):
        if self.rect.colliderect(sprite.rect):
            return True
