lista = ()
soma = cont = 0
while True:
    produto = str(input('Digite o nome do produto: ')).upper().strip()
    valor = float(input('Digite o preço: '))
    lista += produto, valor
    continuar = str(input('Quer continuar? [S/N]')).strip()
    while continuar not in 'SsNn':
        continuar = str(input('Tente novamente. Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print('-=' * 18)
print(f'{"LISTA DE PRODUTOS":^36}\n')
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<25} R$ {lista[c + 1]:.2f}')
    cont += 1
for c in range(1, len(lista), 2):
    soma += lista[c]
print()
print(f'Você comprou {cont} produtos e a soma', end=' ')
print(f'deles foi de R$ {soma:.2f}')
print('-=' * 18)