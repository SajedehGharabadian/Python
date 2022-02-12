import time

import arcade

INSTRUCTIONS_PAGE_0 = 0
GAMEOVER = 1


class Dino(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("img/dino_run0.png")
        self.center_y = 140
        self.center_x = 100
        #self.speed = 4
        self.score = 0

        self.width = 60
        self.height = 140

        self.current_state = INSTRUCTIONS_PAGE_0



    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 390,300, arcade.color.GRAPE, 50)
        arcade.draw_text("Press Escape and Exit", 390,260, arcade.color.GRAPE, 25)

        


        
