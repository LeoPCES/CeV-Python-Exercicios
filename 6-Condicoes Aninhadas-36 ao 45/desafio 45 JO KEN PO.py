from random import randint
print('\033[1;97;41m{:*^60}\033[m'.format("JOKENPO"))

#usuario

print(''''Escolha um elemento:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
n = int(input('Escolha:'))
if n == 1:
    escolha = 'PEDRA'
elif n == 2:
    escolha = 'PAPEL'
elif n == 3:
    escolha = 'TESOURA'
else:
    print('\033[1;37;41mINSIRA UM VALOR VÁLIDO\033[m')


#computador

bot = randint(1, 3)
if bot == 1:
    escolhabot = 'PEDRA'
elif bot == 2:
    escolhabot = 'PAPEL'
else:
    escolhabot = 'TESOURA'

#condicao do jogo

if n == 1 and bot == 3:
    print('Parabéns, você ganhou!\nVocê escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))
elif n == 1 and bot == 2:
    print('Você perdeu!\n Você escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))

elif n == 2 and bot == 1:
    print('Parabéns, você ganhou!\nVocê escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))
elif n == 2 and bot == 3:
    print('Você perdeu!\n Você escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))

elif n == 3 and bot == 2:
        print('Parabéns, você ganhou!\nVocê escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))
elif n == 3 and bot == 1:
        print('Você perdeu!\n Você escolheu: {}\nComputador: {}.'.format(escolha, escolhabot))
elif n == bot:
    print('\033[1;30;41mEMPATE\033[m\nVocê escolheu:{}\nComputador: {}'.format(escolha, escolhabot))




