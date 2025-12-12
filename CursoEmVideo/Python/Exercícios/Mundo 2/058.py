import random

n = random.randint(0,10)
tentativa = int() 
c = int()
while n != tentativa:
    tentativa = int(input('Digite um número entre 0 e 10: '))
    if tentativa == n:
        print('Parabéns você adivinhou o número no qual a CPU pensou')
        print('Você tentou {} vezes até acertar.'.format(c+1))
    else:
        print('Número errado! Tente novamente.')
        c += 1