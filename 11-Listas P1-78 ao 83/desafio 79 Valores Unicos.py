'''Crie um programa onde o usuario possa digitar varios valores numericos
e cadastre-os em uma lista. Caso o numero ja exista la dentro, ele nao sera
adicionado. No final, serao exibidos todos os valores únicos digitados, em
ordem CRESCENTE.'''

numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Deseja continuar? [S/N]')).strip().upper()
    while r not in 'SsNn':
        r = str(input('Opção inválida. --> [S/N]')).strip().upper()
    if r in 'Nn':
        break
print('-='*30)
numeros.sort()
print(f'Voce digitou os valores {numeros}')




