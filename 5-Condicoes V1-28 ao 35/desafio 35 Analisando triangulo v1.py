'''Ler comp de 3 retas e diga ao usuario se elas podem ou nao
formar um triangulo'''

print('-'*5, 'Analisador de Triangulos', '-'*5)

r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados podem formar um triangulo.')
else:
    print('Os segmentos informados não podem formar um triangulo.')
