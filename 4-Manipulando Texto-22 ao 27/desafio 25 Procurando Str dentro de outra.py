#verifica se uma pessoa tem SILVA no nome.
nome = str(input('Infome algum nome: \n')).title().strip()
sobre = 'Silva' in nome
print('Seu nome tem Silva?  {}'.format(sobre))