'''Contagem regressiva para o estouro de fogos de artificio
indo de 10 até 0.'''

from time import sleep
print("\033[1;97;41mCONTAGEM FOGOS DE ARTIFICIO\033[m")
n = str(input('Digite qualquer valor para começar:'))
for x in range(10, 0-1, -1):
    sleep(1)
    print(x)
print('\033[1;31;47mBOOOOOOOOOOOOM\033[m')