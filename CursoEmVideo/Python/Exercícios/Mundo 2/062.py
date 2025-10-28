pt = float(input('Qual é o primeiro termo da progressão aritmética: '))
r = float(input('Qual é a razão da progressão aritmética: '))
c = 1
d = 1
while c != 11:
    print(pt + ((c -1)*r))
    c += 1

sn = str(input('Você quer mais alguns termos? [Y/N]: ')).upper()

if sn == 'Y':
    d = int(input('Quantos mais termos deseja ver? '))
elif sn == 'N':
    print('----FIM----')
    exit()
else:
    print('Opção Inválida')
    

t = c+d

if d == 0:
    print('----FIM----')
if d != 0:
    while c != t:
        print(pt + ((c -1)*r))
        c += 1