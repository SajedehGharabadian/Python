
import random
import time
import arcade

class Tree(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__()
        self.texture = random.choice([arcade.load_texture("img/cactous0.png"),
                                      arcade.load_texture("img/cactus1.png")])

        self.speed = 8
        self.center_x = w
        self.center_y = 140

        self.width = 60
        self.height = 150
        
        
        self.start_time = time.time()

    def move(self):
        self.end_time = time.time()
        if self.end_time - self.start_time > 0.25:
            self.speed += 0.75
            self.start_time = time.time()
        self.center_x -= self.speed