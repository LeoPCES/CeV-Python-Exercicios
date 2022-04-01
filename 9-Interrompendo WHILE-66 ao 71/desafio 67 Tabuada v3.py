'''Programa que mostra a tabuada de Varios Numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa sera interrompido
quando o valor solicitado for NEGATIVO.'''

print ('=*=*'*6 ,'TABOADA', '=*=*'*6)

while True:

    n = int(input('Digite um numero: '))
    if n < 0:
        break
    for c in range(1, 11):
        produto = n * c
        print(f'{n} x {c} = {produto}')
    print('=' * 18)

print('FIM DO PROGRAMA')
