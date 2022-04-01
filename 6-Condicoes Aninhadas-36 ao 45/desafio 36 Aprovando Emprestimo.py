'''programa para aprovar o emprestimo de uma casa
pergunte valor da casa, salario e em quanto tempo ele vai pagar
a prestaçao mensao nao pode superior a 30% do salário'''

print ('*'*5, 'EMPRÉSTIMO BANCÁRIO', '*'*5)
#variáveis comprador
casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe o valor do seu salário: '))
anos = int(input('Em quantos anos o senhor deseja pagar?\n'))
#cálculos
aprovacao = salario * 0.3
prestacao = (casa / anos) / 12
# condições

if prestacao < aprovacao:
    print('Seu empréstimo foi Aprovado e o valor das suas prestações mensais é de R${:.2f}'.format(prestacao))
else:
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${}.\nSeu empréstimo foi Negado'.format(casa, anos, prestacao))

