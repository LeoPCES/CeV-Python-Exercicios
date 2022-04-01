'''Ler um numero inteiro e mostrar se é impar ou par'''

n = int(input('Informe um número qualquer: '))
par = n % 2
if par == 0:
    print('O numero digitado é par.')
else:
    print('O numero informado é ímpar.')