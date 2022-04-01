'''Perguntar o salario de um funcionario e calcular o seu aumento
para salarios superiores a 1250, aumente 10%
para os inferiores ou iguais, aumente 15%'''

salario = float(input('Informe o valor do seu salário: '))
if salario>=1250:
    base = salario * 1.1
    aumento = base - salario
    print('O valor do seu aumento é de R${:.2f} e o seu salário vai ser de R${:.2f}'.format(aumento, base))
else:
    base = salario * 1.15
    aumento = base - salario
    print('O valor do seu aumento é de R${:.2f} e o seu salário vai ser de R${:.2f}'.format(aumento, base))