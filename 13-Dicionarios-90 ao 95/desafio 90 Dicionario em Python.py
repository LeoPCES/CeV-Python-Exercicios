''' ler nome e media de um aluno, guardando em um dicionario.
No final, mostre o conteudo da estrutura na tela.'''

tabela = dict()

tabela['Aluno(a)'] = str(input('Informe o nome --> ')).strip().title()
tabela['media'] = float(input(f'Média de {tabela["Aluno(a)"]} --> '))
print('-=-'*8)

if tabela['media'] >= 7:
    tabela['situação'] = 'Aprovado(a)'
else:
    tabela['situação'] = 'Reprovado(a)'

for key, valor in tabela.items():
    print(f'- {key}: {valor}')



#aprendizado
'''estado = dict()
brasil = list()

for c in range (0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())

for estado in brasil:
    for v in estado.items():
        print(v, end=' ')'''