'''Faca um programa que leia 5 valores numericos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posicoes na lista.'''

print('='*40)
print(f'{"LISTINHA":^40}')
print('='*40)
valor = []

for cont in range (0,5):
    valor.append(int(input(f'Digite um número na posição {cont}: ')))

print(f'Você digitou os valores {valor}')
print(f'O maior valor digitado foi {max(valor)} na posição {valor.index(max(valor))}')

print(f'O menor valor digitado foi {min(valor)} na posição {valor.index(min(valor))}')

