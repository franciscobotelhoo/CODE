import math

a = float(input('Valor do ângulo em Graus(º): '))
sina = math.sin(math.radians(a))
cosa = math.cos(math.radians(a))
tana = math.tan(math.radians(a))
print('Para um ângulo de {}º \ntemos que o seu seno é de {:.2f}, \no seu cosseno é de {:.2f}, \ne a sua tangente é de {:.2f}'.format(a,sina,cosa,tana))