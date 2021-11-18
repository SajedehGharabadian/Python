
import turtle

num_side = [3 , 4 , 5 , 6 , 7]
t = turtle.Pen()
t.speed(0)

t.color('blue')
t.shape('turtle')

def shape(n , size) :
    for i in range (n):
        t.forward(size)
        t.left(360/n)


t.setpos(0,0)
k=0
for i in range (-200, 200 , 20) :
    for j in range (-100 , 100 , 20):
        while k < len(num_side) :
            t.penup()
            t.goto(i,j)
            t.pendown()
            shape(num_side[k],50)
            k += 1
    