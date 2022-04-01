'''Ler data de nascimento de um jovem e diga se é ou não
a hora de se alistar, diga tambem o tempo que falta ou
se já passou do tempo'''

from datetime import date
print('*'*8, 'ALISTAMENTO MILITAR', '*'*8)
sexo = str(input('Informe o seu sexo: \nH: para homem\nF: para mulher\nDigite aqui: ')).capitalize()

if sexo == 'H':
    # variáveis se sexo = homem
    hoje = date.today().year
    nascimento = int(input('Informe o seu ano de nascimento: '))
    idade = hoje - nascimento
    tempo = 18 - idade
    passou = idade - 18
    # condições
    if idade < 18:
        print('Falta ainda {} anos para você se alistar.'.format(tempo))
    elif idade > 18:
        print('Já passou {} anos em que você deveria se alistar.'.format(passou))
    else:
        print('Já é a hora de você se alistar.')
else:
    print('Você não precisa de alistar.')





