from random import *

def msg(txt):
    print('=' * (len(txt) + 4))
    print(f'| {txt} |')
    print('=' * (len(txt) + 4))

def tela():
    print('''
    Existe um super prêmio de uma destas 3 portas!
    Adivinhe qual é a porta certa para ganhar o prêmio!''')
    for c in range(1,4):
        print('''
     ______
    |      |
    |  {c} |
    |    O |
    |______| 
    ''')
def main():
    msg('Porta da Fortuna')
    tela()
    score = 0
    while True:
        print("\nEscolha uma porta (1, 2 ou 3) : ", end='')
        portaEscolhida = int(input())
        portaCerta = randint(1,3)
        print(f"A porta escolhida foi a {portaEscolhida}")
        print(f"A porta certa é {portaCerta}")
        if portaEscolhida == portaCerta:
            print('Parabéns!')
            score += 1
        else:
            print('Que peninha!')
            score += 0
        pergunta = str(input('\nVocê quer jogar novamente [s/n]: ')).upper()[0]

        if pergunta == 'N':
            break
    print('Obrigado por jogar')
    print(f'sua pontuação final é {score}')

if __name__ == '__main__':
    main()