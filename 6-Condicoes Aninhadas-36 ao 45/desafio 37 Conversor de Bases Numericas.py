'''Escreva um programa que leia numero inteiro
e peça para o usuario escolher qual sera a base
de conversao'''

inteiro = int(input('Informe um número inteiro para conversão: '))
n = int(input('Digite 1 para conversão em Binário\nDigite 2 para Octal\nDigite 3 para hexadecimal\nInforme aqui: '))
if n==1:
    print(bin(inteiro)[2:], 'em binários.')
elif n==2:
    print(oct(inteiro)[2:], 'em octal')
elif n==3:
    print(hex(inteiro)[2:], 'em hexadecimal')
else:
    print('Informe uma opção correta!')

