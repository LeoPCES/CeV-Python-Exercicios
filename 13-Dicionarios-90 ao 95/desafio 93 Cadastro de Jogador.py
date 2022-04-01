'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai
ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um diiconario, incluindo o total de gols feitos durante o campeonato.'''

print('<<< Aproveitamento do Jogador >>>'.upper())
print('-='*18)
dados = {}
lista_gols = []
total = 0

dados['Jogador'] = str(input('Informe o nome do jogador: ')).title()
partida = int(input('O jogador jogou quantas partidas? --> '))

for c in range (0, partida):
    lista_gols.append(int(input(f'Quantos gols na partida {c+1}? -->')))
    total += lista_gols[c]

dados['Gols'] = lista_gols[:]
dados['Total'] = total

print('*-'*25)
print(dados)
print('*-'*25)

for k, v in dados.items():
    print(f'{k} ---> {v}')

print('*-'*25)

print(f'O jogador {dados["Jogador"]} jogou {partida} partidas!')
for contador in range(0, partida):
    print(f'==> Na partida {contador+1}, marcou {lista_gols[contador]} gols.')
print(f'Foi um total de \033[1;31m{total}\033[m gols!')

