import math

n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
on = bool(True)

while on == True:
    print('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa')
    op = int(input('O que deseja fazer: '))

    if op == 1:
        print('A soma de {} e {} é de {}'.format(n1, n2, n1+n2))
    if op == 2:
        print('A multiplicação de {} e {} é de {}'.format(n1, n2, n1*n2))
    if op == 3:
        if n1 > n2:
            print('O número {} é maior que o número {}'.format(n1, n2))
        else:
            print('O número {} é maior que o número {}'.format(n2, n1))
    if op == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    if op == 5:
        on = bool(False)
print('------Fim------')