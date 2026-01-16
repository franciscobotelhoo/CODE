#Exercício 013
#Crie um programa que pede ao utilizador o valor do seu salário e a percentagem do seu aumento. Calcule o valor do aumento e apresente o valor final do salário do utilizador.

print('===================================\n Calculadora de aumentos salariais\n===================================')

s = float(input('\nIntroduza o valor do seu salário: '))
a = float(input('\nIntroduza a percentagem do seu aumento salarial: '))
print(f'\nApós um aumento salarial de {a}%, o seu salário de {s:.2f}€ é atualizado para {s + (s*(a/100)):.2f}€.')