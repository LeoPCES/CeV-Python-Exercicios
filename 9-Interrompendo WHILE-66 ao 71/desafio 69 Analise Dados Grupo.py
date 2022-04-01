'''Programa que le a idade e o sexo de VARIAS PESSOAS. A cada pessoa cadastrada,
o programa devera perguntar se o usuario quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos HOMENS foram cadastrados.
C) quantas MULHERES tem MENOS de 20 anos.'''

cont = cont2 = cont3 = 0

while True:

    idade = int(input('Informe a idade: \n'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe seu gênero: [M / F]\n')).upper().strip()[0]
    cond = ' '

    if idade > 18:
        cont += 1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade < 20:
        cont3 += 1

    while cond not in 'SN':
         cond = str(input('Deseja cadastrar mais pessoas? [S / N]')).upper().strip()[0]

    if cond == 'N':
        break


print(f'{cont} pessoas tem mais de 18 anos.')
print(f'{cont2} homens cadastrados.')
print(f'E temos {cont3} mulheres com menos de 20 anos cadastradas.')



