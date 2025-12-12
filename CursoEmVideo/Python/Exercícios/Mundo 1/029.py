v = int(input('Qual era a velocidade do carro? '))
if v >= 80:
    print('Você será multado')
    km = float(input('Quantos quilómetros é que você andou a esta velocidade? '))
    c = km*7
    print('Você terá de pagar {:.2f}R$'.format(c))
else:
    print('Muito bem cidadão')