'''Crie um programa que leia varios numeros inteiros. O programa so para
quando o usuario digitar 999, que é a condicao de parada. No final, mostre
quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando flag).'''
print('=*=*'*8, 'DIGITE 999 PARA PARAR', '=*=*'*8)
n = 0
soma = 0
cont = 0
condicao = 0

while n != 999:

    n = int(input('Digite um número inteiro: \n'))
    soma += n
    cont += 1
    if n == 999:
        condicao = soma - 999
        print('A soma entre os \033[1;97m{}\033[m numeros digitados é de \033[1;31m{}\033[m '.format(cont, condicao))





