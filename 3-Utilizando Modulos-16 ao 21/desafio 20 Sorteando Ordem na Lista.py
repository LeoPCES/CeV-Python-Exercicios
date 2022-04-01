from random import shuffle
a1 = str(input('Digite o primeiro aluno: '))
a2 = str(input('Digite o segundo aluno: '))
a3 = str(input('Digite o terceiro aluno: '))
a4 = str(input('Digite o quarto alun: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem do sorteio é: {}'.format(lista))

'''lista = random.sample([a1, a2, a3, a4], k=3)
print('A ordem de apresentação será {}'.format(lista))'''