#Exercício 4a
#Crie um programa que verifique o tipo primitivo de uma variável, se tem espaços, se é um número, se é alfabético, se é afldanumérico, se está em maiúscula, se está em minúscula e se está capitalizada. 
i1 = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(i1)};')
print(f'Só tem espaços? {i1.isspace()};')
print(f'É um número? {i1.isnumeric()};')
print(f'É alfabético? {i1.isalpha()};')
print(f'É alfanumérico? {i1.isalnum()};')
print(f'Está em maiúscula? {i1.isupper()};')
print(f'Está em minúscula? {i1.islower()};')
print(f'Está capitalizada? {i1.istitle()}.')