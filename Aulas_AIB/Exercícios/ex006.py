#Exercício 006
#Crie um programa que lê um número. Apresente na consola o dobro, o triplo, e a raiz quadrada

n = float(input('Digite um número: '))

#Versão 01:
print('Versão 01:')
print(f'O dobro de {n} é {n*2}.\nO triplo de {n} é {n*3}.\nA raiz quadrada de {n} é {n**(1/2)}')

#Versão 02:

dobro = n*2
triplo = n*3
sqrt = n**(1/2)
print('\nVersão 02:')
print(f'O dobro de {n} é {dobro}.\nO triplo de {n} é {triplo}.\nA raiz quadrada de {n} é {sqrt}')