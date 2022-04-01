'''Nome e peso de varias pessoas, guardando em uma lista, no final, mostre:
a) quantas pessoas foram cadastradas
b) listagem com pessoas mais pesadas
c) listagem com pessoas mais leves'''

galera = []
dados = []
listapesado = []
listaleve = []
#cadastro
while True:
    dados.append(str(input('Cadastre seu NOME: \n')))
    dados.append(int(input('Cadastre o seu PESO: \n')))
    galera.append(dados[:])
    dados.clear()
    cond = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SsNn':
        cond = str(input('Opção Inválida. Deseja Continuar? [S/N]'))

    if cond in 'Nn':
        break
#lista das pessoas pesadas e leves
for p in galera:
    if p[1] >= 100:
        listapesado.append(p[0])

    elif p[1] <= 70:
        listaleve.append(p[0])
print('=*'*10)
print(f'Foram cadastrados {len(galera)} pessoas!')
print(f'Lista com as pessoas mais pesadas: \033[1;31m{listapesado}\033[m')
print(f'Lista com as pessoas mais leves: \033[1;31m{listaleve}\033[m')
print('=*'*10)