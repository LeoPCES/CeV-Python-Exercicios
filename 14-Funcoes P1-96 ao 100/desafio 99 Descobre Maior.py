'''Faca um programa que tenha uma funcao chamada maior(), que receba
varios parâmetros com valores inteiros. Seu programa tem que analisar
todos os valores e dizer qual deles é o maior.'''

from time import sleep


def maior(*num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} numeros!')
    print(f'O maior valor informado foi o {maior}!')


maior(2, 1, 8, 10, 3)