d = float(input('Qual é a distância da sua viagem? '))
if d<=200:
    print('A sua viagem de {}Km irá custar {}R$'.format(d,(d*0.50)))
else:
    print('A sua viagem de {}Km irá custar {}R$'.format(d,(d*0.45)))