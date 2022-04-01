'''programa para calcular a media e mostrar a situação'''

print('*---*'*5, 'PROGRAMA PARA CALCULAR A MÉDIA', '*--*'*5)
n1 = float(input('Informe valor da nota 1: '))
n2 = float(input('Informe o valor da nota 2:'))
media = (n1 + n2) / 2

if media < 5:
    print('Sua média é {:.1f} e você foi reprovado.'.format(media))
elif media >= 7:
    print('Sua média foi {:.1f} e você foi aprovado.'.format(media))
else:
    print('Sua média é de {:.1f} e você está de recuperação.'.format(media) )
