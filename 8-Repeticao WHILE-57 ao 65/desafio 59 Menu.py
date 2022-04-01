'''Programa que leia 2 valores e mostra um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
O programa devera realizar a operacao solicitada em cada caso.'''

print('\033[1;31m ================ MENU ================\033[m')
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
soma = n1 + n2
produto = n1 * n2
maior = 0
menor = 0
condicao = False
print('''
======================
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
======================''')

cond = int(input('Digite uma opção: '))
while cond < 6 and condicao != True:

    if cond == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        condicao = True
    elif cond == 2:
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
        condicao = True
    elif cond == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O numero maior numero é {}'.format(maior))
        condicao = True
    elif cond == 4:
        n1 = float(input('Digite o primeiro numero: '))
        n2 = float(input('Digite o segundo numero: '))
        print('''
======================
[1] somar
[2] multiplicar
[3] maior
[4] novos numeros
[5] sair do programa
======================''')
        cond = int(input('Digite uma opção: '))
        soma = n1 + n2
        produto = n1 * n2
        maior = 0
        menor = 0

        condicao = False
    else:
        print('Você saiu do programa')
        condicao = True

print('Obrigado por utilizar o programa')







