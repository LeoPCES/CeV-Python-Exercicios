from math import sqrt
print('Programa para calcular a hipotenusa ')
ad = float(input('Digite o valor do cateto adjacente: '))
op = float(input('Digite o valor do cateto oposto: '))
h = ad**2 + op**2
hipo = sqrt(h)
print('O valor da hipotenusa é {}'.format(hipo))