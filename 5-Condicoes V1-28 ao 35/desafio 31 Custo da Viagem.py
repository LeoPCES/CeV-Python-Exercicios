'''Calcular preco da passagem, 0,50 para viagens de ate 200km
0,45 para viagens mais longas'''
print('-*-'*10, 'VIAGENS', '-*-'*10 )
km = float(input('Informe a distancia em km da sua viagem: '))
if km<= 200:
    preco = 0.50 * km
else:
    preco = 0.45 * km
print('Para {}km, o preço da viagem será de R${}'.format(km,preco))
print('-*-'*10, 'Obrigado pela preferência!', '-*-'*10 )