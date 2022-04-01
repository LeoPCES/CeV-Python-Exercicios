'''Crie um codigo em Python que teste se o site Pudim está acessivel pelo
computador usado.'''

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print(f'Deu erro ao acessar o site {site}')
else:
    print('Deu certo!')
