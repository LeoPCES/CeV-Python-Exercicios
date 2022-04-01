'''Ler a velocidade de um carro, se ultrapassar 80km mostrar
uam mensagem dizendo que ele foi multado. A multa vai custar
7,00 por cada km acima do limite'''

vel = float(input('Informe a velocidade do veíuclo: '))
multa = (vel - 80) * 7
if vel>80:
    print('Você foi multado ao passar no radar em {}km/h\nValor da multa: R${:.2f}'.format(vel, multa))
else:
    print('Você passou ao radar em {}km/h'.format(vel))