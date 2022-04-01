'''Melhorar o desafio 28 onde o computador vai 'pensar' em um numero
entre 0 e 10. So que agora o jogador vai tentar adivinhar ate acertar,
mostrando no final quantos palpites foram necessarios para vencer!'''

from random import randint
print('\033[1;32m*-*'*8, 'JOGO DE ADIVINHAÇÃO', '*-*'*8, '\033[m')

n = int(input('Pense em um numero entre 0 e 10: '))
sorte = randint(0,10)
palpite = 1

while n != sorte:
    n = int(input('Tente denovo: '))
    palpite += 1

print('\033[1;31mPARABÉNS VOCÊ GANHOU!\033[m')
print('\033[1;97mNumero sorteado: {}\033[m'.format(sorte))
print('\033[1;34mForam necessarios {} palpites.\033[m'.format(palpite))
