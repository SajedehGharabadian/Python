import arcade


center_x = 310
center_y = 100
count1 = 0
count2 = 0

arcade.Window(400,400,"Draw Square")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

for i in range(10):
    if i % 2 == 0:
        count2 = 0
        for j in range(10):
            if j % 2 == 0:
                arcade.draw_circle_filled(center_x-count1,center_y+count2,10,arcade.color.BLUE)
                count2 += 25
            elif j % 2 == 1 :
                arcade.draw_circle_filled(center_x-count1,center_y+count2,10,arcade.color.RED)
                count2 += 25
    elif i % 2 == 1:
        count2 = 0
        for j in range(10):
            if j % 2 == 0:
                arcade.draw_circle_filled(center_x-count1,center_y+count2,10,arcade.color.RED)
                count2 += 25
            elif j % 2 == 1 :
                arcade.draw_circle_filled(center_x-count1,center_y+count2,10,arcade.color.BLUE)
                count2 += 25
    count1 += 25





arcade.finish_render()

arcade.run()