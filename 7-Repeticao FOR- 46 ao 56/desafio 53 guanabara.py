#variaveis
frase = str(input('Digite uma frase: ')).upper().strip()
lista = frase.split()
junto = ''.join(lista)
soma = ''

# condiçao
for cont in range(len(junto)-1, -1, -1):
    soma += junto[cont]

if junto == soma:
    print('O inverso de {} é {}, portanto:\nÉ um palíndromo'.format(junto, soma))
else:
    print('O inverso de {} é {}, portanto:\nNão um palíndromo'.format(junto, soma))

