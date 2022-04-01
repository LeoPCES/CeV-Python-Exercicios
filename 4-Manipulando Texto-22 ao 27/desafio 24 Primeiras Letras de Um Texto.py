#desafio: verificar se uma cidade começa ou não com SANTO
cit = str(input('Informe uma cidade: \n')).title()
part = cit.split()
condi = 'Santo' in part[0]

print(condi)


