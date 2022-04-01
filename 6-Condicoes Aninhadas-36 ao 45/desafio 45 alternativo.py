'''Programa em que o computador joga JO KEN PO -- Falta Terminar'''

from random import randint
print(" JO KEN PO ")
lista = ('PEDRA', 'PAPEL', 'TESOURA')
print('''ESCOLHA UMA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
escolha = int(input('Digite uma opção: '))

computador = randint(0, 2)
print('Computador jogou: {}'.format(lista[computador]))
print('Voce jogou: {}'.format(lista[escolha]))
