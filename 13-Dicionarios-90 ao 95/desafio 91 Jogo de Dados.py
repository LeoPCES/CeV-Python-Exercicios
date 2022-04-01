'''Crie um programa onde 4 jogadores joguem um dado  e tenham resultados aleatorios.
Guarde esses resultados em um dicionário. No final, coloque esse dicionario em ordem
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep
from operator import itemgetter
jogos = {}
lista = []
ranking = []
for c in range (1, 5):
    lista.append(f'Jogador{c}')
#jogando valor aleatorio no dicionário
for p in lista:
    jogos[p] = randint(1, 6)

print(f'{"VALORES SORTEADOS":^30}')

for k, v in jogos.items():
    print(f'{k} acertou {v} no lançamento.')
    sleep(1)

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('-='*25)
print('<<< RANKING DOS JOGADORES >>>')
print(ranking)
print()
for i, v in enumerate(ranking):
    print(f'{i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)
print('fim do programa...')





