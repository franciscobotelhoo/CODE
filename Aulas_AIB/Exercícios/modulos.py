'''import math

num = int(input("Digite um número: "))
raiz = math.sqrt(num)
print(f"A raiz quadrada de {num} é {raiz}")'''

'''from math import sqrt

num = int(input("Digite um número: "))
raiz = sqrt(num)
print(f"A raiz quadrada de {num} é {raiz}")'''

from math import sqrt, floor

num = int(input("Digite um número: "))
raiz = sqrt(num)
valor_final = floor(raiz)
print(f"A raiz quadrada de {num} é {valor_final:.2f}")

