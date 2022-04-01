#Ler um numero de 0 a 9999 e mostrar na tela os digitos separados
num = int(input('Digite um número entre 0 e 9999: \n'))
# m c d u
# 0 1 2 3
u = num // 1 % 10
d = num // 10 % 10
c =num // 100 % 10
m =num // 1000 % 10

print('Analisando o número:\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(u, d, c, m))