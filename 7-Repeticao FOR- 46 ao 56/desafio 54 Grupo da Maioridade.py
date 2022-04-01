'''Ler ano de 7 pessoas e diga quantas já atingiram a maioridade'''

from datetime import  date
anoatual = date.today().year
somamenos = 0
somamais = 0

for c in range(1, 8):
    nascimento = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = anoatual - nascimento
    if idade < 18:
        somamenos += 1
    else:
        somamais += 1
print('{} pessoas não completaram 18 anos e {} pessoas já atingiu maioridade.'.format(somamenos, somamais))


