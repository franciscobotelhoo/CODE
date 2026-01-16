#Exercício 011
#Crie um programa que lê dois valores correspondentes à altura e largura de uma parede. Sabendo que cada m^2 utiliza-se 0.35l e cada litro de tinta custa 13€. Apresente a quantidade de tinta e o valor que gastará para pintar a parede.

print('==================================\n Calculadora de preços de pintura\n==================================')

h = float(input('\nIntroduza a altura da parede: '))
l = float(input('\nIntroduza a largura da parede: '))

a = h*l

print(f'\nSabendo que cada m^2 utiliza-se 0.35l e cada litro de tinta custa 13€. Para pintar a parede você irá gastar {a*0.35}l de tinta e {(a*0.35)*13:.2f}€')
