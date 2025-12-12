import random

n = random.randint(1,5)
a = int(input('O computador pensou num número entre 0 e 5, qual é que achas que é? '))
if a==n:
    print('Parabéns acertas-te!')
else:
    print('O número escolhido foi {}. Tenta novamente!'.format(n))