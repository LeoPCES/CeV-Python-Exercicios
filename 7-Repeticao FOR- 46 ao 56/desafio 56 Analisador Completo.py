'''Ler nome, idade e sexo de 4 PESSOAS e mostre:
a media da idade;
qual o nome do homem mais velho;
quantas mulheres tem menos de 20.'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0

for p in range (1, 5):
    print('---- {}ª PESSOA ----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Ao todo, são {} mulher com menos de 20 anos'.format(totalmulher20))









