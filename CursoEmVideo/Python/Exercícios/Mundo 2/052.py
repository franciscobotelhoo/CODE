num = int(input('Digite um número: '))
div = 0

for i in range(1, num+1):
    if num%i == 0:
        div += 1

if div > 2:
    print(f'O número {num} não é primo, pois foi divisível por {div} números')
else:
    print(f'O número {num} é primo, pois foi divisível por {div} números')