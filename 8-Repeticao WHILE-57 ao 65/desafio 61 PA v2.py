'''progressao aritmetica de 10 termos com while'''

n1 = int(input('Informe o valor do primeiro termo da p.a: '))
r = int(input('Informe o valor da razão da p.a: '))

contador = 9

while contador != 0:
    n1 = n1 + r
    print(n1, end=' ')
    contador -= 1








