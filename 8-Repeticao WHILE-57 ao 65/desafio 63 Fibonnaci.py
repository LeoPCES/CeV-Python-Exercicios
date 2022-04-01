'''Programa que ler um numero N inteiro qualquer e mostre na tela os n primeiros
elementos de uma Sequencia de Fibonnaci.
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8'''

print('='*8,'Sequencia de Fibonacci', '='*8)

n = int(input('Quandos termos você quer mostrar?\n'))

a = 0
b = 1
print('=*='*11)

if n == 1:
    print(a, end=' >')
    print('\033[1;31m FIM\033[m')


elif n ==2:
    print(a,' > ', b, end='')
    print(' > \033[1;31m FIM\033[m')

else:

    print ('{} > {}'.format(a, b), end='')
    cont = 3
    while cont <= n:

        c = a + b
        print(' > {}'.format(c), end='')
        a = b
        b = c
        cont +=1

    print(' > \033[1;31mFIM\033[m')






