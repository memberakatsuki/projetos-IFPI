from random import randint
def jogo(numero,score):
    while True:
        pergunta = str(input("\nGostaria de somar mais um número [s/n]: ")).upper()[0]
        if pergunta == 'S':
            numero = randint(1, 10)
            score += numero
            print(f'''
Seu próximo número é {numero}
Sua pontuação agora é {score}''')
        elif pergunta == 'N':
            print(f'Sua pontuação final é {score}')
            if score > 21 or score < 21:
                print('Que pena!')
            elif score == 21:
                print('Você VENCEU!')
            break

def main():
    numero = randint(1, 10)
    score = numero
    print('''
Vinte e um!
==========
Tente fazer exatamente 21 pontos!
    ''')
    print(f'''
Seu próximo número é {numero}
Sua pontuação agora é {score}
    ''')
    jogo(numero,score)

if __name__ == '__main__':
    main()