'''Crie um programa que vai gerar 5 numeros aleatorios e colocar em uma tupla.
Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o
maior valor que estão na tupla.'''

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os valores sorteados foram: ')
for n in num:
    print(f'{n} ', end='')
print()
print(f'O maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')

