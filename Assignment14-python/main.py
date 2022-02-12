import random
import time
import arcade

from dino import GAMEOVER, Dino
from ground import Ground
from tree import Tree
from bird import Bird


class Game(arcade.Window):
    def __init__(self):
        self.start_time_day = time.time()
        self.w = 1100
        self.h = 600
        super().__init__(self.w,self.h,'Game')
        self.background = arcade.set_background_color(arcade.color.WHITE)
        self.gravity = 0.5
        self.ground_list = arcade.SpriteList()
        self.dino = Dino()
        self.tree_list = arcade.SpriteList()
        self.start_time_tree = time.time()
        self.start_time_bird = time.time()
        self.start_time_score = time.time()
        self.flag = 1
        self.flag_tree = 1
        self.flag_day = 1
        self.flag_score = 1
        self.flag_ground = 1
        self.flag_dino = 1
        self.flag_bird = 1
        self.flag_tree_sleep = 1
        self.flag_bird_sleep = 1
        self.tree_t = random.randint(2,5)
        self.bird_t = random.randint(5,8)
        self.bird_list = arcade.SpriteList()
        self.sound = arcade.load_sound(":resources:sounds/jump4.wav")
        self.sound_game_over = arcade.load_sound(":resources:sounds/gameover2.wav")
        my_file = open("high_score.txt","r")
        self.high_score = my_file.read()

        
    
        new_ground = Ground(self.w,85)
        self.ground_list.append(new_ground)

        self.my_physics_engine = arcade.PhysicsEnginePlatformer(self.dino,[self.ground_list,self.tree_list],gravity_constant= self.gravity)
        self.tree_physics_engine = []

       

    def on_draw(self):
        arcade.start_render()
        self.dino.draw()
        arcade.draw_text('Score:' + str(self.dino.score),950,550,arcade.color.BLUE_GREEN,15)
        arcade.draw_text('HI:' + str(self.high_score),800,550,arcade.color.BLUE_GREEN,15)



        for ground in self.ground_list:
            ground.draw()

        for tree in self.tree_list:
            tree.draw()

        for bird in self.bird_list:
            bird.draw()

        if self.dino.current_state == GAMEOVER:
            self.dino.draw_game_over()
            self.flag_tree = 0
            self.flag_day = 0
            self.flag_score = 0
            self.flag_ground = 0
            self.flag_dino = 0
            self.flag_bird = 0
            for tree in self.tree_list:
                tree.speed = 0

            for bird in self.bird_list:
                bird.speed = 0

            if self.dino.score >  int(self.high_score):
                my_file = open('high_score.txt' ,'w')
                my_file.write(str(self.dino.score))
            


    def on_update(self, delta_time: float):
        self.my_physics_engine.update()
        self.end_time = time.time()

        if self.flag_day == 1:
            if self.end_time - self.start_time_day > 15 and  self.background == arcade.set_background_color(arcade.color.WHITE):
                    self.background = arcade.set_background_color(arcade.color.BLACK)
                    self.start_time_day = time.time()
                    
                
            elif self.end_time - self.start_time_day > 20 and self.background == arcade.set_background_color(arcade.color.BLACK):
                    self.background = arcade.set_background_color(arcade.color.WHITE)
                    self.start_time_day = time.time()
            

        if self.flag_tree == 1 : 
            self.flag_bird = 0       
            if self.end_time - self.start_time_tree > 2:
                new_tree = Tree(self.w,5)
                self.tree_list.append(new_tree)
                self.tree_physics_engine.append(arcade.PhysicsEnginePlatformer(new_tree,self.ground_list,gravity_constant= self.gravity))
                self.start_time_tree = time.time()
                self.flag_bird = 1


        if self.dino.score > 1000 and self.flag_bird == 1: 
            #self.end_time_bird = time.time()
            self.flag_tree = 0
            if self.end_time - self.start_time_bird > 5:
                new_bird = Bird(self.w,random.randint(100,160))
                self.bird_list.append(new_bird)
                self.start_time_bird = time.time()
                self.flag_tree = 1
            
        
        for tree in self.tree_list:
            tree.move()

        for bird in self.bird_list:
            bird.update_animation()
            bird.move()
            if bird.center_x < 0:
                    self.bird_list.remove(bird)


        if self.flag_score == 1:
            self.end_time_score = time.time()
            if self.end_time_score - self.start_time_score > 0.25:
                self.dino.score += 1
                self.start_time_score = time.time()



        for tree in self.tree_physics_engine:
            tree.update()

        if self.flag_ground == 1:

            for ground in self.ground_list:
                ground.move()

                if ground.center_x < 900 and len(self.ground_list) < 2:
                    new_ground = Ground(2400,85)
                    self.ground_list.append(new_ground)

        
        for ground in self.ground_list:
            if ground.center_x < (-900):
                self.ground_list.remove(ground)


        for tree in self.tree_list:
            if arcade.check_for_collision(self.dino,tree):
                self.dino.current_state = GAMEOVER
                arcade.play_sound(self.sound_game_over,0.25)
                tree.speed = 0
                for ground in self.ground_list:
                    ground.speed = 0

                for tree in self.tree_list:
                    tree.speed = 0

                for bird in self.bird_list:
                    bird.speed = 0
        
        
        for bird in self.bird_list:
            if arcade.check_for_collision(self.dino,bird):
                self.dino.current_state = GAMEOVER
                tree.speed = 0
                for ground in self.ground_list:
                    ground.speed = 0

                for tree in self.tree_list:
                    tree.speed = 0
                for bird in self.bird_list:
                    bird.speed = 0



    
    def on_key_press(self,key, modifiers):

        if key == arcade.key.UP:
            if self.my_physics_engine.can_jump() and self.flag_dino == 1:
                self.dino.change_y = 15
                arcade.play_sound(self.sound,0.25)

        elif key == arcade.key.DOWN:
            self.dino.texture = arcade.load_texture("img/dino_duck.png")
            self.dino.height = 40

        elif key == arcade.key.ESCAPE:
            arcade.finish_render()
            arcade.exit()
            
            

    def on_key_release(self,key, modifiers):
        self.dino.change_x = 0
        self.dino.texture = arcade.load_texture("img/dino_run0.png")





game = Game()
game.run()
        

