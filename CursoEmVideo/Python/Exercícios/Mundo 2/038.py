n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1>n2:
    print ('O número {}, é maior que o número {}.'.format(n1, n2))
elif n1<n2:
    print ('O número {}, é menor que o número {}.'.format(n1, n2))
else:
    print('Não existe número maior, pois ambos são iguais')        