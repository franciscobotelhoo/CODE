#Exercício 004a
#Crie um programa que verifique o tipo primitivo de uma variável, se tem espaços, se é um número, se é alfabético, se é afldanumérico, se está em maiúscula, se está em minúscula e se está capitalizada. 

i1 = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(i1)};')   #Verificação do tipo primiitivo
print(f'Só tem espaços? {i1.isspace()};')              #Verificação se a variável são apenas espaços
print(f'É um número? {i1.isnumeric()};')               #Verificação se a variável são números
print(f'É alfabético? {i1.isalpha()};')                #Verificação se a varíavel é alfabética
print(f'É alfanumérico? {i1.isalnum()};')              #Verificação se é alfabética e numérica
print(f'Está em maiúscula? {i1.isupper()};')           #Verificação se está em maiúscula
print(f'Está em minúscula? {i1.islower()};')           #Verificação se está em minúscula
print(f'Está capitalizada? {i1.istitle()}.')           #Verificação se está capitalizada