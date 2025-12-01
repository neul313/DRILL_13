from pico2d import *
import game_world
import common
import random


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

        self.x = random.randint(50, int(common.court.w) - 50)
        self.y = random.randint(80, int(common.court.h) - 50)

    def draw(self):
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collisions(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)