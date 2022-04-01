'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final, mostre:
A) quantas vezes apareceu o valor 9.
B) em que posicao foi digitado o primeiro valor 3
C) Quais foram os numeros PARES.'''

num = int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: '))

print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O 3 apareceu pela primeira vez na posição {num.index(3)+1}ª')

print('Os pares digitados são: ', end= '')
for c in num:
    if c % 2 == 0:
        print(c, end=' > ')

print('FIM')

