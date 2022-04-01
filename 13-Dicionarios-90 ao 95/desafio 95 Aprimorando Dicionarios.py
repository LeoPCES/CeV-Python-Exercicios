'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualizacao de detalhes do aproveitamento de cada jogador.'''

print('<<< Aproveitamento de Jogadores >>>'.upper())
print('-='*18)
lista_dados = []

while True:
    dados = {}
    lista_gols = []
    total = 0
    dados['Jogador'] = str(input('Informe o nome do jogador: ')).title()
    partida = int(input('O jogador jogou quantas partidas? --> '))
    for c in range(0, partida):
        lista_gols.append(int(input(f'Quantos gols na partida {c+1}? -->')))
        total += lista_gols[c]
    dados['Gols'] = lista_gols[:]
    dados['Total'] = total
    lista_dados.append(dados.copy())
    dados.clear()
    resp = str(input('Deseja continuar? [S/N] =--> ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('Opção Inválida! [S/N] =--> ')).upper().strip()[0]
    if resp in 'Nn':
        break

print('-='*30)
print(lista_dados)
print('-='*30)
print(f'{"cod":<3} {"Jogador":<14} {"Gols":<14} {"Total"}')

for cont, d in enumerate(lista_dados):
    print(f'{cont:<3} {d["Jogador"]:<14} {d["Gols"]} {d["Total"]:^14}')

while True:
    cond = int(input(f'Mostrar dados de qual jogador? [999 INTERROMPE] =--> '))
    if cond == 999:
        break
    print(f'Levantamento do Jogador {lista_dados[cond]["Jogador"]}')
    for contador in range(0, len(lista_dados[cond]["Gols"])):
        print(f'--> Na partida {contador+1}, marcou {lista_dados[cond]["Gols"][contador]}.')

print('Fim do programa...')



