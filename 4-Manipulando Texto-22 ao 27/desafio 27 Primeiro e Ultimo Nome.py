'''Leia nome completo da pessoa mostrando em seguida
o primeiro e o último nome separadamente'''

nome = str(input('Informe o seu nome: ')).title().strip()
lista = nome.split()
lista2 = len(lista) - 1
print('Primeiro nome: {}'.format(lista[0]))
print('Ultimo nome: {}'.format(lista[lista2]))