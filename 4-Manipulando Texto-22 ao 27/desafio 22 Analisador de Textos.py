#Desafio --> Mostrar qnts letras maiusculas e minusculas, quantas letras ao /rtodo, quantas letras o primeiro nome
nome = str(input('Informe um nome completo: \n')).strip()
maius = nome.upper()
minus = nome.lower()
dividido = nome.split()
print('Nome maiúsculo: {}\nNome minúsculo: {}\n'.format(maius, minus))
print('O nome completo tem {} letras\nO primero nome tem {} letras.'.format(len(''.join(dividido)), len(dividido[0])))

