from pico2d import *
import game_world
import common
import random

class Ball():
    image = None

    def __init__(self,x, y):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
            self.x = random.randint(50,common.court.w - 50) #보이랑 같게
            self.y = random.randint(80,common.court.h - 50)

    def draw(self):

        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        self.image.draw(sx, sy)

        draw_rectangle(*self.get_bb())

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)
