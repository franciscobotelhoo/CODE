p = float(input('Digite o seu peso em kg (Ex: 69.9): '))
a = float(input('Digite a sua altura em cm (Ex: 174): '))
imc = (p/(a**2))*10000
print('{:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso.')
elif 18.5 <= imc < 25:
    print('Peso Ideal.')
elif 25 <= imc < 30:
    print('Sobrepeso.')
elif 30 <= imc < 40:
    print('Obesidade.')
elif imc >= 40:
    print('Obesidade Mórbida.')