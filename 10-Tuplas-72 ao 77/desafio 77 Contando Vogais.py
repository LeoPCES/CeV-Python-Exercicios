'''Crie um programa que tenha uma tupla com várias palavras(nao usar acentos).
Depois disso, voce deve mostrar, para cada palavra, quais são suas vogais.'''
lista = ()

while True:
    palavra = str(input('Informe uma palavra: ')).strip().lower()
    valor = ''
    lista += palavra, valor
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Opção inválida. Deseja continuar? [S/N]')).strip().upper()
    if continuar in 'N':
        break

for c in range (0, len(lista), 2):
    print(f'\nNa palavra {lista[c]} temos ', end='')
    for letra in lista[c]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

