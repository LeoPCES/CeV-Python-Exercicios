'''contador de numeros pares entre 1 e 50'''
n = str(input('Digite qualquer coisa para começar: '))
for cont in range(1, 51):
    calc = cont % 2
    if calc == 0:
        print(cont)

print('FIM')