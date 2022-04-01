'''programa que calcula a soma entre todos os numeros impares
que são multiplos de 3 no intervalo de 1 até 500'''

inicio = str(input('Digite qlq coisa: '))
soma = 0
contador = 0
for x in range (1, 501, 2):
    if x % 3 == 0:
        contador += 1
        soma += x



print('A soma dos {} numeros são de: {}'.format(contador, soma))