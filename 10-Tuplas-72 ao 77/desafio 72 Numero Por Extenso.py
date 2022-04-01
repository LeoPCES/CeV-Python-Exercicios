'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero a vinte.
Seu programa devera ler um numero pelo teclado entre 0 e 20 e MOSTRA-LO por
Extenso.'''

listagem = ('Zero', 'Um', 'Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis', 'Dezessete', 'Dezoito','Dezenove', 'Vinte')
n = 0

while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você escolheu o {listagem[n]}')
        break


