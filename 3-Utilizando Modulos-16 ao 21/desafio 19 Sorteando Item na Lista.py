from random import choice
a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Escreva o nome do primeiro aluno: ')
a3 = input('Escreva o nome do primeiro aluno: ')
a4 = input('Escreva o nome do primeiro aluno: ')
lista  = [a1, a2, a3, a4]
sorteio = choice(lista)
print('O aluno que vai apagar o quadro vai ser {}'.format(sorteio))


