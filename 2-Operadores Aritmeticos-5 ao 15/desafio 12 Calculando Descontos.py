#Calcular o descnto que o cliente quer (aprimorado)
n = float(input('Informe o valor de um produto:'))
des = float(input('Informe a porcentagem do desconto:'))
calc = 1 - des/100
produto = n * calc
print('O valor do seu produto com desconto é de: R${:.2f}'.format(produto))