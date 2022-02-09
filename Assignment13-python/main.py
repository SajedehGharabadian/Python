
import time
import arcade

from player import GAMEOVER, WINNER, Player
from ground import Ground,Box
from enemy import Enemy



class Game(arcade.Window):
    def __init__(self):
        self.w = 800
        self.h = 700
        self.gravity = 0.15
        super().__init__(self.w,self.h,'game')
        self.background_image = arcade.load_texture("background.png")
        self.me = Player()
        self.ground_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.start_time = time.time()
        self.flag = 1

        self.k = arcade.Sprite(":resources:images/items/keyRed.png")
        self.k.center_x= 100
        self.k.center_y = 600
        self.k.width = 45
        self.k.height = 45 

        self.lock = arcade.Sprite(":resources:images/tiles/lockYellow.png")
        self.lock.center_x = 700
        self.lock.center_y = 120
        self.lock.width = 50
        self.lock.height = 50

        self.life = arcade.Sprite("heart.png")
        self.life.center_x = 30
        self.life.center_y = 20
        self.life.width = 30
        self.life.height = 30
        self.life.heart = 3
        self.life.change_x = 30

        for i in range(0,1000,120):
            ground = Ground(i,35)
            self.ground_list.append(ground)

        for i in range(350,600,80):
            box = Box(i,250)
            self.ground_list.append(box)

        for i in range(100,400,80):
            box = Box(i,500)
            self.ground_list.append(box)


        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.me,[self.ground_list,self.enemy_list],gravity_constant= self.gravity)

        self.enemy_physics_engine = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background_image)
        self.me.draw()

        for ground in self.ground_list:
            ground.draw()

        for enemy in self.enemy_list:
            enemy.draw()

        try:
            self.k.draw()
        except:
            pass

        self.lock.draw()

        self.life.center_x = 30
        for i in range(self.life.heart):
            
            self.life.draw()
            self.life.center_x += self.life.change_x

        if self.me.current_state == GAMEOVER:
            self.me.draw_game_over()
            self.flag = 0
            self.end_time = time.time()
            if self.end_time - self.start_time > 2:
                arcade.finish_render()
                return
               
               # self.start_time = time.time()

        elif self.me.current_state == WINNER:
            self.me.draw_win()
            self.flag = 0
            self.end_time = time.time()
            if self.end_time - self.start_time > 2:
                time.sleep(4)
                # arcade.finish_render()
                # return
                

    def on_update(self, delta_time: float):

        self.me.update_animation()

        if self.flag == 1:
            self.end_time = time.time()
            if self.end_time - self.start_time > 5:
                new_enemy = Enemy()
                self.enemy_list.append(new_enemy)
                self.enemy_physics_engine.append(arcade.PhysicsEnginePlatformer(new_enemy,self.ground_list,gravity_constant= self.gravity))
                self.start_time = time.time()

        for enemy in self.enemy_list:
            enemy.update_animation()
            

        for enemy in self.enemy_list:
            if arcade.check_for_collision(self.me,enemy):
                self.enemy_list.remove(enemy)
                self.life.heart -= 1
                if self.life.heart == 0:
                    self.me.current_state = GAMEOVER

            
        self.my_physics_engine.update()

        for item in self.enemy_physics_engine:
            item.update()

        try:
            if arcade.check_for_collision(self.me,self.k):
                self.me.pocket.append(self.k)
                del(self.k)
        except:
            pass

        if arcade.check_for_collision(self.me,self.lock) and len(self.me.pocket) == 1:
            self.lock.texture = arcade.load_texture(":resources:images/items/gemGreen.png")
            self.me.current_state = WINNER



    def on_key_press(self,key, modifiers):
        if key == arcade.key.LEFT:
            self.me.change_x = (-1 * self.me.speed)
        elif key == arcade.key.RIGHT:
            self.me.change_x = (1 * self.me.speed)

        elif key == arcade.key.UP:
            if self.my_physics_engine.can_jump():
                self.me.change_y = 10


        elif key == arcade.key.ESCAPE:
            arcade.finish_render()
            arcade.exit()

    def on_key_release(self,key, modifiers):
        self.me.change_x = 0
        


        


game = Game()

game.run()
        
