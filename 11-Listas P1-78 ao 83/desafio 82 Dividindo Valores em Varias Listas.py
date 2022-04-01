'''Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso,
crie duas listas extras que vao contar os valores pares e os valores impares digitados,
respectivamente. Ao final, mostre o conteudo das tres listas geradas.'''
lista = []
par = []
impar = []

while True:
    n = int(input('Acrescente um valor para a lista: '))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    cond = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while cond not in 'SsNn':
        cond = str(input('Opção inválida! --> \033[1;31m[S/N]\033[m')).strip().upper()[0]
    if cond in 'Nn':
        break

print(f'Lista de todos os numeros digitados: {lista}')
print(f'A lista formada pelos pares: {par}')
print(f'A lista formada pelos ímpares: {impar}')