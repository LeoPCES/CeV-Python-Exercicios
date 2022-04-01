'''Criar um programa que simula um caixa eletronico. No inicio,
pergunte ao usuario qual o valor a ser sacado (inteiro) e o programa
vai informar quantas cedulas de cada valor serao entregues.
OBS: Considere que o caixa so possui notas de 50, 20, 10 e 1.'''

print('=*'*30)
print('{:^60}'.format('BANCO DU LEO'))
print('=*'*30)
print('Somente cédulas de R$ 50,00 / R$ 20,00 / R$ 10 / R$ 1,00')

valor = int(input('Informe o valor para saque. R$ '))
print()
print('='* 30)
print()

while True:
    if valor % 50 == 0:
        print(f'Serão entregues {valor / 50:.0f} cédulas de R$50,00')
        break

    elif valor % 50 != 0:
        resto50 = valor % 50
        resto20 = resto50 % 20

        if resto20 == 0:
            print(f'Total de {valor // 50:.0f} cédulas de R$50,00')
            print(f'Total de {resto50 // 20:.0f} cédulas de R$20,00')
            break
        elif resto20 !=0:
            print(f'Total de {valor // 50:.0f} cédulas de R$50,00')
            print(f'Total de {resto50 // 20:.0f} cédulas de R$20,00')
            print(f'Total de {resto20 // 10} cédulas de R$10,00')
            print(f'Total de {(resto20 % 10) / 1:.0f} cédulas de R$1,00')
            break










