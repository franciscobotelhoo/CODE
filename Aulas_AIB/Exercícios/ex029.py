from time import sleep
from random import randint

num = randint(1, 5)
n = int(input('Tente adivinhar o número que estou pensando (entre 1 e 5): '))
print('Processando...')
sleep(3)
if n == num:
    print('Parabéns, você acertou!')
else:    
    print(f'Você errou! O número era {num}.')