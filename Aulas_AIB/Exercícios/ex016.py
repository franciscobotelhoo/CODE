#Crie um programa que lê um numero decimal e através da função trunc(), apresente a parte inteira do numero.

from math import trunc

print('EXERCÍCIO 016 - Apresentar a parte inteira de um número decimal')
num = float(input("\nIntroduza um valor decimal: "))
print(f"\nA parte inteira do valor {num} é {trunc(num)}.")