#Exercício 008
#Crie um programa que lê um valor decimal, que corresponde à altura do utilizador em metros. Apresente esse mesmo valor convertido em centímetros e milímetros.

h = float(input('Escreva a sua altura em metros: '))

print(f'Você mede {h*100} cm ou {h*1000} mm.')