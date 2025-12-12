import datetime
ano = datetime.datetime.now().year
anon = int(input('Qual é o ano de nascimento? '))
idade = ano-anon
if idade <= 9:
    print('O atleta compete na categoria mirim')
elif 10 <= idade <= 14:
    print('O atleta compete na categoria infantil')
elif 15 <= idade <= 19:
    print('O atleta compete na categoria júnior')
elif idade == 20:
    print('O atleta compete na categoria sênior')
elif idade >=21:
    print('O atleta compete na categoria master')