'''Programa para sortear exercicios para fazer Revisao.'''

from random import randint
from time import sleep


lista = ["Tipos Primitivos", "Operadores Aritmeticos", "Modulos", "Manipulando Texto",
         "Condicoes V1", "Condicoes Aninhadas", "Repeticao For", "Repeticao While",
         "Interrompendo While", "Tuplas", "Listas p1", "Listas p2",
         "Dicionarios", "Funcoes p1", "Funcoes p2", "Erros e Excecoes"]
temp = []
resultado = []

assunto = int(input("Quantos assuntos você deseja revisar? \n"))

# Sorteio dos Assuntos
while assunto > 0:
    temp.append(randint(0, 15))
    for element in temp:
        if element not in resultado:
            resultado.append(element)
            assunto -= 1
resultado.sort()


exercicios = []
# Mostrando os Assuntos
for nome in resultado:
    print(f'Voce vai estudar --> \033[0;31m {lista[nome]} \033[m')
    x1 = int(input(f'Qual o primeiro exercicio da materia \033[0;32m {lista[nome]} \033[m? \n'))
    x2 = int(input(f'Qual o ultimo exercicio da materia \033[0;32m {lista[nome]} \033[m? \n'))
    print('-='*30)
    sorteio = randint(x1, x2)
    exercicios.append(sorteio)

print()

# Mostrando os Exercicios
for question in exercicios:
    print(f'Você irá revisar exercício --> \033[1;36m{question}\033[m')
    sleep(0.5)






