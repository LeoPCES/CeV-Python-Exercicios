'''Categoria de atletas de acordo com a idade
9 anos, 14, 19 e 25'''

from datetime import date

print('*---*'*6, 'PROGRAMA DE CLASSIFICAÇÃO DE NADADORES', '*---*'*6)
nascimento = int(input('Informe o ano de nascimento: '))

ano = date.today().year
idade = ano - nascimento

if idade <= 9:
    print('Você nasceu em {} então sua categoria é MIRIM'.format(nascimento))
elif 9 < idade <=14:
    print('Você nasceu em {} então sua categoria é INFANTIL'.format(nascimento))
elif 14 < idade <=19:
    print('Você nasceu em {} então sua categoria é JUNIOR'.format(nascimento))
elif idade == 20 :
    print('Você nasceu em {} então sua categoria é SÊNIOR'.format(nascimento))
elif idade > 20:
    print('Você nasceu em {} então sua categoria é MASTER'.format(nascimento))




