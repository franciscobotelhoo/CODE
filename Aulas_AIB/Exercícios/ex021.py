import math
n = float(input('Digite um número inteiro: '))

if math.trunc(n) % 2 == 0 and n == 0:
    print(f'O número {math.trunc(n)} é par.')
else:
    print(f'O número {math.trunc(n)} é ímpar.')