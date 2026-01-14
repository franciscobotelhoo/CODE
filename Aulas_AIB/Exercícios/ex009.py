#Exercício 009
#Crie um programa que lê um valor inteiro. Apresente na consola a tabuada desse valor.

n = int(input('Digite um valor inteiro para o qual quer saber a tabuada: '))

for i in range(1,11):
    if i == 1:
        print(f'\n{n} x {i} = {n*i}')
    print(f'{n} x {i} = {n*i}')

# print(f'\n{n} x {1} = {n}')
# print(f'{n} x {2} = {n*2}')
# print(f'{n} x {3} = {n*3}')
# print(f'{n} x {4} = {n*4}')
# print(f'{n} x {5} = {n*5}')
# print(f'{n} x {6} = {n*6}')
# print(f'{n} x {7} = {n*7}')
# print(f'{n} x {8} = {n*8}')
# print(f'{n} x {9} = {n*9}')
# print(f'{n} x {10} = {n*10}')