'''Faça um programa que leia o SEXO de uma pessoa.
Só aceita o valor de 'F' ou 'M'.
Caso esteja errado, Peça a digitação novamente!'''


sexo = ''

while sexo != 'M' and sexo!='F':
    sexo = str(input('Informe seu sexo: \n[M] para Masculino\n[F] para Feminino\nDigite: ')).upper().strip()
    if sexo !='M' and sexo!= 'F':
        print('\033[1;31mDigite novamente.\033[m')
    if sexo == 'M':
        print('Cadastro \033[1;32mMasculino\033[m realizado com sucesso.')
    if sexo == 'F':
        print('Cadastro \033[1;32mFeminino\033[m realizado com sucesso.')

print('\033[1;33;107m===FIM===\033[m')

#jeito que guanabara fez
'''sexo = str(input('Informe seu sexo: [M/F]')).upper().strip()
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Digite nvoamente: ')).strip().upper()
print('Sexo \033[1;31m{}\033[m cadastrado com sucesso'.format(sexo))'''