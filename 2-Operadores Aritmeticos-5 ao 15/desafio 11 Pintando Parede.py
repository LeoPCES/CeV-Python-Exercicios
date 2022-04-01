#Ler largura e altura. Calcular area da parede e qntd de tinta (1l de tinta pinta 2m² de parede)

print('\033[1;91mVamos calcular quantos litros de tinta vai na sua parede\033[m\n')
a = float(input('Informe a altura em metros:'))
l = float(input('Informe a largura em metros: '))
area = a * l
tinta = area / 2
print('Sua parede tem {}m², e precisará de {} litros de tinta.'.format(area, tinta))