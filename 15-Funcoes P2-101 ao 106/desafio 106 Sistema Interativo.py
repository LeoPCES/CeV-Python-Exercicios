'''Faca um mini-sistema que utilize interactive help do Python.
O usuario vai digitar o comando e o manual vai aparecer. Quando
o usuário digitar a palavra "FIM" o programa se encerrará.
OBS: use cores.'''

c = ('\033[m',
     '\033[0;97;41m',  # vermelho
     '\033[0;97;42m',  # verde
     '\033[0;30;107m', # branco
     '\033[0;97;44m'   # azul

     )

def ajuda(txt):
    título(f'Acessando o manual do comando \'{txt}\'', 4)
    print(c[3], end='')
    help(txt)
    print(c[0], end='')


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


#programa principal

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO...', 1)