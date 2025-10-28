n = 0
soma = 0
while n != 999:
    n = float(input('Digite um número: '))
    if n != 999:
        soma += n
    else:
        break
print(soma)