'''Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuario possa
mostrar as notas de cada aluno individualmente.'''

from time import sleep
listatotal = list()
alunotemp = list()
notatemp = list()

aluno = list()
nota = list()
media = list()

print('-='*20)
print(f'{"BOLETIM":^40}')
print('-='*20)

while True:
    alunotemp.append(str(input('Informe o nome do Aluno --> ').strip().capitalize()))
    notatemp.append(float(input('Nota 1: ')))
    notatemp.append(float(input('Nota 2: ')))
    media.append((notatemp[0]+notatemp[1])/2)
    listatotal.append(alunotemp[:])
    listatotal.append(notatemp[:])
    alunotemp.clear()
    notatemp.clear()

    cond = str(input('Deseja continuar? [S/N] \n')).strip().upper()
    while cond not in 'SsNn':
        cond = str(input('Informe uma opção correta [S/N] --> '))
    if cond in 'Nn':
        break

print('-='*20)
print()
print('Nª  /  ALUNO       MÉDIA')
print('-'*20)
for c in range(0, len(listatotal), 2):
    aluno.append(listatotal[c])
for c2, d in enumerate(listatotal):
    if c2 == 1 or c2 % 2 == 1:
        nota.append(d)

for contador in range(0, len(aluno)):
    print(f'{contador}    {aluno[contador]}        {media[contador]}')
print('-='*20)

while True:
    deseja = int(input(f'Deseja ver a nota de qual aluno? (999 interrompe) --> '))
    if deseja == 999:
        break
    print(f'Notas de {aluno[deseja]} são {nota[deseja]}')
    print('-'*25)

print(f'FINALIZANDO O PROGRAMA...')
sleep(2)
print(f' <<< VOLTE SEMPRE >>>')









