'''Faca um programa que tenha uma funcao chamada area() que receba as dimensoes
de um terreno retangular (largura x comprimento) e mostra a area do terreno.'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno de de {largura} x {comprimento} é de {a}m²! ')

 
#inicio
l = float(input('Informe a largura em metros -->'))
c = float(input('Informe o comprimento em metros --> '))

area(l, c)







#funçao usando desempacotamento
'''def soma (*valores):
    s = 0
    for num in valores:
         s += num
    print(f'Somando os valores {valores} temos {s}')

soma(1, 5, 8)'''




#funçao usando lista
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# inicio
valores = [6, 3, 9, 2, 0]
dobra(valores)
print(valores)'''

