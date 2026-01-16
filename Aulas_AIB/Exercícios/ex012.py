#Exercício 012
#Crie um programa que pede ao utilizador o valor de um produto e o seu desconto. Calcule o desconto e apresente o valor final ao utilizador.

print('==========================\n Calculadora de descontos\n==========================')

p = float(input('\nPreço do produto: '))
desconto = float(input('\nDesconto a aplicar: '))
d = p*(desconto/100)
pd = p-d
print(f'\nO preço do produto com {desconto}% de desconto é de {pd:.2f}€')