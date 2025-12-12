ano = int(input('Digite um ano: '))
quatro = ano%4
cem = ano%100
quatrocentos = ano%400
if quatro == 0 and cem == 0 and quatrocentos == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} é um ano comum'.format(ano))
