#Exercício 014
#Crie um programa que pede ao utilizador a temperatura em graus celsius - Cº. Converta o valor para obter o seu correspondente em graus Fahrenheit - Fº.

print('============================\n Conversora de temperaturas\n============================')

c = float(input('\nIntroduza o valor da temperatura atual (graus Celsius): '))

print(f'\nA temperatura de {c:.2f}ºC, corresponde a {c*1.8+32:.2f}ºF')