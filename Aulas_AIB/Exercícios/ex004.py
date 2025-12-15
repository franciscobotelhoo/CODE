#Exercício 4
#Crie um programa que leia 3 variáveis. Retorne a informação se cada variável é numérica, alfabética e/ou alfanumérica.

i1 = input('Introduza o 1º item para identificação: ')
i2 = input('Introduza o 2º item para identificação: ')
i3 = input('Introduza o 3º item para identificação: ')

print(f'O 1º item ({i1}) tem as seguintes características: \nNumérico - {i1.isnumeric()} \nAlfabético - {i1.isalpha()} \nAlfanumérico - {i1.isalnum()} ')
print(f'O 2º item ({i2}) tem as seguintes características: \nNumérico - {i2.isnumeric()} \nAlfabético - {i2.isalpha()} \nAlfanumérico - {i2.isalnum()} ')
print(f'O 3º item ({i3}) tem as seguintes características: \nNumérico - {i3.isnumeric()} \nAlfabético - {i3.isalpha()} \nAlfanumérico - {i3.isalnum()} ')