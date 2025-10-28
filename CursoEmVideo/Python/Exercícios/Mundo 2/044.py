pi = float(input('Preço do produto: '))
print('Condições de pagamento:\n1- À vista dinheiro/cheque: 10% de desconto;\n2- À vista no cartão: 5% de desconto;\n3- Em até 2x no cartão: preço normal;\n4- 3x ou mais no cartão: 20% de juros.')
cp = int(input('Qual opção deseja escolher? '))
if cp == 1:
    pf = pi-(pi*0.10)
    print('O valor a pagar é de {:.2f}'.format(pf))
elif cp == 2:
    pf = pi-(pi*0.05)
    print('O valor a pagar é de {:.2f}'.format(pf)) 
elif cp == 3:
    print('O valor a pagar é de {:.2f}'.format(pi))
elif cp == 4:
    pf = pi + (pi * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    if parcelas < 3:
        print('Número inválido de parcelas para esta opção.')
    else:
        valor_parcela = pf / parcelas
        print('O valor total com juros é de {:.2f}'.format(pf))
        print('Dividido em {} parcelas de {:.2f}'.format(parcelas, valor_parcela))
else:
    print('Opção inválida.')
