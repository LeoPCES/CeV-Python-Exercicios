'''Crie um programa que o usuario digite uma expressao qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressao passada esta com os parenteses abertos
e fechados na forma correta.
Ex:
correto --> 5 + (5/(2+3))
invalido --> )5+ 3(5*4)) '''

print('='*80)
print(f'{"PROGRAMA PARA LER EXPRESOES FECHADAS CORRETAMENTE!":^80}')
print('='*80)

expressao = str(input('Digite a expressão: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está inválida!')


