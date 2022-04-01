'''progressao aritmetica de 10 termos'''

n1 = int(input('Informe o valor do primeiro termo da p.a: '))
r = int(input('Informe o valor da razão da p.a: '))

for c in range (1,11):
    an = n1 + ((c-1)*r)
    print(an, end=' ')

