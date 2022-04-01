'''Crie um programa que tenha a funcao leiaint(), que vai funcionar
de forma semelhante a funcao input() do Python, so que fazendo a
validacao para aceitar apenas um valor numérico. Ex:
n = leiaint("Digite um n")'''

def leiaInt(txt):
    resul = str(input(txt))

    while resul.isnumeric() == False:
        print('\033[1;31mErro! Digite um numero inteiro válido!\033[m')
        resul = str(input(txt))
        
    if resul.isnumeric() == True:
        alt = resul
        return alt

n = leiaInt('Digite um número: ')
print(f'Voce digitou o numero {n}!')