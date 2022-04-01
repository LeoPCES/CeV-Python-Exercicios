'''Faca um programa que tenha uma funcao chamada contador(), que receba
tres parametros: inicio, fim e passo. Seu programa tem que realizar tres
contagens através da funcao criada:
a) de 1 ate 10, de 1 em 1
b) de 10 ate 0, de 2 em 2
c) uma contagem personalizada.'''

from time import sleep
def contador(inicio, fim, passo):
    print('=-'*15)
    if passo > 0:
        print(f'Contagem de {inicio} até {fim} de {passo} em {passo}!')
        for c in range(inicio, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM...')
    elif passo < 0:
        print(f'Contagem de {inicio} até {fim} de {passo*(-1)} em {passo*(-1)}!')
        for c in range(inicio, fim-1, passo):
            print(c, end=' ')
            sleep(0.5)
        print('FIM...')

#inicio
contador(1, 10, 1)
contador(10, 0, -2)
print('=-' * 15)
print('Agora personalize a contagem!')
i = int(input('Inicio --> '))
f = int(input('Fim --> '))
p = int(input('Passo --> '))
contador(i, f, p)
