pt = float(input('Qual é o primeiro termo da progressão aritmética: '))
r = float(input('Qual é a razão da progressão aritmética: '))
for c in range(1,11):
    print(pt + (c - 1)*r)