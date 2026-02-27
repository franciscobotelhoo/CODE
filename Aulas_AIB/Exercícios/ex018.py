#Crie um programa que peça o valor de um ângulo (0º -360º), apresente os valores do seno, cosseno e tangente.

import math
from emoji import emojize

print('EXERCÍCIO 018 - Funções trignométricas:')
angulo = float(input("\nIntroduza o ângulo pretendido: "))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(emojize(f'\nO :boomerang:   {angulo}º corresponde: Seno - {seno:.2f}, Cosseno - {cosseno:.2f} e Tangente - {tangente:.2f}.'))