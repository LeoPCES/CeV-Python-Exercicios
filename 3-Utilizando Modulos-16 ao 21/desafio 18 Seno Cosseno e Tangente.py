import math
n = float(input('Digite um angulo que você deseja: '))
sn = math.sin(math.radians(n))
print("O valor de {} tem o seno de {:.2f}".format(n, sn))
cn = math.cos(math.radians(n))
print('O valor de {} tem o cosseno de {:.2f}'.format(n, cn))
tn = math.tan(math.radians(n))
print('O valor de {} tem a tangente de {:.2f30}'.format(n, tn))
