'''Melhorando desafio 61, perguntando para o usuario se ele quer mostrar mais
termos. O programa encerra quando ele disser que quer mostrar 0 termos.'''

n1 = int(input('Informe o valor do primeiro termo da p.a: '))
r = int(input('Informe o valor da razão da p.a: '))

contador = 1
contagem = 5


while contagem != 0:
#primeiros 10 termos
    while contador <= 10:
        n1 = n1 + r
        print('\033[1;31m',n1, end=' ')
        contador += 1
    print('\033[m')

    print('')
#termos a mais (usuário digita quantos ele quer)
    termo2 = int(input('Quantos termos você quer mostrar a mais?\n'))
    cont = 1

    if termo2 !=0:
        while cont <= termo2:
            n1 = n1 + r
            print(n1, end=' ')
            cont += 1
    else:
            contagem = 0















