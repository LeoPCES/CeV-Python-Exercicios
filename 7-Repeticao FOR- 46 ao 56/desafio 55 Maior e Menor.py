'''programa para ler o maior e o menor peso de 5 pessoas'''
alt = 0
maior = 0
menor = 0
for cont in range (1, 6):
    peso = int(input('Informe o peso da {}ª pessoa: '.format(cont)))
    if cont ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {} kg'.format(maior))
print('O menor peso lido foi de {} kg'.format(menor))



