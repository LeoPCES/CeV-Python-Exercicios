'''Escrever um programa que faça o computador pensar em um
numero inteiro entre 0 e 5 para o usuario tentar descobrir
qual foi o numero escolhido. O programa devera escrever na tela
se ele ganhou ou perdeu.'''

from random import randint
n = int(input('Pense em um numero entre 0 e 5: '))
sorte = randint(0,5)
if n == sorte:
    print('Parabéns, você acertou!')
else:
    print('Você perdeu!')