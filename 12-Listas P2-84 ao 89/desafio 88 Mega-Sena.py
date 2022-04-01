'''Faca um programa que de palpites da MEGA SENA. O programa vai perguntar
quantos jogos serao gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta. No caso, fiz o da loto facil.'''

from random import randint
from time import sleep
lista = []
temp = []
resul = []
print(f'{"PALPITES ONLINE":*^30}')

n = int(input('Quantos palpites você deseja?\n'))
while n > 0:
    while len(resul) < 15:
        temp.append(randint(1, 25))
        for element in temp:
            if element not in resul:
                resul.append(element)

    lista.append(resul[:])
    resul.clear()
    temp.clear()
    n-=1

for c, j in enumerate(lista):
    j.sort()
    print(f'Jogo {c+1}: {j}')
    sleep(1)

print(f'{"BOA SORTE":^30}')