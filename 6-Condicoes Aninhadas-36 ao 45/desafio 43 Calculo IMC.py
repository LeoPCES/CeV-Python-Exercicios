'''Calculo do IMC mostrando o status da pessoa.'''

print('#'*10, 'PROGRAMA PESO IDEAL IMC', '#'*10)
#dados do usuario
peso = float(input('Informe o seu peso: '))
altura = float(input('Informe sua altura em centímetros: '))
imc = peso / ((altura/100)**2)

#condicoes
if imc < 18.5:
    print('Seu IMC é {:.1f} e você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é {:.1f} e você está no peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é {:.1f} e você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é {:.1f} e você está obeso.'.format(imc))
else:
    print('Seu IMC é {:.1f} e você está com obesidade MÓRBIDA'.format(imc))
