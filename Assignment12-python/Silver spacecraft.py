import math
import random
from select import select
import time
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

INSTRUCTIONS_PAGE_0 = 0
GAMEOVER = 1

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip2_orange.png")
        self.speed = 4
        self.center_x = random.randint(0,w)
        self.center_y = h
        self.angle = 180
        self.width = 48
        self.height = 48
        self.start_time = time.time()

    def move(self):
        self.end_time = time.time()
        if self.end_time - self.start_time > 1.5:
            self.speed += 0.5
            self.start_time = time.time()
        self.center_y -= self.speed
        

class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
        
    def move(self):
        angle_rad = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_rad)
        self.center_y += self.speed * math.cos(angle_rad)
        
class SpaceCreft(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width = 48
        self.height = 48
        self.center_x = w//2
        self.center_y = 48
        self.angle = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 4
        self.score = 0
        self.heart_list = []
        self.start_time = time.time()
        self.sound = arcade.Sound(":resources:sounds/hit4.wav")
        self.current_state = INSTRUCTIONS_PAGE_0
        
        
    def rotate(self):
        self.angle += self.change_angle * self.speed

    def fire(self):
        self.bullet_list.append(Bullet(self))
        self.end_time = time.time()
        arcade.play_sound(self.sound,0.25)
        if self.end_time - self.start_time > 1.5:
            arcade.stop_sound(self.sound,0.25)
            self.start_time = time.time()


    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """
        output = "Game Over"
        arcade.draw_text(output, 200,300, arcade.color.WHITE, 30)
        



class Heart(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.img = arcade.load_texture("heart.png")
        self.life = 3
        self.change_x = 30


    def draw(self):
        self.x = 0
        for i in range(self.life):
            arcade.draw_lrwh_rectangle_textured(self.x,self.y,30,30,self.img)
            self.x += self.change_x


        
            


class Game(arcade.Window):
    def __init__(self):
        self.w = 600
        self.h = 600
        super().__init__(width=self.w,height=self.h,title="Silver SpaceCraft")
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.me = SpaceCreft(self.w,self.h)
        self.enemy_list = []
        self.start_time = time.time()
        self.start_x = 500
        self.start_y = 10
        self.t = random.randint(2,5)
        self.sound_c = arcade.Sound(":resources:sounds/secret4.wav")
        self.count = 0 
        self.life = Heart()
        self.bc_game_over = arcade.load_texture("black.png")
    

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background_image)
        self.me.draw()
        arcade.draw_text('Score:' + str(self.me.score),self.start_x,self.start_y,arcade.color.WHITE,15)
        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()

        self.life.draw()
        if self.me.current_state == GAMEOVER:
            arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.bc_game_over)
            self.me.draw_game_over()
            
            
            



    def on_update(self, delta_time):
        self.me.rotate()
        self.end_time = time.time()
        if self.end_time - self.start_time > self.t:
            self.enemy_list.append(Enemy(self.w,self.h))
            self.start_time = time.time()

        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(enemy,bullet):
                    arcade.sound.play_sound(self.sound_c,30)
                    self.me.score += 1
                    self.enemy_list.remove(enemy)
                    self.me.bullet_list.remove(bullet)
                   
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.enemy_list.remove(enemy)
                self.life.life -= 1
                if self.life.life == 0:
                    self.me.current_state = GAMEOVER

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()
           
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()

        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_angle = -1

        elif key == arcade.key.LEFT:
            self.me.change_angle = 1

        elif key == arcade.key.SPACE:
            self.me.fire()


    def on_key_release(self, symbol, modifiers):
        self.me.change_angle = 0

game = Game()
arcade.run()