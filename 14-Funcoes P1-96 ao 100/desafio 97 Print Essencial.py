'''faca um programa que tenha uma funcao chamada escreva(),
que recebe um texto qualquer como parametro e mostre uma
mensagem com tamanho adaptavel.
Ex:
~~~~~~~~
  ola
~~~~~~~~
'''
def escreva(txt):
    print('*'* (len(txt)+2))
    print(f' {txt}')
    print('*' * (len(txt)+2))


#inicio
escreva('batatinha')