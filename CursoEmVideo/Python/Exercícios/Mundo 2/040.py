n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1+n2)/2
if m<5.0:
    print('REPROVADO!')
elif 5.0 <= m <= 6.9:
    print('RECUPERAÇÃO!')
elif m>=7.0:
    print('APROVADO!')