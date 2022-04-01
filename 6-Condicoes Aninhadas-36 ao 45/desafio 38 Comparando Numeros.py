'''Programa  para comparar dois numeros inteiros'''

print('*--*'*7, 'COMPARAÇÃO', '*--*'*7)
n1 = int(input('Informe o primeiro numero: '))
n2 = int(input('Informe o segundo numero: '))
if n1 > n2:
    print('O primeiro valor é maior.')
elif n1 < n2:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois são iguais')
