'''Crie um programa que tenha uma tupla unica com nomes de produtos
e seus respectivos precos, na sequencia. No final, mostre uma listagem
dep recos, organizando os dados em forma TABULAR.'''

print('-'*30)
print('{:^30}'.format('LISTAGEM DE PREÇOS'))
print('-'*30)

listagem = ('Arroz', 15.50, 'Leite', 4 ,'Pão', 5.75 , 'Café', 8)

for c in range(0, 8, 2):
    print(f'{listagem[c]:.<25} R$ {listagem[c+1]:.2f}')


