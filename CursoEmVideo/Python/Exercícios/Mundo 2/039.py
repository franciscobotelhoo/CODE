import datetime
ano = datetime.datetime.now().year
anon = int(input('Em que ano nasceste? '))
idade = ano - anon
falta = 18 - idade
if idade>18:
    passou = -1 * falta
    print('Já foste ao dia da defesa nacional há {} anos, muito bem. Espero que tenhas gostado!'.format(passou))
elif idade<18:
    print('Ainda não foste ao dia da defesa nacional, vais daqui a {} ano(s). Vais gostar, confia!'.format(falta))
elif idade == 18:
    print('É este ano o teu dia da defesa nacional. Espero que gostes, ou tenhas gostado!')
