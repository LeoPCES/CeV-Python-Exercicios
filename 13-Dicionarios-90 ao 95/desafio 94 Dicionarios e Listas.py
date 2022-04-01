'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando
os dados de cada pessoa em um dicionario e todos os dicionarios em uma lista.
No final, mostre:
a) quantas pessoas cadastradas
b) a média da idade
c) uma lista com mulheres
d) uma lista com idade ACIMA da média.'''

lista = []
totpessoas = totidade = 0
listamulher = []
lista_media = []
while True:
    info = {}
    info['Nome'] = str(input('Informe o nome: ')).title().strip()
    info['Sexo'] = str(input('Sexo [M/F] --> ')).upper().strip()[0]
    info['Idade'] = int(input('Digite sua idade: '))
    totidade += info['Idade']
    totpessoas += 1
    lista.append(info.copy())
    resp = str(input('Deseja continuar? [S/N] --> ')).upper().strip()[0]
    while resp not in 'SsNn':
        resp = str(input('\033[1;31mOpção inválida!\033[m [S/N] --> ')).upper().strip()[0]
    if resp in 'Nn':
        break

media_idade = totidade / totpessoas
print(f'A) Foram {totpessoas} pessoas cadastradas.')
print(f'B) A média de idade das pessoas é de {media_idade:.1f}')
for p in lista:
    if p['Sexo'] == 'F':
        listamulher.append(p['Nome'])
print(f'C) As mulheres cadastradas são: {listamulher}')
for d in lista:
    if d['Idade'] > media_idade:
        lista_media.append(d['Nome'])
print(f'D) Lista das pessoas que estão acima da média: {lista_media}')
