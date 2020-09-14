from turtle import *
def carro_minecraft(a,b,d,e,f):
    speed(11)
    shape("turtle")


    color("Red")
    penup()
    # lado de trás do carro 
    for c in range(a):
        right(90)
        forward(250)
        right(90)
        forward(280)
        pendown()
        # parte de cima do carro
        for c in range(b):
            right(90)
            forward(100)
        left(45)
        forward(100)
        right(45)
        forward(150)
        right(45)
        forward(100)
        left(45)
        forward(100)
        #parte da frente do carro
        for c in range(d):
            right(90)
            forward(100)
        left(45)
        
        # roda dianteira
        for c in range(e):
            color("Black")
            forward(0.8)
            right(1)
        color("Red")
        penup()
        right(45)
        forward(66)
        pendown()
        forward(200)
        left(45)
        
        # roda traseira
        for c in range(f):
            color("Black")
            forward(0.8)
            right(1)
        color("Red")
        penup()
        right(45)
        forward(66)
        pendown()
        forward(60)
        penup()
        forward(100)
    done()

def main():
    lado_traseiro = 1
    parte_cima = 2
    lado_dianteiro = 2
    roda_dianteira = 360
    roda_traseira = 360
    carro_minecraft(lado_traseiro,parte_cima,lado_dianteiro,roda_dianteira,roda_traseira)

if __name__ == '__main__':
    main()
