'''Aprimore o desafio 86, mostrando no final:
a) a soma de todos os pares digitados
b) a soma dos valores da terceira coluna
c) o maior valor da segunda linha'''
matriz = [[0,0,0],[0,0,0],[0,0,0]]
par = 0
colunasoma = 0
for l in range (0,3):
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para: [{l},{c}]'))
        colunasoma += matriz[l][2]
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]

print('*=-'*8)

for l in range (0,3):
    for c in range (0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('*=-'*8)
print(f'A soma de todos os pares da matriz é {par}!')
print(f'A soma de todos os elementos da terceira coluna é {colunasoma}!')
print(f'O maior valor da segunda linha é o {max(matriz[1])}')

