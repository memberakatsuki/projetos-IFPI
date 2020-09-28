from turtle import*
from time import sleep
    
def drawPlanet(tamanho,cor):
    color(cor)
    begin_fill()
    penup()
    backward(100)
    left(90)
    pendown()
    for c in range(360):
        right(1)
        forward(tamanho)
        
    end_fill()
    penup()


def main():
    bgcolor('MidnightBlue')
    print('==========SEU_PLANETA===========')
    tamanho = int(input('Digite o tamanho que você deseja o planeta: '))
    if tamanho >=4:
        print('esse tamnho, seu planeta não vai parecer de forma correta')
        pergunta = str(input("você deseja continuar?[s-sim/n-não] :")).upper()
        if pergunta == 'S':
            print('ok')
            print('Agora volte para a outra tela AZUL que apareceu, você verá')
            drawPlanet(tamanho, 'Green')
            hideturtle()
            done()
        else:
            print('Você escolheu não contiuar')
            sleep(3)
            False
    elif tamanho >= 1:
        print('Agora volte para a outra tela AZUL que apareceu, você verá')
        drawPlanet(tamanho, 'Green')
        hideturtle()
        done()
    elif tamanho <= 0:
        print('esse tamanho não está no padrão, e por isso o programa foi encerrado')
        sleep(3)
        False

if __name__ == '__main__':
    main()
