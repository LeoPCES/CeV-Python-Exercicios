'''Programa que leia um numero e mostre o seu fatorial.'''

print("="*10, 'CÁLCULO DE FATORIAL', '='*10)

n = int(input('Informe um número: '))
c = n
f = 1

print('Calculando {}! = '.format(n), end='')

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end = '')
    f = f * c
    c -= 1

print('{}'.format(f))


'''Usando for:
n1 = int(input('Digite um número inteiro qualquer: '))
acumulador = 1
for n1 in range(n1, 0, -1):
    acumulador *= n1
print('O produto de todos os números é {}'.format(acumulador))'''




















