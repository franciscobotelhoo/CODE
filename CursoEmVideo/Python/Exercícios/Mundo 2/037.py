numero = int(input('Digite um número: '))
bc = int(input('Qual é a base de conversão para qual {} será convertida?\n1 para binário\n2 para octal\n3 para hexadecimal\nEscolha a sua opção: '.format(numero) ))
if bc == 1:
    nb = bin(numero)
    print('O numero {} convertido para binário é {}'.format(numero, nb))
elif bc == 2:
    no = oct(numero)
    print('O numero {} convertido para octal é {}'.format(numero, no))
elif bc == 3:
    nh = hex(numero)
    print('O numero {} convertido para hexadecimal é {}'.format(numero, nh))
else:
    print('Opção inválida.')