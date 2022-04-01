#mostrar na tela o TIPO PRIMITIVO e as informaçoes possiveis

tipo = input("Digite alguma coisa --> ")

print(f'O tipo primitivo desse valor é --> {type(tipo)}')
print(f'O valor digitado só tem espaços? -->{tipo.isspace()}')
print(f'O valor digitado só tem numeros? -->{tipo.isnumeric()}')
print(f'O valor digitado é alfabético? -->{tipo.isalpha()}')
print(f'O valor digitado é alfanumérico? -->{tipo.isalnum()}')
print(f'O valor digitado está em maiúsculas? -->{tipo.isupper()}')
print(f'O valor digitado está em minusculas? -->{tipo.islower()}')
print(f'O valor digitado está capitalizado? -->{tipo.istitle()}')
