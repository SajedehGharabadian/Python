
import time
import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self,w,h):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture("img/bird2.png"),arcade.load_texture("img/bird1.png")]
                                    

        self.speed = 19
        self.center_x = w
        self.center_y = h

        self.width = 60
        self.height = 100
        self.change_x = -1
        
        
        self.start_time = time.time()

    def move(self):
        self.end_time = time.time()
        if self.end_time - self.start_time > 1.5:
            self.speed += 0.5
            self.start_time = time.time()
        self.center_x += self.change_x * self.speed