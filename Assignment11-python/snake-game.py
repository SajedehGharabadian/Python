import random
import arcade
from arcade.sprite_list.spatial_hash import check_for_collision

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
DEFAULT_LINE_HEIGHT = 45

INSTRUCTIONS_PAGE_0 = 0
GAME_OVER = 1
ADD_BODY = 2
APPLE = 3
PEAR = 4
BUMB= 5


class Snake(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.width = 8
        self.height = 8
        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.BLUE
        self.change_x = 0   #jahat taaghrat harekat mar
        self.change_y = 0
        self.score = 0
        self.center_x = SCREEN_WIDTH//2        # mogheiat dar safhe dar ebteda
        self.center_y = SCREEN_HEIGHT//2
        self.speed = 3
        self.text = None
        self.current_state = INSTRUCTIONS_PAGE_0
        self.body = []

    def move(self):

        self.body.append([self.center_x,self.center_y])

        if len(self.body) > self.score:
            self.body.pop(0)

        if self.change_x > 0:
            self.center_x += self.speed
        elif self.change_x < 0:
            self.center_x -= self.speed
        elif self.change_y > 0:
            self.center_y += self.speed
        elif self.change_y < 0:
            self.center_y -= self.speed

    def eat(self):
        if self.current_state == APPLE:
            self.score += 1 
            self.body.append([self.center_x,self.center_y])
            
        elif self.current_state == PEAR:
            self.score += 2
            self.body.append([self.center_x,self.center_y])
            self.body.append([self.center_x,self.center_y])
            

        elif self.current_state == BUMB:
            self.score -= 1
            self.body.pop(0)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.height,self.color1)

        for i in range(len(self.body)):
            if i % 2 == 0:
                arcade.draw_circle_filled(self.body[i][0],self.body[i][1],self.height,self.color1)
            elif i % 2 == 1:
                arcade.draw_circle_filled(self.body[i][0],self.body[i][1],self.height,self.color2)

        
    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 150,300, arcade.color.BLACK, 30)
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT//2

            
class Wall_Left(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 0
        self.center_y = 0
        self.width = 40
        self.height = SCREEN_HEIGHT*2
        self.color = arcade.color.BRONZE

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height+SCREEN_HEIGHT*2,self.color)

class Wall_Right(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = SCREEN_WIDTH
        self.center_y = 0
        self.width = 40
        self.height = SCREEN_HEIGHT*2
        self.color = arcade.color.BRONZE

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height+SCREEN_HEIGHT*2,self.color)
        
class Wall_Down(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 0
        self.center_y = 0
        self.width = SCREEN_WIDTH*2
        self.height = 40
        self.color = arcade.color.BRONZE

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

class Wall_UP(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = SCREEN_WIDTH//2
        self.center_y = SCREEN_HEIGHT
        self.width = SCREEN_WIDTH*2
        self.height = 40
        self.color = arcade.color.BRONZE

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.r = 8
        self.color = arcade.color.RED
        self.center_x  = random.randint(0,SCREEN_WIDTH-100)
        self.center_y = random.randint(0,SCREEN_HEIGHT-100)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)  

class Pear(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.r = 8
        self.color = arcade.color.YELLOW
        self.center_x  = random.randint(0,SCREEN_WIDTH-100)
        self.center_y = random.randint(0,SCREEN_HEIGHT-100)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)  

class Bumb(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 16
        self.height = 16
        self.r = 8
        self.color = arcade.color.BLACK
        self.center_x  = random.randint(0,SCREEN_WIDTH-100)
        self.center_y = random.randint(0,SCREEN_HEIGHT-100)

    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)  

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=SCREEN_WIDTH,height=SCREEN_HEIGHT,title="Snake Game")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake()
        self.snake.body.append(self.snake)
        self.apple = Apple()
        self.pear = Pear()
        self.bumb = Bumb()
        self.wall_left = Wall_Left()
        self.wall_right = Wall_Right()
        self.wall_down = Wall_Down()
        self.wall_up = Wall_UP()
        self.start_x = 0
        self.start_y = 10

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.bumb.draw()
        self.wall_right.draw()
        self.wall_left.draw()
        self.wall_down.draw()
        self.wall_up.draw()
        arcade.draw_text('Score:' + str(self.snake.score),self.start_x,self.start_y,arcade.color.BLACK,15)

        if self.snake.current_state == GAME_OVER:
            self.snake.draw_game_over()

        if self.snake.score < 0:
            self.snake.draw_game_over()

    
        
    def on_update(self, delta_time: float):
        self.snake.move()
        if check_for_collision(self.snake,self.apple):
            self.snake.current_state = APPLE
            self.snake.eat()
            self.snake.move()
            self.apple = Apple()

        elif check_for_collision(self.snake,self.pear):
            self.snake.current_state = PEAR
            self.snake.eat()
            self.pear = Pear()

        elif check_for_collision(self.snake,self.bumb):
            self.snake.current_state = BUMB
            self.snake.eat()
            self.bum = Bumb()

        elif check_for_collision(self.snake,self.wall_left):
            self.snake.current_state = GAME_OVER

        elif check_for_collision(self.snake,self.wall_right):
            self.snake.current_state = GAME_OVER

        elif check_for_collision(self.snake,self.wall_down):
            self.snake.current_state = GAME_OVER

        elif check_for_collision(self.snake,self.wall_up):
            self.snake.current_state = GAME_OVER
        

    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.UP:
            self.snake.change_x = 0   #jologiri az harekat movarab mar
            self.snake.change_y = 1
        elif key == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1




my_game = Game()

arcade.run()
 