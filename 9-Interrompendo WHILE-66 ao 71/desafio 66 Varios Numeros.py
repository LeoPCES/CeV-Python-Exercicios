'''Programa que lê varios numeros inteiros pelo teclado.
O programa só vai parar quando o usuario digitar 999, que
é a condicao de parada. No final, mostre quantos numeros
foram digitados e qual a soma entre eles, desconsiderando
o flag.'''

n = s = contador = 0

while True:
    n = int(input('Digite um numero: \n'))

    if n == 999:
        break
    contador += 1
    s += n
print(f'A soma dos {contador} números é de {s}.')


