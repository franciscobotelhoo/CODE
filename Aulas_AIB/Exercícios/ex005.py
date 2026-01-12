#Exercício 005
#Crie um programa que lê um número inteiro, apresente na consola o seu sucessor e o seu antecessor

n1 = int(input('Digite um valor inteiro: '))

#Versão 01:
print('\nVersão 1')
print(f'O antecessor de {n1} é {n1-1}. \nO sucessor de {n1} é {n1+1}')

#Versão 02:
antecessor = n1-1
sucessor = n1+1

print('\nVersão 2')
print(f'O antecessor de {n1} é {antecessor}. \nO sucessor de {n1} é {sucessor}')
