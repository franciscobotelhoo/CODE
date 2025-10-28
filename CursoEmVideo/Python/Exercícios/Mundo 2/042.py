l1 = float(input('Comprimento de um lado:'))
l2 = float(input('Comprimento de outro lado:'))
l3 = float(input('Comprimento de outro lado:'))
if l1+l2>l3 and l1 +l3>l2 and l2+l3>l1:
    print('Estes três lados conseguem formar um triângulo.')
else:
    print('Estes três lados não conseguem formar um triângulo.')
    quit()
if l1==l2 and l1==l3:
    print('O triângulo é equilátero.')
elif l1==l2 or l1==l3 or l2==l3:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.') 