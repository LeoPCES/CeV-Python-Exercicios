ficha = list()
while True:
    nome = str(input('Nome --> '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    if resp in 'Nn':
        break

print('-='*20)
print(f'{"Nª":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-='*20)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    cond = int(input('Deseja mostrar a nota de qual aluno? (999 INTERROMPA): '))
    if cond == 999:
        print('FINALIZANDO...')
        break
    if cond <= len(ficha)-1:
        print(f'Notas de {ficha[cond][0]} são {ficha[cond][1]}')

print('<<<FINALIZANDO...>>>')
