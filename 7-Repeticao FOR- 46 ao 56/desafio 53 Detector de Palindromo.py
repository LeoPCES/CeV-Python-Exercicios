'''Ler uma frase e diga se é ou não PALINDROMO'''

frase = str(input('Digite uma frase: ')).upper().strip()
contador = len(frase)
lista = frase.split()
junta = ''.join(lista)

if junta[::-1] == junta:
    print('O inverso de {} é {}!\nTemos um palíndromo!'.format(junta, junta[::-1]))
else:
    print('O inverso de {} é {}!\nPortanto, não é um palíndromo!'.format(junta, junta[::-1]))


