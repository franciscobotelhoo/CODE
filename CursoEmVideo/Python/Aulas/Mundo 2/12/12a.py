nome = str(input('Qual é o seu nome? '))
if nome == 'Xico':
    print('Que belo nome! <3')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print('Tão sem graça. É muito comum.')
elif nome in 'Ana Joana Margarida Isabel':
    print('Belo nome para uma menina')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))