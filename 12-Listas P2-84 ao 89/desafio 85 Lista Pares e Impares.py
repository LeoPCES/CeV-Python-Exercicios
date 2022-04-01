'''ler 7 numeros e cadastrar em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostrar os valores pares e ímpares em ordem crescente.
listatotal = [[pares][impares]] '''

total = [[], []]

for contador in range (0,7):
    n = int(input('Informe um numero inteiro: \n'))
    if n % 2 ==0:
        total[0].append(n)
    elif n % 2 == 1:
        total[1].append(n)

total[0].sort() # organizar os pares
total[1].sort() # organizar os ímpares
print(f'Os pares são: {total[0]}')
print(f'Os ímpares são: {total[1]}')

