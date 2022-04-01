'''Reescreva a funcao leiaint() que fizemos no desafio 104, incluindo
agora a possibilidade da digitacao de um numero de tipo inválido. Aproveite
e crie tambem uma funcao leiafloat() com a mesma funcionalidade.'''

def leiaInt(txt):
   while True:
       try:
           n = int(input(txt))
       except (ValueError, TypeError):
           print('Por favor, digite um numero inteiro válido!')
           continue
       except (KeyboardInterrupt):
           print('\nUsuário preferiu não digitar esse número.')
           return 0
       else:
           return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('Por favor, digite um numero real válido!')
            continue
        except (KeyboardInterrupt):
            print('\nUsuário preferiu não digitar esse número.')
            return 0
        else:
            return n


n = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um numero real: ')
print(f'Voce digitou o numero inteiro {n}, e o real {n2}')