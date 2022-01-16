
import turtle

num_side = [3 , 4 , 5 , 6 , 7]
side_len = [50 , 70 , 90 , 110 , 130]
t = turtle.Pen()
t.speed(0)

t.color('blue')
t.shape('turtle')

def shape(n , size) :
    for l in range (n):
        t.forward(size)
        t.left(360/n)


t.goto(0,0)

z=0
while z < (len(side_len)):
    for i in range (150, -150 , -30) :
        for j in range (100, -100 , -30):
            t.penup()
            t.goto(i,j)
            t.pendown()
            shape(num_side[z],side_len[z])
            z += 1
            