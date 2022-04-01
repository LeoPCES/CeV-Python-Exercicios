'''Aprimorando o Exercicio 35 acrescentando a caracteristica
do triangulo.'''

print('-'*5, 'Analisador de Triangulos', '-'*5)

r1 = float(input('Informe o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceiro segmento: '))

#inicio: condiçao  1
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados podem formar um triangulo.')

    #inicio : condição 2
    if r1 == r2 == r3:
        print('O triângulo formado será Equilátero. ')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triânguo formado será Isósceles.')
    else:
        print('O triângulo será escaleno.')
    #fim : condiçao 2

else:
    print('Os segmentos informados não podem formar um triangulo.')
#fim: condiçao 1

