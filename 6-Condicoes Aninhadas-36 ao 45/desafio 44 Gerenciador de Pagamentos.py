'''Valor a ser pago por um produto, considerando o preço normal
e condiçao de pagamento:
dinheiro/cheque --> 10% de desconto
a vista no cartao de desconto --> 5% de desconto
em ate 2x no cartão --> preço normal
3x ou mais --> 20% de juros'''

print('#--#'*6, 'PROGRAMA PREÇO LOJA', '#--#'*6)
#dados usuario
produto = float(input('Informe o valor do produto. R$'))
print('Insira a opção de pagamento: \n1 para à vista dinheiro/cheque')
print('2 para à vista no cartão de desconto')
print('3 para em até 2x no cartão')
print('4 para 3x ou mais no cartão')
n = int(input('Insira a opção: '))

#condições
if n == 1:
    preco = produto * 0.9
    print('O valor a ser pago será de R${:.2f}'.format(preco))
elif n == 2:
    preco = produto * 0.95
    print('O valor a ser pago será de R${:.2f}'.format(preco))
elif n ==3:
    print('O valor a ser pago será de R${:.2f}'.format(produto))
else:
    preco = produto * 1.2
    print('O valor a ser pago será de R${:.2f}'.format(preco))

