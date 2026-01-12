#calculos aritmeticos
#criação de um programa que apresente a soma, subtração, multiplicação, divisão, potência, divisão inteira e o resto da divisão entre dois números inteiros.
n1 = int(input('Digite um valor inteiro: '))
n2 = int(input('Digite outro valor inteiro que não 0: '))

while n2 == 0:
    n2 = int(input('Um valor diferente de 0, por favor: '))

print(f'Soma: {n1} + {n2} = {n1+n2}. Subtração: {n1} - {n2} = {n1-n2}. Multiplicação: {n1} x {n2} = {n1*n2}. Divisão: {n1} / {n2} = {n1/n2}. \nPotência: {n1} ^ {n2} = {n1**n2}. Divisão Inteira: {n1} / {n2} = {n1//n2}. Resto da divisão: {n1} / {n2} = {n1%n2}.')