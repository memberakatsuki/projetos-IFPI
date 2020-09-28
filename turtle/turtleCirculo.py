from turtle import *

def drawStar():
    pendown()
    begin_fill()
    for side in range(360):
        left(1)
        forward(1)

    end_fill()
    penup()

color('WhiteSmoke')
bgcolor('Red')

drawStar()
backward(100)
right(90)
forward(100)
drawStar()
right(90)
forward(150)
left(90)
drawStar()

hideturtle()
done()
