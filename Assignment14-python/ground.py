import time

import arcade

class Ground(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.texture = arcade.load_texture("img/ground.png")
        self.center_y = y
        self.center_x = x


        self.width = 2400
        self.height = 28
        self.speed = 8


        self.start_time = time.time()

    def move(self):
        self.end_time = time.time()
        if self.end_time - self.start_time > 1.5:
            self.speed += 0.5
            self.start_time = time.time()
        self.center_x -= self.speed