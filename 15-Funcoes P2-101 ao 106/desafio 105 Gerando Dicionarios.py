'''Faca um programa que tenha uma funcao notas() que pode receber
varias notas de alunos e vai retornar um dicionário com as seguintes
informacoes:
- Quantidade de notas
- A maior nota
- A menor nota
- A media da turma
- A situacao(opcional)
Adicione também as docstrings.'''

def notas(*valor, sit=False):
    '''
    -> Função de receber notas de uma turma!
    :param valor: recebe as notas.
    :param sit: mostra a situação da turma.
    :return: um dicionário com o Total de notas, maior e menor nota, e a média da turma.
    '''
    cont = maior = menor = media = 0
    dicionario = {}
    for c in range(0, len(valor)):
        cont += 1
        media += valor[c]
        if c == 0:
            maior = menor = valor[c]
        else:
           if valor[c] > maior:
               maior = valor[c]
           if valor[c] < menor:
               menor = valor[c]

    dicionario['Total'] = cont
    dicionario['Maior'] = maior
    dicionario['Menor'] = menor
    dicionario['Media'] = media / len(valor)
    if sit == True:
        if dicionario['Media'] >= 7:
            dicionario['Situação'] = 'Boa!'
        elif 5 <= dicionario['Media'] < 7:
            dicionario['Situação'] = 'Preocupante!'
        else:
            dicionario['Situação'] = 'Horrível!'
    return dicionario


#principal
resp = notas(8, 2, 4)
print(resp)
