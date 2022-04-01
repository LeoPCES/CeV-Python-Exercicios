'''Crie um programa que tenha uma funcao fatorial() que receba dois
parametros: o primeiro que indique o numero a calcular e o outro
chamado show, que sera um valor logico(opcional) indicando se será
mostrado ou não na tela o processo de cálculo fatorial.'''

def fatorial(n1=0, show=False):
    '''
    --> Calcula o fatorial de um número.
    :param n1: Número a ser calculado
    :param show: Opcional (mostrar ou não a conta)
    :return: O valor do fatorial de um número n1.
    '''
    fat = 1
    while n1 > 0:
        fat *= n1
        if show == True:
            if n1 > 1:
                print(f'{n1} x ', end='')
            else:
                print(f'{n1} = ', end='')
        n1 -= 1
    return fat


print(fatorial(3,show=True))
