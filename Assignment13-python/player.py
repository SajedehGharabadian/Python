
import arcade


INSTRUCTIONS_PAGE_0 = 0
GAMEOVER = 1
WINNER = 2

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        self.stand_right_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")]
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png",mirrored = True)]

        self.walk_right_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png"),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png")]
        
        self.walk_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png",mirrored = True),
                                   arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png",mirrored = True)]

        self.center_x = 100
        self.center_y = 50
        self.current_state = INSTRUCTIONS_PAGE_0

        # self.width = 60
        # self.height = 60
        self.speed = 4

        self.pocket = []

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 200,300, arcade.color.BLACK, 45)
        arcade.draw_text("Press space and exit", 200,250, arcade.color.BLACK, 30)

    def draw_win(self):
        """
        Draw "WIN" across the screen.
        """
        output = "YOU WIN"
        arcade.draw_text(output,280,350, arcade.color.PURPLE, 45)
        arcade.draw_text("Press Escape and exit", 200,250, arcade.color.PURPLE, 30)




