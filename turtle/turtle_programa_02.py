from turtle import *
def figuras(a,b,d):
    speed(11)
    shape("turtle")

    for c in range(a):
        forward(100)
        right(72)
    right(180)
    penup()
    forward(100)

    for c in range(b):
        pendown()
        forward(100)
        right(60)
    left(90)
    penup()
    forward(120)

    for c in range(d):
        pendown()
        forward(2)
        right(1)
    
def main():
    pentagono = 5
    hexagono = 6
    circulo = 360
    figuras(pentagono,hexagono,circulo)

if __name__== '__main__':
    main()

