import math

co = float(input('Qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente: '))
h = math.sqrt(math.pow(co,2)+math.pow(ca,2))
print('A hipotenusa do triângulo cujo cateto oposto é {}, e o cateto adjacente é {}, é {}'.format(co,ca,h))