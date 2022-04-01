'''Mostrar quantas vezes aparece a letra A
Em que posição aparece na primeira vez
Em que posição aparece na ultima vez'''

frase = str(input('Digite uma frase qualquer: \n')).lower().strip()
print('A letra A aparece: {} vezes.'.format(frase.count('a')))
print('A letra A aparece na primeira vez na posição: {}.'.format(frase.find('a')+1))
print('A letra A aparece na ultima vez na posição: {}'.format(frase.rfind('a')+1))