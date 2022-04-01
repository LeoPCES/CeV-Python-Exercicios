'''Faca um programa que tenha uma lista chamada números e duas
funcoes chamadas sorteia() e somapar(). A primeira vai sortear
5 numeros e vai coloca-las dentro de uma lista e a segunda funcao
vai mostrar a soma entre todos os valores PARES sorteados pela funcao
anterior.'''
from random import randint


def sorteia(lista):
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteando os {len(numeros)} valores da lista: {numeros}')


def soma_par():
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'Somando os pares de {numeros}, temos {soma}.')



#inicio
numeros = []
sorteia(numeros)
soma_par()
