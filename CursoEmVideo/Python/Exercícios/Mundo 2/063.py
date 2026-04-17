n = int(input('Quantos termos da sequência de Fibonacci você deseja ver? '))
c = 3
termo = 0
t1 = 0
t2 = 1

print(f'{t1} -> {t2}', end='')

while c <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    c += 1
    t1 = t2
    t2 = t3
    