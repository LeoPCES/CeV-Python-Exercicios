'''ler 6 numeros inteiros e mostrar apenas a soma dos pares, se digitar impar desconsidera.'''

print('Digite 6 numeros e somarei a soma dos nº pares: ')
soma = 0
cont = 0
for c in range(0,6):
    n = int(input('Informe um numero: \n'))
    if n % 2 == 0:
        soma += n
        cont += 1
print('A soma dos {} pares digitados é de {}.'.format(cont, soma))
