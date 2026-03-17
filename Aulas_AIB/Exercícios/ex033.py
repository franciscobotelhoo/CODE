#Analisando triângulos
#1ªfase: Importar bibliotecas
#2ªfase: Gerar os lados do triângulo
#3ªfase: Analisar se os lados formam um triângulo
#4ªfase: Analisar o tipo do triângulo (equilátero, isósceles ou escaleno)

from random import randint
from time import sleep
from emoji import emojize

l1 = randint(1, 20)
l2 = randint(1, 20)
l3 = randint(1, 20)

print(emojize('Gerando os lados do triângulo... :gear:'))
sleep(2)
print(emojize(f'Lados gerados: {l1}, {l2}, {l3} :check_mark_button:'))
sleep(2)
print(emojize('Analisando os lados... :eyes:'))
sleep(2)

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print(emojize('Estes três lados conseguem formar um triângulo. :thumbs_up:'))
else:
    print(emojize('Estes três lados não conseguem formar um triângulo. :thumbs_down:'))
    quit()

if l1==l2 and l1==l3:
     print('O triângulo é equilátero.')
elif l1==l2 or l1==l3 or l2==l3:
     print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')