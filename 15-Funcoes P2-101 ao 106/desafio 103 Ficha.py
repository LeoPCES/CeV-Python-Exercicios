'''Faca um programa que tenha uma funcao chamda ficha(), que receba dois parametros
opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser
capaz de mostrar a ficha do jogador, mesmo que algum dado nao tenha sido informado
corretamente.'''

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador fez {nome} fez {gols} gol(s) no campeonato!')

#principal
jogador = str(input('Informe o nome do jogador --> '))
g = str(input(f'Quantos gols o {jogador} fez? --> '))

if g.isnumeric():
    g = int(g)
else:
    g = 0
if jogador.strip() == '':
    ficha(gols = g)
else:
    ficha(jogador, g)
