'''Crie um programa que tenha uma funcao chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa, retornando
um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou
OBRIGATORIO nas eleicoes.'''

def voto(nascimento):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if 18 <= idade <= 70:
        return f'Com {idade} anos --> Seu voto é Obrigatório!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos --> Seu voto é Opcional!'
    else:
        return f'Com {idade} anos --> Voto negado!'


ano_de_nascimento = int(input('Informe seu ano de nascimento: '))
print(voto(ano_de_nascimento))
