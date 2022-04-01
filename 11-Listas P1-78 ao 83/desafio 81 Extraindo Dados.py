'''Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso, mostre:
A) quantos numeros foram digitados
B) A lista de valores, ordenada em forma DECRESCENTE
C)se o valor 5 foi digitado e está ou NAO na LISTA.'''

lista = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cond = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SsNn':
        cond = str(input('Opçao inválida! ---> \033[1;31m[S/N]\033[m')).strip().upper()[0]
    if cond in 'Nn':
        break

print(f'Foi digitados {len(lista)} numeros.')
lista.sort(reverse=True)
print(f'A lista em forma decrescente: {lista}')
if 5 in lista:
    print('O numero 5 foi digitado e está na lista.')
else:
    print('O numero 5 não foi digitado.')