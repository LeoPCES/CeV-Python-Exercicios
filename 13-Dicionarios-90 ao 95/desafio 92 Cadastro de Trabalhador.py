'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de 0,
o dicionario recebera também o ANO DE CONTRATACAO e o SALARIO. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai aposentar.'''


from datetime import date
anoatual = date.today().year
tabela = dict()
tabela['Nome'] = str(input('Informe o nome: ')).title().strip()
tabela['Idade'] = int(input('Informe seu ano de nascimento: '))
ano = tabela['Idade']
tabela['Idade'] = anoatual - ano
tabela['CTPS'] = int(input('Informe sua carteira de trabalho[0 não tem]: '))

if tabela['CTPS'] != 0:
    tabela['Contratação'] = int(input('Informe o ano de contratação --> '))
    tabela['Salário'] = float(input('Informe seu salário --> R$ '))
    tabela['Aposentadoria'] = (tabela['Contratação'] - ano) + 35

for k, v in tabela.items():
    print(f'- {k} --> {v}')

print('Fim do programa...')