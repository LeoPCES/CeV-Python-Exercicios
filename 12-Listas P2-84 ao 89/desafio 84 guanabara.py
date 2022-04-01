#nome e peso de varias pessoas, guardando em uma lista
# a)quantas pessoas foram cadastradas
# b) listagem com pessoas mais pesadas
# c) listagem com pessoas mais leves

galera = []
dados = []
maior = menor = 0
#cadastro
while True:
    dados.append(str(input('Cadastre seu NOME: \n')))
    dados.append(int(input('Cadastre o seu PESO: \n')))
    if len(galera) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    galera.append(dados[:])
    dados.clear()
    cond = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SsNn':
        cond = str(input('Opção Inválida. Deseja Continuar? [S/N]'))

    if cond in 'Nn':
        break

print('=*'*10)
print(f'Foram cadastrados {len(galera)} pessoas!')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso dfoi de {menor}Kg. Peso de ',end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()
print('=*'*10)