#Exercício 015
#Crie um programa que pede ao utilizador o número de dias que alugou uma viatura. Peça também o número de Km que realizou no aluguer. Calcule o valor a pagar, sabendo 15€/dia e 0,35€/km

print('=========================================\n Calculadora de preços a pagar de aluger\n=========================================')

nd = int(input('\nIntroduza o nº de dias pelo qual alugou a viatura: '))
km = float(input('\nIntroduza a quantidade de Km que fez com a viatura: '))

print(f'\nTotal a pagar: {(nd*15)+(km*0.35):.2f}€')