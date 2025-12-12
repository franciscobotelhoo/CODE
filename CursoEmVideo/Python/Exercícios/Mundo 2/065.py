n = 0
soma = 0
maior = None
menor = None
c = 0

on = bool(True)
po = ''

while on == True:
    n = float(input('Digite um número: '))
    c += 1
    soma += n
    po = str(input('Deseja continuar? [Y/N]: ')).upper()
    if maior is None:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        if po == 'N':
            print(c)
            print('A média entre todos os valores foi de {}'.format(soma/(c)))
            print('O maior valor digitado foi {}'.format(maior))
            print('O menor valor digitado foi {}'.format(menor))
            break
