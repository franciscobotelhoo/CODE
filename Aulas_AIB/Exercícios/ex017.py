#Pedir ao utilizador os valores dos catetos de um triângulo retângulo, apresente o valor da hipotenusa.

from math import hypot
from emoji import emojize

print('EXERCÍCIO 017 - Encontrar a hipotenusa de um triângulo')
cateto1 = float(input("\nIntroduza o valor do cateto adjacente: "))
cateto2 = float(input("\nIntroduza o valor do cateto oposto: "))
hipotenusa = hypot(cateto1, cateto2)
print(emojize(f"\nA hipotenusa do :triangular_ruler: com os catetos {cateto1} e {cateto2} é {hipotenusa:.2f}."))