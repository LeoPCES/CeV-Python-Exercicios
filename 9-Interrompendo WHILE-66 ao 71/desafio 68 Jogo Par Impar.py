'''Faca um programa que jogue par ou impar com o computador. O jogo so sera
interrompido quando o jogador PERDER, mostrando o total de vitorias consecutivas
que ele conquistou no final do jogo.'''

from random import randint
from time import sleep

print('=*'*8, 'VAMOS JGOAR IMPAR & PAR', '=*'*8)
cont = 0

while True:

    aleatorio = randint(0, 10)
    num = int(input('Aposte seu número: \n'))
    cond = str(input('Par ou Impar? [P] PAR [I] IMPAR\n')).upper().strip()[0]
    soma = aleatorio + num

    if soma % 2 == 0 and cond == 'P':
        print(f'Você jogou {num} e o computador {aleatorio}. TOTAL = {soma} é PAR')
        print('\033[1;31mParabéns, você ganhou!\033[m\nVamos jogar novamente!')
        cont += 1
        sleep(3)

    elif soma % 2 != 0 and cond == 'I':

        print(f'Você jogou {num} e o computador {aleatorio}. TOTAL = {soma} é ÍMPAR')
        print('\033[1;31mParabéns, você ganhou!\033[m\nVamos jogar novamente!')
        cont += 1
        sleep(1)

    else:
        print(f'Você jogou {num} e o computador {aleatorio}')
        print(f'\033[1;31mVocê perdeu!\033[m\nVocê venceu {cont} vezes')
        break















