km = float(input('Quantos Km foram percorridos? '))
d = int(input('Por quantos dias o carro esteve alugado? '))
print('O preço a pagar é de {:.2f}R$, {:.2f}R$ pelos dias, e {:.2f}R$ pelos Km percorridos'.format(d*60+km*0.15,d*60,km*0.15))