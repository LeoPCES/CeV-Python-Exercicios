'''Crie uma Tupla preenchida com os 20 primeiros colocados da tabela do
campeonato brasileiro de futebol, na ordem de colocaçao. Depois mostre:
A) os 5 primeiros
B) os ultimos 4 colocados.
C) time em ordem alfabetica.
D) Em que posicao esta o time de chapecoense.'''

times = ('América - MG', 'Atlético - PR', 'Atlético-GO', 'Atlético-MG', 'Avaí', 'Botafogo', 'Ceará SC', 'Corinthians',
         'Coritiba', 'Flamengo','Cuiabá', 'Fluminense', 'Goiás', 'Fortaleza', 'Internacional', 'Juventude',
         'Palmeiras', 'Chapecoense', 'Bragantino', 'Santos')

print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('='*15)
print(f'Os ultimos 4 colocados são: {times[-4:]}')
print('='*15)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('='*15)
print('O chapecoense está em {}ª posição'.format(times.index('Chapecoense')+1))