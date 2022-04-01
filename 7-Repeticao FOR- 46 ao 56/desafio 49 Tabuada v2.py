'''#relembra desafio 9, só que com a condiçao que o usuario escolher'''

print('*---------*'*4, 'ESCOLHA UMA TABOADA', '*---------*'*4 )
n = int(input('Informe um número que mostrarei a taboada: '))

for c in range(1, 11):
    calculo = n * c
    print('{} x {} = {}'.format(n, c, calculo))
    print('='*12)
