'''Ler um numero Inteiro e diga se é ou não PRIMO'''

n = int(input('Digite um numero inteiro: \n'))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[1;31m', end='')
        tot += 1
    else:
        print('\033[1;37m', end='')
    print('{} '.format(c), end='')

print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot > 2:
    print('O número {} não é primo.'.format(n))
else:
    print('O numero é primo.')