'''Programa que leia varios valores pelo teclado. No final da execuçao,
mostra a media de todos os valores e qual foi o MAIOR e o MENOR valor lido.
O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar
valores.'''

print('='*12, 'SOMA DOS NÚMEROS', '='*12)
condicao = ''
soma = 0
cont = 0

while condicao != 'N':

    n = int(input('Digite um número inteiro: '))

    soma += n
    cont += 1

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    condicao = str(input('Você deseja continuar? [S] SIM  [N] NÃO\n')).upper().strip()

    if condicao == 'N':
        print('FIM DO PROGRAMA')
    elif condicao != 'S' and condicao != 'N':
        print('\033[1;31mOpção Inválida.\033[m')


media = soma / cont

print('A média dos números é de {}'.format(media))
print('O maior é o {} e o menor é o {}'.format(maior, menor))




