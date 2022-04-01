'''Programa que le o nome e o preco de varios produtos. O programa
devera perguntar se o usuario vai continuar. No final, mostre:
A) qual o total gasto na compra.
B) quantos produtos custam mais de R$1000,00
C) qual o nome do produto mais barato.'''

soma = cont = cont2 = menor = 0
barato = ' '
print('='*30)
print('{:^30}'.format('SUPERMERCADO DU BOM'))
#print(f'{:^30} SUPERMERCADO DU BOM')
print('='*30)
while True:
    nome = str(input('Qual é o nome do produto cadastrado? \n')).strip()
    valor = float(input('Informe o preço: \n'))
    cond = ' '

    #a
    soma += valor
    #b
    if valor > 1000:
        cont += 1
    #c
    cont2 += 1
    if cont2 == 1:
        menor = valor
        barato = nome
    else:
        if valor < menor:
            menor = valor
            barato = nome

    while cond not in 'SN':
        cond = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if cond == 'N':
        break

print(f'Total das compras é de R${soma:.2f}')
print(f'{cont} produtos custam mais de R$1000,00')
print(f'O produto mais barato é: {barato}')
