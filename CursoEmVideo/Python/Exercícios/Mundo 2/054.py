import datetime
m = 0
nm = 0
ano = datetime.datetime.now().year
for c in range(0,7):
    n= int(input('Digite o ano de nascimento: '))
    if ano-n>=18:
        m = m +1
    elif ano-n<18:
        nm = nm + 1
print('{} são maiores de idade.\n{} são menores de idade'.format(m,nm))